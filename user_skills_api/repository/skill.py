from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from user_skills_api import models
import user_skills_api.schema as schema


def create(new_skill:schema.Skill,db:Session):
    skill = models.Skill(id=new_skill.id, name=new_skill.name, user_id=new_skill.user_id)
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill


def get(name:str,db:Session):
    skill = db.query(models.Skill).filter(models.Skill.name == name).first()
    if not skill:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="skill does not exist")
    return skill