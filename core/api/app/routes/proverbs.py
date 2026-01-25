from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from typing import List
import random

from app.database import get_db, Proverb
from app.schemas import ProverbCreate, ProverbResponse

router = APIRouter()


@router.get("/proverbs", response_model=List[ProverbResponse])
async def get_all_proverbs(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    category: str = Query(None, description="Filter by category"),
    db: AsyncSession = Depends(get_db)
):
    """Get all proverbs with optional category filtering"""
    query = select(Proverb)
    
    if category:
        query = query.filter(Proverb.category == category)
    
    result = await db.execute(query.offset(skip).limit(limit))
    proverbs = result.scalars().all()
    return proverbs


@router.get("/proverbs/random", response_model=ProverbResponse)
async def get_random_proverb(db: AsyncSession = Depends(get_db)):
    """Get a random Yoruba proverb"""
    # Count total proverbs
    count_result = await db.execute(select(func.count()).select_from(Proverb))
    total = count_result.scalar()
    
    if total == 0:
        raise HTTPException(
            status_code=404, 
            detail="No proverbs available"
        )
    
    random_offset = random.randint(0, total - 1)
    result = await db.execute(select(Proverb).offset(random_offset).limit(1))
    proverb = result.scalar_one_or_none()
    
    return proverb


@router.post("/proverbs", response_model=ProverbResponse)
async def create_proverb(
    proverb: ProverbCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new proverb"""
    db_proverb = Proverb(**proverb.dict())
    db.add(db_proverb)
    await db.commit()
    await db.refresh(db_proverb)
    return db_proverb


@router.get("/proverbs/{proverb_id}", response_model=ProverbResponse)
async def get_proverb(
    proverb_id: int,
    db: AsyncSession = Depends(get_db)
):
    """Get a specific proverb by ID"""
    result = await db.execute(select(Proverb).where(Proverb.id == proverb_id))
    proverb = result.scalar_one_or_none()
    
    if not proverb:
        raise HTTPException(
            status_code=404, 
            detail="Proverb not found"
        )
    
    return proverb
