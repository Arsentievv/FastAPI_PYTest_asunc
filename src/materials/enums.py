from enum import Enum


class MaterialType(str, Enum):
    stone = "Камень"
    metal = "Метал"
    glass = "Стекло"
    other = "Прочее"