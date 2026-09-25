from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Player
from app.schemas import PlayerCreate, PlayerResponse

router = APIRouter(prefix="/players", tags=["players"])


@router.post("/", response_model=PlayerResponse)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = Player(
        name= player.name,
        team = player.team,
        matches = player.matches,
        wickets=player.wickets,
        runs = player.runs
    )

    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    
    return db_player
 
