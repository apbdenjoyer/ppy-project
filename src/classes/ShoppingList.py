import os
from decimal import Decimal
from typing import List, Set

from multipledispatch import dispatch

from src.classes.Product import Product, ProductStatus


class ShoppingList:
    list_name: str
    product_list: List[Product]
    categories = Set[str]

    def __init__(self, list_name: str):
        self.list_name = list_name
        self.categories = set()
        self.product_list = list()

        if not os.path.exists("saved_lists"):
            os.makedirs("saved_lists")

    # List management
    @dispatch(Product)
    def add_product(self, product: Product):
        self.product_list.append(product)
        return

    @dispatch(str, str, int, Decimal, str)
    def add_product(self, name: str, category: str,
                    quantity: int, price: Decimal,
                    notes: str
                    ):
        new_product = Product(
            name, category, quantity, price, notes, ProductStatus.PENDING
            )
        self.categories.add(category)
        self.add_product(new_product)

    def remove_product(self, product: Product):
        self.product_list.remove(product)
        return

    def edit_product(self, product: Product, name: str = '',
                     category: str = '', quantity: int = 0,
                     price: Decimal = 0, notes: str = '',
                     status: ProductStatus = ProductStatus.PENDING):
        if product not in self.product_list:
            pass

        edited_product = Product(
            name, category, quantity, price, notes, status
            )

        self.product_list.remove(product)
        self.product_list.append(edited_product)
        pass

    # todo -> write a proper comparing function
    def filter_list(self,
                    name: str = '',
                    category: str = '', quantity: int = 0,
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
                    quantity > product.quantity and
                    price > product.price and
                    notes.lower() not in
                    product.notes.lower()
            ):
                filtered_list.append(product)

        return filtered_list

    def display_list(self):
        print("THIS WILL BE A PRODUCT LIST")

    def save_list(self):
        filename = os.path.join("saved_lists", self.list_name + ".txt")
        with open(filename, 'w+') as f:
            f.write("--LIST START--\n")
            f.write(f"{self.list_name}\n")
            for product in self.product_list:
                f.write("--PRODUCT START--\n")
                f.write(f"name:{product.name}\n")
                f.write(f"category:{product.category}\n")
                f.write(f"quantity:{product.quantity}\n")
                f.write(f"price:{product.price}\n")
                f.write(f"notes:{product.notes}\n")
                f.write(f"status:{product.status}\n")
                f.write("--PRODUCT END--\n")
            f.write("--LIST END--\n")
            f.close()

    def load_list(self, file: str):
        filepath = os.path.join("saved_lists", file + ".txt")
        with open(filepath, 'r+') as f:
            for line in f:
                if line.startswith("--LIST END--"):
                    return
                if line.startswith("--LIST START--"):
                    # get list name
                    self.list_name = next(f)
                    self.product_list = []
                    self.categories = []
                elif line.startswith("--PRODUCT START--"):
                    name = next(f).strip()[5:]
                    category = next(f).strip()[9:]
                    quantity = int(next(f).strip()[9:])
                    price = Decimal(next(f).strip()[6:])
                    notes = next(f).strip()[6:]

                    status = ProductStatus[next(f).strip()[7:]]
                    read_product = Product(name, category, quantity, price, notes, status)
                    self.product_list.append(read_product)
