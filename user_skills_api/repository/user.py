from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from user_skills_api import models
import user_skills_api.schema as schema
import user_skills_api.hashing as hashing


def get(id:int,db:Session):
    usr = db.query(models.User).filter(models.User.id == id).first()
    if not usr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="usr does not exist")
    return usr


def delete(id:int,db:Session):
    usr = db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    if not usr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="usr does not exist")
    return usr


def update(id:int,usr:schema.User,db:Session):
    usr_obj = db.query(models.User).filter(models.User.id == id)
    if not usr_obj.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="usr does not exist")
    usr_obj.update({models.User.name: usr.name}, synchronize_session=False)
    db.commit()
    return usr


def create(new_usr:schema.User,db:Session):
    usr = models.User(id=new_usr.id, name=new_usr.name, age=new_usr.age, email=new_usr.email,
                      password=hashing.Hash.bcrypt(new_usr.password))
    db.add(usr)
    db.commit()
    db.refresh(usr)
    return new_usr
