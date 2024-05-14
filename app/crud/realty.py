import ast
import pandas as pd

from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy import select

from app.db import AsyncSession, get_db_session
from app import models


class RealtyCRUD:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db: AsyncSession = db

    async def get_all_realties(self, skip: int = 0, limit: int = 10) -> List[models.Realty]:
        result = await self.db.execute(select(models.Realty).offset(skip).limit(limit))
        result = result.scalars().all()
        # pprint.pprint(dict(result[0]))
        return result

    async def get_realty_by_realty_id(self, realty_id: int) -> models.Realty:
        result = await self.db.execute(select(models.Realty).filter(models.Realty.realty_id == realty_id))
        result = result.scalars().first()

        if result is None:
            raise HTTPException(status_code=404, detail="Not Found")

        return result

    async def get_realties_by_type(
            self,
            realty_type: str,
            skip: int = 0,
            limit: int = 10
    ) -> List[models.Realty]:
        result = await self.db.execute(select(models.Realty).filter(
            models.Realty.realty_type == realty_type
        ).offset(skip).limit(limit))
        result = result.scalars().all()

        if result is None:
            raise HTTPException(status_code=404, detail="Not Found")

        return result

    async def add_realty_images(self, realty: models.Realty, images: list):
        for img in images:
            image = models.RealtyImage(
                realty=realty,
                url=img
            )
            self.db.add(image)
            await self.db.commit()
            await self.db.refresh(image)

    async def create_realty(self, realty_data: dict, realty_images: list):
        realty = models.Realty(**realty_data)

        self.db.add(realty)
        await self.db.commit()
        await self.db.refresh(realty)

        await self.add_realty_images(realty=realty, images=realty_images)

    async def upload_file(self, path_to_file: str):
        exel_data = pd.read_excel(path_to_file)
        realty_data = {}
        for index, row in exel_data.iterrows():
            row_dict = {column_name: value for column_name, value in row.items() if not pd.isna(value)}

            realty_data.update(row_dict)
            seller_data = ast.literal_eval(realty_data.pop("seller_data"))

            realty_id = realty_data.pop("id")
            realty_data.update({"realty_id": realty_id})
            realty_data.update({"seller_name": seller_data["name"]})
            realty_data.update({"seller_phone_number": seller_data["contacts"][0]})
            realty_data.update({"seller_photo": seller_data["image"]})

            realty_images = ast.literal_eval(realty_data.pop("images"))

            await self.create_realty(realty_data=realty_data, realty_images=realty_images)

        return 200
