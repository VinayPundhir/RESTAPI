from fastapi import FastAPI
from user_skills_api import models
from user_skills_api.database import engine
from user_skills_api.routers import skill,user,authentication,files
from user_skills_api.middlewares import AddMiddlewareUsed

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# middlewares
app.add_middleware(AddMiddlewareUsed)

# routes
app.include_router(authentication.router)
app.include_router(skill.router)
app.include_router(user.router)
app.include_router(files.router)


@app.get("/")
def index():
    return {"msg":"welcome!"}








