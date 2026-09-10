class Order:
    def __init__(self,order_id,customer,):
        self.order_id=order_id
        self.customer=customer
        self.products=[]
        self.total_amount=0
    def add_product(self,product):
        self.products.append(product)
    def remove_product(self,product):
        self.products.remove(product)
    def calculate_total_bill(self):
        self.total_amount=0
        for product in self.products:
            self.total_amount+=product.price
    def display_order(self):
        print("-----ORDER-----")
        print("Order ID : ",self.order_id)
        print()

        print("Customer Details")
        self.customer.display()

        print("\nProducts")

        if len(self.products)==0:
            print("No Product in order")
        else:
            for product in self.products:
                product.display()
        self.calculate_total_bill()
        print("Total Amount : ",self.total_amount)