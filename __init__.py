import json
from typing import List, Optional
from products import Product, get_product
from cart import dao


class Cart:
    def __init__(self, id: int, username: str, contents: List[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> 'Cart':
        return Cart(
            id=data['id'],
            username=data['username'],
            contents=[Product.load(p) for p in data['contents']],
            cost=data['cost']
        )


def get_cart(username: str) -> List[Product]:
    """
    Retrieves the cart for a given username and returns a list of Product objects.
    """
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    products_in_cart = []
    for cart_detail in cart_details:
        try:
            # Parse contents as JSON instead of using eval
            contents = json.loads(cart_detail['contents'])
        except json.JSONDecodeError:
            continue

        # Fetch Product objects for each product ID
        for product_id in contents:
            product = get_product(product_id)
            if product:
                products_in_cart.append(product)

    return products_in_cart


def add_to_cart(username: str, product_id: int):
    """
    Adds a product to the cart for the given username.
    """
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """
    Removes a product from the cart for the given username.
    """
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """
    Deletes the entire cart for the given username.
    """
    dao.delete_cart(username)