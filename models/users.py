from .cart import Cart


class User:
    def __init__(self, name, balance: float):
        self.balance = balance
        self.name = name
        self.cart = Cart()

    def __str__(self):
        return f'User: {self.name}, Balance: {self.balance}'
