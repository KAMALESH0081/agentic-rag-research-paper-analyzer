import os
from fastapi import APIRouter, UploadFile, File
from app.services.pipeline import run_pipeline
from app.models.schema import ExtractionResult

router = APIRouter()

UPLOAD_DIR = "data/papers"

@router.post("/analyze", response_model=ExtractionResult)
async def analyze_paper(file: UploadFile = File(...)):

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = run_pipeline(file_path)

    return result

