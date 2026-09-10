from product import Product
class Grocery(Product):
    def __init__(self,product_id, name, category, price, quantity,expiry_date,weight):
        super().__init__(product_id, name, category, price, quantity)
        self.expiry_date=expiry_date
        self.weight=weight
    def display(self):
        super().display()
        print("Expiry Date : ",self.expiry_date)
        print("Weight : ",self.weight,)