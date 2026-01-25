from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db, ToneMarking
from app.schemas import ToneMarkingRequest, ToneMarkingResponse
from app.services.tone_service import add_tone_marks

router = APIRouter()


@router.post("/tone-mark", response_model=ToneMarkingResponse)
async def mark_tones(
    request: ToneMarkingRequest,
    db: AsyncSession = Depends(get_db)
):
    """Add tone marks (diacritics) to Yoruba text"""
    try:
        tone_marked_text = add_tone_marks(request.text)
        
        # Save to database
        db_tone_marking = ToneMarking(
            original_text=request.text,
            tone_marked_text=tone_marked_text
        )
        db.add(db_tone_marking)
        await db.commit()
        
        return ToneMarkingResponse(
            original=request.text,
            tone_marked=tone_marked_text
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing tone marking: {str(e)}"
        )


@router.get("/tone-mark/history", response_model=list[ToneMarkingResponse])
async def get_tone_marking_history(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    """Get history of tone marking requests"""
    result = await db.execute(select(ToneMarking).offset(skip).limit(limit))
    history = result.scalars().all()
    
    return [
        ToneMarkingResponse(
            original=item.original_text,
            tone_marked=item.tone_marked_text
        )
        for item in history
    ]
