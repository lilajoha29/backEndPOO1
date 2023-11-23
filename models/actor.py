from sqlalchemy import Column,Integer, String

from config.database import Base


class Actor(Base):

    __tablename__ = "actor"

    id = Column(Integer,primary_key = True)
    fname = Column(String)
    lname = Column(String)
    gender = Column(String)

