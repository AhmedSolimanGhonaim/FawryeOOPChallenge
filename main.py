from datetime import datetime, timedelta
from models.users import User
from models.products import ExpireSense, OnlineProduct, Shippable
from models.payment import Payment
from models.shipping import ShippingService

# Create user
user = User("Ahmed", 2000)

# Create products
cheese = ExpireSense("Cheese", 100, 3, 0.4, datetime.now() + timedelta(days=1))
biscuits = ExpireSense("Biscuits", 150, 2, 0.7,
                       datetime.now() + timedelta(days=5))
tv_card = OnlineProduct("TV Scratch Card", 200, 1)

# Add to cart
print(user.cart.add_to_cart(cheese))
print(user.cart.add_to_cart(biscuits))
print(user.cart.add_to_cart(tv_card))

# Show total
print(f"Subtotal: {user.cart.get_total_price}")

# Ship physical products
shippables = [item for item in user.cart.items if isinstance(item, Shippable)]
shipping_service = ShippingService()
shipping_service.ship(shippables)

# Checkout
payment = Payment(user)
print(payment.checkout())
