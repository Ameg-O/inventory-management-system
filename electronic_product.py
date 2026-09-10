from product import Product

class Electronic(Product):
    def __init__(self, product_id, name, category, price, quantity, brand, warranty):
        super().__init__(product_id, name, category, price, quantity)
        self.brand = brand
        self.warranty = warranty

    def display(self):
        super().display()
        print("Brand : ", self.brand)
        print("Warranty : ", self.warranty, "Years")
