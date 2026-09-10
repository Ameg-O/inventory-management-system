
class Product:
    def __init__(self,product_id,name,category,price,quantity):
        self.product_id=product_id
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity
    def display(self):
        print("Product ID : ",self.product_id)
        print("Product Name : ",self.name)
        print("Product Category : ",self.category)
        print("Product Price : ",self.price)
        print("Product Quantity : ",self.quantity)
    def increase_price(self,amount):
        if amount>0:
            self.price+=amount
        else:
            print("Price must be greater than 0")
    def decrease_price(self,amount):
        if amount<=0:
            print("Amount must be greater than 0")
        elif amount<=self.price:
            self.price-=amount
        else:
            print("price cannot become negative")
    def add_stock(self,stock):
        if stock>0:
            self.quantity+=stock
            print("Stock added succesfully")
        else:
            print("stock must be positive")
    def remove_stock(self,stock):
        if stock<=0:
            print("Stock must be greater than 0")
        elif stock<=self.quantity:
            self.quantity-=stock
            print("Stock removed succesfully")
        else:
            print("Not enough stock")




