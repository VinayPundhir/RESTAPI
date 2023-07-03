from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
import user_skills_api.schema as schema
from user_skills_api.database import get_db
from user_skills_api.repository import skill

router = APIRouter(tags=["skills"])


@router.post("/create_skill")
def create_skill(new_skill:schema.Skill , db:Session = Depends(get_db)):
    return skill.create(new_skill,db)


@router.get("/skill_info_by_name/{name}", response_model=schema.ShowSkill)
def get_info_by_name(name: str, db: Session = Depends(get_db)):
    return skill.get(name,db)