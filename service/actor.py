from models.actor import Actor as ActorModel
from schemas.actor import Actor

class ActorService():

    def __init__(self,db) -> None:
        self.db = db

    def create_actor(self,actor: Actor):
        new_actor = ActorModel(
        fname = actor.fname,
        lname = actor.lname,
        gender = actor.gender
        )
        self.db.add(new_actor)
        self.db.commit()
        return