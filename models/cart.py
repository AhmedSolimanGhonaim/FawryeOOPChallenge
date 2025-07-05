from .products import ExpireSense


class Cart:
    def __init__(self):
        self.items = []

    @property
    def get_count(self):
        return len(self.items)

    @property
    def get_total_price(self):
        return sum(
            item.total_price if hasattr(item, "total_price") else item.price
            for item in self.items
        )

    def add_to_cart(self, item):
        if isinstance(item, ExpireSense) and item.is_expired():
            return f'{item.name} is expired. Cannot add to cart.'
        if item.quantity < 1:
            return 'Sorry, out of stock.'
        self.items.append(item)
        item.quantity -= 1
        return f'Added successfully. Cart now has {len(self.items)} item(s).'

    def clear_cart(self):
        self.items = []
