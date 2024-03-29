from fastapi import APIRouter
from .Leetcode_Contest.contest_status import contest_status
from .Leetcode_Contest.contest_info import contest_info
import schemas
from .Database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from .Database import models
from typing import List


router = APIRouter(
    prefix="/leetcode",
    tags=["Leetcode"]
)


@router.get("/contest/status")
async def get_contest_status():
    return contest_status()


@router.post("/contest/ranking", response_model=List[schemas.Contest_Ranking_Out])
async def get_contest_ranking(usernames: schemas.Contest_Ranking, db: Session = Depends(get_db)):
    contests = db.query(models.Contest).filter(
        models.Contest.username.in_(usernames.contestants_ids)).all()
    return contests


@router.post("/contest/info", response_model=schemas.Contest_Info_Out)
async def get_contest_info(contest_name: schemas.Contest_Info_In):
    return contest_info(contest_name.contest_name)
