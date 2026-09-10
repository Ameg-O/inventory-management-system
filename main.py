from admin import Admin
from customer import Customer
from electronic_product import Electronic
from grocery_product import Grocery
from inventory import Inventory
from order import Order
from product import Product
import json

def save_products(inventory):
    data=[]
    for product in inventory.products:
        if isinstance(product,Electronic):
            data.append({
                "type": "electronic",
                "product_id": product.product_id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "quantity": product.quantity,
                "brand": product.brand,
                "warranty": product.warranty,
                
            })
        elif isinstance(product,Grocery):
            data.append({
                "type": "grocery",
                "product_id": product.product_id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "quantity": product.quantity,
                "expiry_date": product.expiry_date,
                "weight": product.weight

            })
        else:
            data.append({
                "type": "product",
                "product_id": product.product_id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "quantity": product.quantity
            })
    with open("products.json","w") as file:
        json.dump(data,file,indent=4)
def load_products(inventory):
    try:
        with open("products.json","r") as file:
            data=json.load(file)
        for item in data:
            if item["type"]=="electronic":
                product=Electronic(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"],
                    item["brand"],
                    item["warranty"]
                )
            elif item["type"]=="grocery":
                product=Grocery(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"],
                    item["expiry_date"],
                    item["weight"]
                )
            else:
                product=Product(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"]
            )
            inventory.products.append(product)
    except FileNotFoundError:
        pass
def save_customers(customers):
    data=[]
    for customer in customers:
        data.append({
            "person_id": customer.person_id,
            "name": customer.name,
            "phone": customer.phone,
            "email": customer.email,
            "username": customer.username,
            "password": customer.password
        })
    with open("customers.json","w") as file:
        json.dump(data,file,indent=4)

def load_customers(customers):
    try:
        with open("customers.json","r") as file:
            data=json.load(file)
        for item in data:
            customer=Customer(
                item["person_id"],
                item["name"],
                item["phone"],
                item["email"],
                item["username"],
                item["password"]
            )
            customers.append(customer)
    except FileNotFoundError:
        pass



    

inventory=Inventory()
load_products(inventory)
customers=[]
load_customers(customers)
orders=[]

admin=Admin(1,"Ameg","1234567890","Ameg123@gmail.com","admin","12345")


