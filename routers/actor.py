from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session
from models.actor import Actor as ActorModel
from service.actor import ActorService
from schemas.actor import Actor


actor_router = APIRouter()

@actor_router.post('/actor', tags=['actor'],starus_code=201,response_model=dict)
def create_actor(actor:Actor)->dict:
    db = Session()
    ActorService(db).create_actor(actor)
    return JSONResponse(content={"message": "se ha agregado un actor", "starus_code": 201})
