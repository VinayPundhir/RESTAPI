from fastapi.requests import Request
from fastapi import UploadFile,APIRouter
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='user_skills_api/templates')
router = APIRouter(tags=["files"])

FILES_DIR = "user_skills_api/uploaded_files"


@router.get("/upload")
def upload_file(request:Request):
    return templates.TemplateResponse(name="fileupload.html",context={"request":request})


@router.post("/save_file")
async def save_file(file:UploadFile):
    with open(f"{FILES_DIR}/{file.filename}",'wb') as f:
        f.write(await file.read())
        return {"msg": f"saved file {file.filename}"}