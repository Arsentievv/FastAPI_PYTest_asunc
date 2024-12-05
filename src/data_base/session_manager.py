import contextlib

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.orm import DeclarativeBase
from config import get_settings

settings = get_settings()


class Base(DeclarativeBase):
    pass


class SessionManager:
    def __init__(self):
        self._engine: AsyncEngine | None = None
        self._session: AsyncSession | None = None

    def init(self, host):
        self._engine = create_async_engine(host)
        self._session = async_sessionmaker(autocomit=False, bind=self._engine)

    async def close(self):
        if self._engine in None:
            raise Exception("Data Base Session Manager is not initialized")

        await self._engine.dispose()
        self._engine = None
        self._session = None

    async def connect(self):
        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self):
        if self._session in None:
            raise Exception("Data Base Session Manager is not initialized")

        session = self._session
        try:
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()

    # Used for testing
    async def create_all(self, connection: AsyncConnection):
        await connection.run_sync(Base.metadata.create_all)

    async def drop_all(self, connection: AsyncConnection):
        await connection.run_sync(Base.metadata.drop_all)

