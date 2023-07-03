from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from user_skills_api import models
import user_skills_api.schema as schema
from user_skills_api.database import get_db
from user_skills_api.repository import user
from user_skills_api.oauth2 import get_current_user

router = APIRouter(tags=["users"])


@router.get("/user_info/{id}", response_model=schema.ShowUser)
def get_info_by_id(id: int, db: Session = Depends(get_db)):
    return user.get(id,db)


@router.delete("/delete_usr/{id}")
def del_info(id:int,db:Session=Depends(get_db)):
    return user.delete(id,db)


@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_info(id:int,usr:schema.UpdateUsr, db:Session=Depends(get_db)):
    return user.delete(id,usr,db)


@router.get("/all_usrs", response_model=list[schema.ShowUser])
def get_all_users_info(db:Session=Depends(get_db),auth:models.User=Depends(get_current_user)):
    return db.query(models.User).all()


@router.post("/create_usr")
def create_usr_info(new_usr:schema.User , db:Session = Depends(get_db)):
    return user.create(new_usr,db)
