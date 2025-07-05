class ShippingService:
    def ship(self, products):
        print("** Shipment notice **")
        total_weight = 0
        for product in products:
            print(f"{product.get_name()} - {product.get_weight()}kg")
            total_weight += product.get_weight()
        print(f"Total package weight: {total_weight}kg")