while True:

   print("\n ___________________________")
   print("  INVENTORY MANAGEMENT SYSTEM  ")
   print("1. Admin Login")
   print("2. Customer Register")
   print("3. Customer Login")
   print("4. Exit")

   try:
       choice=int(input("Enter Choice : "))
   except ValueError:
       print("Please Enter a number")
       continue

   if choice==1:
       username=input("Enter Admin Username :")
       password=input("Enter Admin Password :")
       if admin.login(username,password):
           print("Admin login Successful")

           while True:

               print("\n ________ADMIN MENU________")
               print("1. Add Product")
               print("2. Display Products")
               print("3. Search Product")
               print("4. Update Product")
               print("5. Remove Product")
               print("6. Low Stock Products")
               print("7. Total Products")
               print("8. Inventory value")
               print("9. Exit")



               try:
                   admin_choice=int(input("Enter Choice: "))
               except ValueError:
                   print("please enter a number")
                   continue

               if admin_choice==1:
                   print("\n1. Normal Product")
                   print("2. Electronic Product")
                   print("3. Grocery Product")
                   try:
                        option=int(input("Enter Product Type : "))
                   except ValueError:
                       print("Product must be a number")
                       continue
                
                   
                   product_id=int(input("Enter Product ID : "))

                   product_exist=False

                   for product in inventory.products:
                       if product.product_id==product_id:
                           product_exist=True
                           break
                   if product_exist:
                       print("Product ID already Exist")
                       continue
                   name=input("Enter Product Name : ")
                   category=input("Enter Category : ")
                   try:
                      price=float(input("Enter Product Price : "))
                   except ValueError:
                       print("Price must be a number.") 
                       continue
                   try:
                       quantity=int(input("Enter Product Quantity : "))
                       if quantity<0:
                           print("Quantity cannot be negative")
                           continue
                   except ValueError:
                       print("Quantity Must be a number")
                       continue
                   
                   if option==1:
                           product=Product(product_id,name,category,price,quantity)
                   elif option==2:
                       brand=input("Enter Brand : ")
                       try:
                            warranty=int(input("Enter Warrant (Years) : "))
                       except ValueError:
                           print("Warranty must be a number")
                           continue
                       product=Electronic(product_id,name,category,price,quantity,brand,warranty)
                   elif option==3:
                       expiry_date=input("Enter Expiry Date : ")
                       try:
                            weight=float(input("Enter Weight : "))
                       except ValueError:
                           print("weight must be number")
                           continue
                       product=Grocery(product_id,name,category,price,quantity,expiry_date,weight)
                   else:
                       print("Invalid choice")
                       continue
                   inventory.add_product(product)
                   save_products(inventory)
               elif admin_choice==2:
                   print("\n--PRODUCT LIST--")
                   print("____________________________")
                   inventory.display_products()
                   
               elif admin_choice==3:
                   try:
                      product_id=int(input("Enter Product ID :"))
                   except ValueError:
                       print("Please enter a number")
                       continue
                   inventory.search_product(product_id)
                   
               elif admin_choice==4:
                   inventory.update_product()
                   save_products(inventory)
                   
               elif admin_choice==5:
                   try:
                        product_id=int(input("Enter Product ID : "))
                   except ValueError:
                       print("Product ID must be a number")
                       continue
                   inventory.remove_product(product_id)
                   save_products(inventory)
                   
               elif admin_choice==6:
                   print("\n-- LOW STOCK PRODUCTS --")
                   print("________________________________")
                   inventory.low_stock_product()
               elif admin_choice==7:
                   inventory.total_products()
               elif admin_choice==8:
                   inventory.inventory_value()
               elif admin_choice==9:
                   print("Admin Logged Out")
                   break

   elif choice==2:
       person_id=len(customers)+1

       name=input("Enter Customer Name : ")
       phone=input("Enter phone Number: ")
       email=input("Enter Email: ")
       username=input("Enter Username:")
       password=input("Enter Password:")

       username_exist=False

       for customer in customers:
           if customer.username==username:
               username_exist=True
               break
       if username_exist:
           print("username already exists")
       else:
           customer=Customer(person_id,name,phone,email,username,password)
           customers.append(customer)
           save_customers(customers)
           print("Customer Registration Successful")
   elif choice==3:

       username=input("Enter Customer Username: ")
       password=input("Enter Customer Password: ")

       logged_customer=None
       for customer in customers:
           if customer.login(username,password):
               logged_customer=customer
               break
       if logged_customer is None:
           print("Invalid Username or Password")
       else:
           print("Customer Login succesful")

           while True:

                print("\n ______ CUSTOMER MENU______")
                print("1. Display Products")
                print("2. Buy Product")
                print("3. View Purchase History")
                print("4. Logout")
                try:
                    customer_choice=int(input("Enter Choice: "))
                except ValueError:
                    print("Please enter a number")
                    continue

                if customer_choice==1:
                    inventory.display_products()
                elif customer_choice==2:
                     try:
                        product_id=int(input("Enter Product Id: "))
                     except ValueError:
                         print("Product ID must be a number")
                         continue

                     selected_product=None
                     for product in inventory.products:
                         if product.product_id==product_id:
                            selected_product=product
                            break
                     if selected_product is None:
                        print("Product Not Found")
                     elif selected_product.quantity<=0:
                           print("Product Out of Stock")
                     else:
                        order_id=len(orders)+1

                        order=Order(order_id,logged_customer)
                        order.add_product(selected_product)
                        logged_customer.buy_product(selected_product)
                        selected_product.remove_stock(1)
                        save_products(inventory)
                        orders.append(order)
                        print("Order created Successfully")
                        order.display_order()
                elif customer_choice==3:
                    logged_customer.view_purchase_history()
                elif customer_choice==4:
                    print("Customer Logged Out")
                    break   
   elif choice==4:
       print("Thank You")
       break
       

    
    
    
       
                   


           

 