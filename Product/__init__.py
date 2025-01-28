from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data: dict) -> 'Product':
        """
        Creates a Product instance from a dictionary.
        """
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data['qty']
        )


def list_products() -> list[Product]:
    """
    Retrieves a list of products from the database and returns them as Product instances.
    """
    return [Product.load(product) for product in dao.list_products()]


def get_product(product_id: int) -> Product:
    """
    Fetches a single product by its ID and returns it as a Product instance.
    """
    product_data = dao.get_product(product_id)
    if not product_data:
        return None  # Return None if the product does not exist
    return Product.load(product_data)


def add_product(product: dict):
    """
    Adds a new product to the database.
    """
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """
    Updates the quantity of a product. Raises a ValueError if quantity is negative.
    """
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
