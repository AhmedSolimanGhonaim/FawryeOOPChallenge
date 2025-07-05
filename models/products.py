from datetime import datetime


class Products:
    def __init__(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f'Product: {self.name}'


class Shippable(Products):
    shipping_fee = 12 / 100

    def __init__(self, name, price, quantity, weight):
        super().__init__(name, price, quantity)
        self.weight = weight
        self.shipping_cost = Shippable.shipping_fee * self.weight
        self.total_price = self.price + self.shipping_cost

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight


class ExpireSense(Shippable):
    def __init__(self, name, price, quantity, weight, expire_date):
        super().__init__(name, price, quantity, weight)
        self.expire_date = expire_date

    def is_expired(self):
        return datetime.now() > self.expire_date


class OnlineProduct(Products):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
