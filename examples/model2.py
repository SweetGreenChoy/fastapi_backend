from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any
from uuid import UUID, uuid4, uuid1
import datetime

app = FastAPI()

class Player(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(max_length=12)
    player_img: str | None = None
    point: int = Field(default=1000000)
    rp: int = Field(gt=-1)

class Tournament(BaseModel):
    id: UUID = Field(default_factory=uuid1)
    name: str
    description: str | None=None
    g_type: int = Field(examples=["0:speed, 1:normal, 2:deep rank"]) # 
    created: datetime.datetime
    buyin: int = Field(default=1000)
    a_score: float = Field(default=6.5)
    winner: str
    runner_up: str
    prize: int

class Register(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    p_id: str
    t_id: str

class Battle(BaseModel):
    id: UUID = Field(default_factory=uuid1)
    b_player: str
    w_player: str
    g_round: int
    winner: str
    result: str

@app.post("/players/signin/req", response_model=Player, status_code=201)
def sign_in(player: Player) -> Any:
    return player

@app.put("/players/mypage{player_name}/req", response_model=Player, status_code=200)
def p_alter(player: Player) -> Any:
    return player

#회원 탈퇴
@app.delete("/players-v1/mypage{player_name}/del-req", response_model=Player)
def p_delete(player: Player) -> Any:
    return player

#토너먼트 생성
@app.post("/tournaments-v1/{tournament_id}/cre-req", response_model=Tournament, status_code=201)
def t_create(tournament: Tournament) -> Any:
    return tournament

"""
#토너먼트 삭제
@app.delete("/tournaments-v1/{tournament_id}/del-req", status_code=200)
def t_delete():

#무료충전여부(result = 1 or 0)
@app.get("/players-point-v1/free-point-checker")
def p_checker():

#포인트 지급(player.point + n)
@app.post("/players-point-v1/free-point-fillup")
def p_fillup():
"""