from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core import settings


engine = create_async_engine(settings.POSTGRES_URL)
SessionLocal = sessionmaker(
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    bind=engine)

Base = declarative_base()


async def get_db_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
