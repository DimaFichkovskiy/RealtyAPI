import os
from fastapi import APIRouter, status, File, Depends, UploadFile
from fastapi_pagination import Page, paginate

from app.crud import RealtyCRUD
from app import schemas


router = APIRouter(
    prefix="/realty",
    tags=["realty"],
    responses={404: {"description": "Not Found"}}
)


@router.get("/realties", response_model=Page[schemas.Realty], status_code=status.HTTP_200_OK)
async def get_all_realties(
    skip: int = 0,
    limit: int = 10,
    realty_crud: RealtyCRUD = Depends()
):
    realties = await realty_crud.get_all_realties(skip=skip, limit=limit)
    return paginate(realties)


@router.get("/{realty_type}", response_model=Page[schemas.Realty], status_code=status.HTTP_200_OK)
async def get_realty_by_type(
        realty_type: str,
        skip: int = 0,
        limit: int = 10,
        realty_crud: RealtyCRUD = Depends()
):
    realties = await realty_crud.get_realties_by_type(realty_type=realty_type, skip=skip, limit=limit)
    return paginate(realties)


@router.get("/{realty_id}", response_model=schemas.Realty)
async def get_realty_by_realty_id(
        realty_id: int,
        realty_crud: RealtyCRUD = Depends(),
):
    realty = await realty_crud.get_realty_by_realty_id(realty_id=realty_id)
    return realty


@router.post("/unloadfile")
async def upload_file(
        file: UploadFile = File(...),
        realty_crud: RealtyCRUD = Depends()
):
    path_to_directory_with_downloaded_files = f"{os.getcwd()}/downloaded-files/"
    with open(os.path.join(path_to_directory_with_downloaded_files, file.filename), "wb") as buffer:
        buffer.write(await file.read())
    await realty_crud.upload_file(path_to_file=f"{path_to_directory_with_downloaded_files + file.filename}")
    return 200
