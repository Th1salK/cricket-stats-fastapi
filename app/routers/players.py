from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db
from app.models import Player
from app.schemas import PlayerCreate, PlayerResponse

router = APIRouter(prefix="/players", tags=["players"])


@router.post("/", response_model=PlayerResponse)
def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    db_player = Player(
        name=player.name,
        team=player.team,
        matches=player.matches,
        wickets=player.wickets,
        runs=player.runs,
    )

    db.add(db_player)
    db.commit()
    db.refresh(db_player)

    return db_player


@router.get("/", response_model=list[PlayerResponse])
def get_all_players(db: Session = Depends(get_db)):

    players = db.scalars(select(Player)).all()

    return players


@router.put("/{player_id}", response_model=PlayerResponse)
def update_player(player_id: int, player: PlayerCreate, db: Session = Depends(get_db)):

    db_player = db.get(Player, player_id)

    if not db_player:
        raise HTTPException(
            status_code=404, detail=f"Player with id {player_id} does not exist."
        )

    db_player.name = player.name
    db_player.team = player.team
    db_player.matches = player.matches
    db_player.wickets = player.wickets
    db_player.runs = player.runs

    db.commit()
    db.refresh(db_player)

    return db_player
