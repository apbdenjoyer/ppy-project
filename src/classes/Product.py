from decimal import Decimal
from enum import Enum


class ProductStatus(Enum):
    PENDING = 'Pending'
    BOUGHT = 'Bought'


class Product:
    name: str
    category: str
    stock: int
    price: Decimal
    notes: str
    status: ProductStatus

    def __init__(self, name: str, category: str, stock: int,
                 price: Decimal, notes: str,
                 status: ProductStatus):
        self.name = name
        self.category = category
        self.stock = stock
        self.price = price
        self.notes = notes
        self.status = status
