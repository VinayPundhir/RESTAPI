from user_skills_api.database import Base
from sqlalchemy import Column,String,INTEGER,ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__="User"
    id = Column(INTEGER,primary_key=True,index=True)
    name=Column(String)
    age = Column(INTEGER)
    email=Column(String)
    password=Column(String)
    skills = relationship("Skill",back_populates="users")


class Skill(Base):
    __tablename__ = "Skill"
    id = Column(INTEGER, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(INTEGER, ForeignKey("User.id"))
    users = relationship("User", back_populates="skills")

