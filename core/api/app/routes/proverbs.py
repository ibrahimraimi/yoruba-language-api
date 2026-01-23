from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
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
    db: Session = Depends(get_db)
):
    """Get all proverbs with optional category filtering"""
    query = db.query(Proverb)
    
    if category:
        query = query.filter(Proverb.category == category)
    
    proverbs = query.offset(skip).limit(limit).all()
    return proverbs


@router.get("/proverbs/random", response_model=ProverbResponse)
async def get_random_proverb(db: Session = Depends(get_db)):
    """Get a random Yoruba proverb"""
    total = db.query(Proverb).count()
    if total == 0:
        raise HTTPException(
            status_code=404, 
            detail="No proverbs available"
        )
    
    random_offset = random.randint(0, total - 1)
    proverb = db.query(Proverb).offset(random_offset).first()
    
    return proverb


@router.post("/proverbs", response_model=ProverbResponse)
async def create_proverb(
    proverb: ProverbCreate,
    db: Session = Depends(get_db)
):
    """Create a new proverb"""
    db_proverb = Proverb(**proverb.dict())
    db.add(db_proverb)
    db.commit()
    db.refresh(db_proverb)
    return db_proverb


@router.get("/proverbs/{proverb_id}", response_model=ProverbResponse)
async def get_proverb(
    proverb_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific proverb by ID"""
    proverb = db.query(Proverb).filter(Proverb.id == proverb_id).first()
    
    if not proverb:
        raise HTTPException(
            status_code=404, 
            detail="Proverb not found"
        )
    
    return proverb
