class Inventory:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        self.products.append(product)
        print("Product Added Successfully")
    def remove_product(self,product_id):
        for product in self.products:
            if product.product_id==product_id:
                self.products.remove(product)
                print("Product removed Successfully")
                return
        print("Product Not Found")
    def search_product(self,product_id):
        for product in self.products:
            if product.product_id==product_id:
                print("Found the product")
                product.display()
                return
        print("The item is not available!")
    def display_products(self):
        if len(self.products)==0:
            print("No Product Available")
        else:
            for product in self.products:
                product.display()
                print()
    def update_product(self):
        try:
            product_id=int(input("Enter product ID : "))
        except ValueError:
            print("Product ID must be a number")
            return
        for product in self.products:
            if product.product_id==product_id:
                print("\n1. Change Name")
                print("2. Change Category")
                print("3. Increase Price")
                print("4. Decrease Price")
                print("5. Add Stock")
                print("6. Remove Stock")

                try:
                    choice=int(input("Enter a choice : "))
                except ValueError:
                    print("Choice must be a number")
                    return
                
                if choice==1:
                    product.name=input("Enter New Name : ")

                elif choice==2:
                    product.category=input("Enter New Category")

                elif choice==3:
                    try:
                        amount=float(input("Enter Amount To Be Increased : "))
                        product.increase_price(amount)
                    except ValueError:
                        print("Amount must be a number")
                        return

                elif choice==4:
                    try:
                        amount=float(input("Enter The Amount To Be Decreased : "))
                        product.decrease_price(amount)
                    except ValueError:
                        print("Amount must be a number")
                        return
                elif choice==5:
                    try:
                        stock=int(input("Enter Stock To Be Added : "))
                        product.add_stock(stock)
                    except ValueError:
                        print("stock must be a number ")
                        return
                elif choice==6:
                    try:
                        stock=int(input("Enter Stock To Be Removed : "))
                        product.remove_stock(stock)
                    except ValueError:
                        print("stock must a number")
                        return
                else:
                    print("Invalid Choice!")
                    return
                print("\nProduct Updated Successfully")
                product.display()
                return
        print("Product Not Found!")
    def low_stock_product(self):
        found=False
        for product in self.products:
            if product.quantity <=5:
                product.display()
                found=True
        if not found:
                print("No Low Stock Product")
    def total_products(self):
        print("Total Products : ",len(self.products))
    def inventory_value(self):
        total=0
        for product in self.products:
            total+=product.price*product.quantity
        print("Total Inventory Value : ",total)
    