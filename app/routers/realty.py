import os

from fastapi import APIRouter, status, File, Depends, UploadFile
from fastapi_pagination import Page, paginate

from app.crud import RealtyCRUD
from app import schemas

from fastapi_pagination.utils import disable_installed_extensions_check

disable_installed_extensions_check()

router = APIRouter(
    prefix="/realty",
    tags=["realty"],
    responses={404: {"description": "Not Found"}}
)


@router.get("/categories", response_model=schemas.Categories, status_code=status.HTTP_200_OK)
async def categories(
        realty_crud: RealtyCRUD = Depends()
):
    # all_categories = await realty_crud.get_all_categories()
    # all_categories_dict = {"categories": all_categories}
    all_categories_dict = {"categories": [
        {"name_en": "apartment", "name_urk": "Квартири"},
        {"name_en": "commercial", "name_urk": "Кормерція"},
        {"name_en": "house", "name_urk": "Приватні будинки"},
        {"name_en": "land", "name_urk": "Земельні ділянки"},
        {"name_en": "secondary", "name_urk": "Вторинка"},
        {"name_en": "town", "name_urk": "Котеджні містечка"}
    ]}
    return all_categories_dict


@router.get("/realties", response_model=Page[schemas.Realty], status_code=status.HTTP_200_OK)
async def get_all_realties(
        realty_crud: RealtyCRUD = Depends()
) -> Page[schemas.Realty]:
    realties = await realty_crud.get_all_realties()
    return paginate(realties)


@router.get("/search", response_model=Page[schemas.Realty], status_code=status.HTTP_200_OK)
async def search_by_keywords(
        query: str = "",
        realty_crud: RealtyCRUD = Depends()
):
    realties = await realty_crud.get_realties_by_keyword(query=query)
    return paginate(realties)


@router.get("/{realty_type}", response_model=Page[schemas.Realty], status_code=status.HTTP_200_OK)
async def get_realty_by_type(
        realty_type: str,
        realty_crud: RealtyCRUD = Depends()
):
    realties = await realty_crud.get_realties_by_type(realty_type=realty_type)
    return paginate(realties)


@router.get("/object/{realty_id}", response_model=schemas.Realty, status_code=status.HTTP_200_OK)
async def get_realty_by_realty_id(
        realty_id: int,
        realty_crud: RealtyCRUD = Depends(),
):
    print(realty_id)
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



