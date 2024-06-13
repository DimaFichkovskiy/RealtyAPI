from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class Image(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    realty_id: int
    url: str


class Realty(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    realty_type: str
    title: str
    description: str
    price: int
    realty_id: int
    region: Optional[str] = None
    condition: Optional[str] = None
    street: Optional[str] = None
    section: Optional[str] = None
    floor: Optional[str] = None
    square: Optional[str] = None
    rooms: Optional[str] = None
    builder: Optional[str] = None
    rc: Optional[str] = None
    turn: Optional[str] = None
    entrance: Optional[str] = None
    heating: Optional[str] = None
    documents: Optional[str] = None
    material_manufacture: Optional[str] = None
    location_type: Optional[str] = None
    settlement: Optional[str] = None
    house_type: Optional[str] = None
    land_area_object: Optional[str] = None
    material_manufacture: Optional[str] = None
    material_manufacture_2: Optional[str] = None
    communications: Optional[str] = None
    appointment: Optional[str] = None
    features: Optional[str] = None
    tenants_object: Optional[str] = None
    comfort: Optional[str] = None
    seller_name: Optional[str] = None
    seller_phone_number: Optional[str] = None
    seller_photo: Optional[str] = None
    realty_images: List[Image]


class Category(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name_en: str
    name_urk: str


class Categories(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    categories: List[Category]
