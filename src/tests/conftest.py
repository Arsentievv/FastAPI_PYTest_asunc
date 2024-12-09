import asyncio
from contextlib import ExitStack

import pytest
from fastapi.testclient import TestClient
from pytest_postgresql import factories
from pytest_postgresql.janitor import DatabaseJanitor
from sqlalchemy.testing.entities import ComparableEntity


from src.main import init_app
from src.materials.models import Material
from src.data_base.db_connect import get_db, session_manager


@pytest.fixture(autouse=True)
def app():
    with ExitStack:
        yield init_app(init_db=False)


@pytest.fixture
def client(app):
    with TestClient(app) as c:
        yield c


test_db = factories.postgresql_proc(port=None, dbname="test_db")


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def connection_test(test_db, event_loop):
    pg_host = "localhost"
    pg_port = "5431"
    pg_user = "postgres"
    pg_db = "postgres_test"
    pg_password = "postgres"

    with DatabaseJanitor(
            user=pg_user, host=pg_host, port=pg_port, dbname=pg_db,
            version=test_db.version, password=pg_password
    ):
        connection_str = f"postgresql+psycopg://{pg_user}:@{pg_host}:{pg_port}/{pg_db}"
        session_manager.init(connection_str)
        yield
        await session_manager.close()


@pytest.fixture(scope="function", autouse=True)
async def create_tables(connection_test):
    async with session_manager.connect() as connection:
        await session_manager.drop_all(connection)
        await session_manager.create_all(connection)


@pytest.fixture(scope="function", autouse=True)
async def session_override(app, connection_test):
    async def get_db_override():
        async with session_manager.session() as session:
            yield session

    app.dependency_overrides[get_db] = get_db_override

