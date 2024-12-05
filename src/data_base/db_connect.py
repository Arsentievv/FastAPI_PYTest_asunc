from data_base.session_manager import SessionManager

session_manager = SessionManager()


async def get_db():
    async with session_manager.session() as session:
        yield session