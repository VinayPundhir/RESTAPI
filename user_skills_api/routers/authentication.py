from fastapi import APIRouter,Depends,HTTPException,status
from user_skills_api import schema,database,models,hashing,token
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

router = APIRouter(tags=['Authentication'])


@router.post("/login")
def login(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    usr = db.query(models.User).filter(models.User.email==data.username).first()
    if not usr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="usr does not exist")
    if not hashing.Hash.verify(usr.password,data.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    access_token_expires = timedelta(minutes=token.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": usr.name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}