from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.data_base.session_manager import SessionManager
from src.config import get_settings

settings = get_settings(db_only=True)

session_manager = SessionManager()


async def get_db():
    async with session_manager.session() as session:
        yield session
