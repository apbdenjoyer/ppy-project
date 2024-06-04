from decimal import Decimal

from src.classes.Product import Product, ProductStatus
from src.classes.ShoppingList import ShoppingList


def main():
    shopping_list = ShoppingList("Shopping List")
    for i in range(1, 5):
        product = Product(f"Product {i}", f"Category {i}", 1 + i, Decimal(3.50 + i),
                    f"Note {i}", ProductStatus.PENDING)
        shopping_list.add_product(product)
    shopping_list.save_list()

    shopping_list2 = ShoppingList("")
    shopping_list2.load_list("Shopping List")

    for prod in shopping_list.product_list:
        print(prod.name, prod.category, prod.price, prod.notes, prod.status)

    print('=')
    for prod in shopping_list2.product_list:
        print(prod.name, prod.category, prod.price, prod.notes,prod.status)


if __name__ == '__main__':
    main()
