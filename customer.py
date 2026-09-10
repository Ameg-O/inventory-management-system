from person import Person
class Customer(Person):
    def __init__(self,person_id,name,phone,email,username,password):
        super().__init__(person_id,name,phone,email)
        self.username=username
        self.password=password
        self.purchase_history=[]
    def display(self):
        super().display()
        print("username :",self.username)
    def login(self,username,password):
        if self.username==username and self.password==password:
            return True
        else:
            return False
    def buy_product(self, product):
        purchase = {
        "product_id": product.product_id,
        "name": product.name,
        "category": product.category,
        "price": product.price,
        "quantity": 1
    }

        self.purchase_history.append(purchase)

        print(product.name, "Purchased Successfully")
    def view_purchase_history(self):
        if len(self.purchase_history)==0:
            print("You Dont have any purchase history.")
        else:
            print("Purchase history")
            print("________________")
            for product in self.purchase_history:
                product.display()
                
    