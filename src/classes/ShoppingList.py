from decimal import Decimal
from typing import List, Tuple

from multipledispatch import dispatch

from src.classes import Product


class ShoppingList:
    product_list: List[Product]
    category_List = Tuple[str]

    def __init__(self):
        self.category_List = []
        self.product_list = []

    # List management
    @dispatch(Product)
    def add_product(self, product: Product):
        self.product_list.append(product)
        return

    @dispatch(str, str, int, Decimal, str)
    def add_product(self, name: str, category: str,
                    stock: int, price: Decimal,
                    notes: str
                    ):
        new_product = (
            name, category, stock, price, notes)
        self.category_List.append(category)
        self.add_product(new_product)

    def remove_product(self, product: Product):
        self.product_list.remove(product)
        return

    def edit_product(self, product: Product, name: str = '',
                     category: str = '', stock: int = 0,
                     price: Decimal = 0,
                     notes: str = ''):
        if product not in self.product_list:
            pass

        edited_product = (
            name, category, stock, price, notes)

        self.product_list.remove(product)
        self.product_list.append(edited_product)
        pass

    # todo -> write a proper comparing function
    def filter_list(self,
                    name: str = '',
                    category: str = '', stock: int = 0,
                    price: Decimal = 0,
                    notes: str = ''
                    ):

        filtered_list: List[Product] = []

        for product in self.product_list:
            if (
                    name.lower() not in
                    product.name.lower() and
                    category.lower() not in
                    product.category.lower() and
                    stock > product.stock and
                    price > product.price and
                    notes.lower() not in
                    product.notes.lower()
            ):
                filtered_list.append(product)

        return filtered_list

    def display_list(self):
        print("THIS WILL BE A PRODUCT LIST")

