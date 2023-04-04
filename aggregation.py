# Aggregation is a more specialized form of association
# between two or more objects. Each object will have
# its independent lifecycle.
# it is a ussualy a one-to-many relationship, where an
# object has one or many objects.
# Objects can live separately, but it can be a
# relationship where one object needs another
# to do a certain task.
# (there are controversies about the definitions of aggregation).

class Cart:
    def __init__(self):
        self._products = []

    def total_price(self):
        return sum(p.price for p in self._products)

    def insert_products(self, *products):
        for product in products:
            self._products.append(product)

    def list_products(self):
        for product in self._products:
            print(product.name, product.price)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

cart = Cart()
product1 = Product('Pen', 1.50)
product2 = Product('Mouse', 20.99)
cart.insert_products(product1, product2)
cart.list_products()
print(cart.total_price())
