from .products import ExpireSense


class Payment:
    def __init__(self, user):
        self.user = user
        self.success = False

    def checkout(self):
        if not self.user.cart.items:
            return 'Cart is empty'

        for item in self.user.cart.items:
            if isinstance(item, ExpireSense) and item.is_expired():
                return f'Cannot checkout: {item.name} is expired.'

        total = self.user.cart.get_total_price
        if self.user.balance >= total:
            self.user.balance -= total
            self.success = True
            self.user.cart.clear_cart()
            return f'Payment successful. Your balance is now: {self.user.balance}'
        return 'Balance is insufficient'
