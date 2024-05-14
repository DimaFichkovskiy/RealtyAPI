from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app import Base


class Realty(Base):
    __tablename__ = "realties"

    id = Column(Integer, primary_key=True)
    realty_type = Column(String, default=None)
    title = Column(String, default=None)
    description = Column(String, default=None)
    price = Column(Integer, default=None)
    realty_id = Column(Integer, default=None)
    region = Column(String, default=None)
    condition = Column(String, default=None)
    street = Column(String, default=None)
    section = Column(String, default=None)
    floor = Column(String, default=None)
    square = Column(String, default=None)
    rooms = Column(String, default=None)
    builder = Column(String, default=None)
    rc = Column(String, default=None)
    turn = Column(String, default=None)
    entrance = Column(String, default=None)
    heating = Column(String, default=None)
    documents = Column(String, default=None)
    material_manufacture = Column(String, default=None)
    location_type = Column(String, default=None)
    settlement = Column(String, default=None)
    house_type = Column(String, default=None)
    land_area_object = Column(String, default=None)
    material_manufacture = Column(String, default=None)
    material_manufacture_2 = Column(String, default=None)
    communications = Column(String, default=None)
    appointment = Column(String, default=None)
    features = Column(String, default=None)
    tenants_object = Column(String, default=None)
    comfort = Column(String, default=None)

    seller_name = Column(String, default=None)
    seller_phone_number = Column(String, default=None)
    seller_photo = Column(String, default=None)

    realty_images = relationship("RealtyImage", back_populates="realty", lazy='selectin')


class RealtyImage(Base):
    __tablename__ = "realty_images"

    id = Column(Integer, primary_key=True)
    realty_id = Column(Integer, ForeignKey("realties.id"))
    url = Column(String, default=None)

    realty = relationship("Realty", back_populates="realty_images", lazy='selectin')
