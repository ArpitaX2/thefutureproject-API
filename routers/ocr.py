from fastapi import APIRouter, UploadFile
import schemas
from .OCR_Modules import image_validate, ocr
from typing import Optional


router = APIRouter(
    prefix="/ocr",
    tags=["OCR - Optical Character Recognition"]
)


@router.post("/image", status_code=200, summary="Get text from image")
async def get_text_from_image(file: UploadFile, lang: Optional[str] = "eng"):
    image_validate.validate_file_size_type(file)
    text = ocr.ocr_space_file(image_file=file, language=lang)
    return schemas.Image_Out(text=text, language=lang)


@router.post("/image/url", status_code=200, summary="Get text from image URL")
async def get_text_from_image_url(image: schemas.Image_Url_In):
    text = ocr.ocr_space_url(url=image.url, language=image.language)
    return schemas.Image_Out(text=text, language=image.language)
