from decimal import Decimal
from enum import Enum


class ProductStatus(Enum):
    PENDING = 'Pending'
    BOUGHT = 'Bought'

    def __str__(self):
        return self.name


class Product:
    name: str
    category: str
    quantity: int
    price: Decimal
    notes: str
    status: ProductStatus


    def __init__(self, name: str, category: str, quantity: int,
                 price: Decimal, notes: str,
                 status: ProductStatus):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.notes = notes
        self.status = status
