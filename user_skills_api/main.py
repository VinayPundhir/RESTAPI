from fastapi import FastAPI,Depends
from user_skills_api import models
from user_skills_api.database import engine
from user_skills_api.oauth2 import get_current_user
from user_skills_api.routers import skill,user,authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(skill.router)
app.include_router(user.router)


@app.get("/")
def index(auth:models.User=Depends(get_current_user)):
    return {"msg":"welcome"}






