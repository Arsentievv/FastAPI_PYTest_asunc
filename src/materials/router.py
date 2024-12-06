from fastapi.routing import APIRouter
from materials import schemas
from materials.crud import MaterialCRUD
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from data_base.db_connect import get_db

router = APIRouter(prefix="/materials", tags=["materials"])


@router.post(
    "/create",
    response_model=schemas.MaterialSchemaGet,
    description="Добавить материал"
)
async def create_material(
        material: schemas.MaterialSchemaCreate,
        db: AsyncSession = Depends(get_db)
):
    result = MaterialCRUD.create_material(material=material, db=db)
    return await result


@router.get(
    "/",
    response_model=list[schemas.MaterialSchemaGet],
    status_code=200,
    description="Получаем все материалы"
)
async def get_all_materials(db: AsyncSession = Depends(get_db)):
    result = MaterialCRUD.get_all_materials(db=db)
    return await result


@router.get(
    "/title/{material_title}",
    response_model=schemas.MaterialSchemaGet,
    status_code=200,
    description="Получение материала по названию"
)
async def get_material_by_title(material_title: str, db: AsyncSession = Depends(get_db)):
    result = MaterialCRUD.get_material_by_title(db=db, title=material_title)
    return await result


@router.get(
    "/id/{material_id}",
    response_model=schemas.MaterialSchemaGet,
    status_code=200,
    description="Получение материала по ID"
)
async def get_material_by_title(material_id: int, db: AsyncSession = Depends(get_db)):
    result = MaterialCRUD.get_current_material(db=db, material_id=material_id)
    return await result