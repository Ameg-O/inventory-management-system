import streamlit as st
import json

from admin import Admin
from customer import Customer
from electronic_product import Electronic
from grocery_product import Grocery
from inventory import Inventory
from order import Order
from product import Product


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Inventory Management System",
    page_icon="📦",
    layout="wide"
)


# =========================================================
# PRODUCT JSON FUNCTIONS
# =========================================================

def save_products(inventory):

    data = []

    for product in inventory.products:

        if isinstance(product, Electronic):

            data.append({
                "type": "electronic",
                "product_id": product.product_id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "quantity": product.quantity,
                "brand": product.brand,
                "warranty": product.warranty
            })

        elif isinstance(product, Grocery):

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

    with open("products.json", "w") as file:
        json.dump(data, file, indent=4)


def load_products(inventory):

    try:

        with open("products.json", "r") as file:
            data = json.load(file)

        for item in data:

            if item["type"] == "electronic":

                product = Electronic(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"],
                    item["brand"],
                    item["warranty"]
                )

            elif item["type"] == "grocery":

                product = Grocery(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"],
                    item["expiry_date"],
                    item["weight"]
                )

            else:

                product = Product(
                    item["product_id"],
                    item["name"],
                    item["category"],
                    item["price"],
                    item["quantity"]
                )

            # Do not use add_product() here
            # because it prints "Product Added Successfully"
            inventory.products.append(product)

    except FileNotFoundError:
        pass


# =========================================================
# CUSTOMER JSON FUNCTIONS
# =========================================================

def save_customers(customers):

    data = []

    for customer in customers:

        data.append({
            "person_id": customer.person_id,
            "name": customer.name,
            "phone": customer.phone,
            "email": customer.email,
            "username": customer.username,
            "password": customer.password
        })

    with open("customers.json", "w") as file:
        json.dump(data, file, indent=4)


def load_customers(customers):

    try:

        with open("customers.json", "r") as file:
            data = json.load(file)

        for item in data:

            customer = Customer(
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


# =========================================================
# DISPLAY PRODUCT
# =========================================================

def display_product(product):

    st.subheader(product.name)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("**Product ID**")
        st.write(product.product_id)

    with col2:
        st.write("**Category**")
        st.write(product.category)

    with col3:
        st.write("**Price**")
        st.write(f"₹{product.price:.2f}")

    with col4:
        st.write("**Quantity**")
        st.write(product.quantity)

    if isinstance(product, Electronic):

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Brand:**", product.brand)

        with col2:
            st.write("**Warranty:**", product.warranty, "Years")

    elif isinstance(product, Grocery):

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Expiry Date:**", product.expiry_date)

        with col2:
            st.write("**Weight:**", product.weight)

    st.divider()


# =========================================================
# LOAD DATA ONLY ONCE
# =========================================================

if "inventory" not in st.session_state:

    st.session_state.inventory = Inventory()
    load_products(st.session_state.inventory)


if "customers" not in st.session_state:

    st.session_state.customers = []
    load_customers(st.session_state.customers)


if "orders" not in st.session_state:

    st.session_state.orders = []


if "admin_logged_in" not in st.session_state:

    st.session_state.admin_logged_in = False


if "logged_customer" not in st.session_state:

    st.session_state.logged_customer = None


inventory = st.session_state.inventory
customers = st.session_state.customers
orders = st.session_state.orders


# =========================================================
# ADMIN
# =========================================================

admin = Admin(
    1,
    "Ameg",
    "1234567890",
    "Ameg123@gmail.com",
    "admin",
    "12345"
)


# =========================================================
# TITLE
# =========================================================

st.title("📦 Inventory Management System")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Menu")


if st.session_state.admin_logged_in:

    menu = st.sidebar.selectbox(
        "Admin Menu",
        [
            "Dashboard",
            "Add Product",
            "Display Products",
            "Search Product",
            "Update Product",
            "Remove Product",
            "Low Stock Products",
            "Logout"
        ]
    )

elif st.session_state.logged_customer is not None:

    menu = st.sidebar.selectbox(
        "Customer Menu",
        [
            "Display Products",
            "Buy Product",
            "Purchase History",
            "View Orders",
            "Logout"
        ]
    )

else:

    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Home",
            "Admin Login",
            "Customer Register",
            "Customer Login"
        ]
    )


# =========================================================
# HOME
# =========================================================

if menu == "Home":

    st.header("Welcome!")

    st.write(
        "This is an Inventory Management System "
        "built using Python OOP, JSON and Streamlit."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Products", len(inventory.products))

    with col2:
        st.metric("Customers", len(customers))

    with col3:
        total_value = 0

        for product in inventory.products:
            total_value += product.price * product.quantity

        st.metric("Inventory Value", f"₹{total_value:.2f}")


# =========================================================
# ADMIN LOGIN
# =========================================================

elif menu == "Admin Login":

    st.header("🔐 Admin Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", type="primary"):

        if username == admin.username and password == admin.password:

            st.session_state.admin_logged_in = True

            st.success("Admin Login Successful")

            st.rerun()

        else:

            st.error("Invalid Username or Password")


# =========================================================
# ADMIN DASHBOARD
# =========================================================

elif menu == "Dashboard":

    st.header("📊 Admin Dashboard")

    total_value = 0

    for product in inventory.products:
        total_value += product.price * product.quantity

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Products",
            len(inventory.products)
        )

    with col2:
        st.metric(
            "Customers",
            len(customers)
        )

    with col3:
        st.metric(
            "Inventory Value",
            f"₹{total_value:.2f}"
        )


# =========================================================
# ADD PRODUCT
# =========================================================

elif menu == "Add Product":

    st.header("➕ Add Product")

    product_type = st.selectbox(
        "Product Type",
        [
            "Normal Product",
            "Electronic Product",
            "Grocery Product"
        ]
    )

    product_id = st.number_input(
        "Product ID",
        min_value=1,
        step=1
    )

    name = st.text_input("Product Name")

    category = st.text_input("Category")

    price = st.number_input(
        "Price",
        min_value=0.0,
        step=1.0
    )

    quantity = st.number_input(
        "Quantity",
        min_value=0,
        step=1
    )

    brand = ""
    warranty = 0
    expiry_date = ""
    weight = 0.0

    if product_type == "Electronic Product":

        brand = st.text_input("Brand")

        warranty = st.number_input(
            "Warranty (Years)",
            min_value=0,
            step=1
        )

    elif product_type == "Grocery Product":

        expiry_date = st.text_input(
            "Expiry Date"
        )

        weight = st.number_input(
            "Weight",
            min_value=0.0,
            step=0.5
        )

    if st.button("Add Product", type="primary"):

        # Check duplicate Product ID

        product_exists = False

        for product in inventory.products:

            if product.product_id == product_id:
                product_exists = True
                break

        if product_exists:

            st.error("Product ID already exists.")

        elif name.strip() == "":

            st.error("Product name cannot be empty.")

        elif category.strip() == "":

            st.error("Category cannot be empty.")

        else:

            if product_type == "Normal Product":

                product = Product(
                    product_id,
                    name,
                    category,
                    price,
                    quantity
                )

            elif product_type == "Electronic Product":

                product = Electronic(
                    product_id,
                    name,
                    category,
                    price,
                    quantity,
                    brand,
                    warranty
                )

            else:

                product = Grocery(
                    product_id,
                    name,
                    category,
                    price,
                    quantity,
                    expiry_date,
                    weight
                )

            inventory.products.append(product)

            save_products(inventory)

            st.success(
                f"{name} added successfully!"
            )


# =========================================================
# DISPLAY PRODUCTS
# =========================================================

elif menu == "Display Products":

    st.header("📦 Products")

    if len(inventory.products) == 0:

        st.info("No products available.")

    else:

        for product in inventory.products:

            display_product(product)


# =========================================================
# SEARCH PRODUCT
# =========================================================

elif menu == "Search Product":

    st.header("🔍 Search Product")

    product_id = st.number_input(
        "Enter Product ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        found = None

        for product in inventory.products:

            if product.product_id == product_id:

                found = product
                break

        if found:

            st.success("Product Found")

            display_product(found)

        else:

            st.error("Product Not Found")


# =========================================================
# UPDATE PRODUCT
# =========================================================

elif menu == "Update Product":

    st.header("✏️ Update Product")

    product_id = st.number_input(
        "Product ID",
        min_value=1,
        step=1
    )

    selected_product = None

    for product in inventory.products:

        if product.product_id == product_id:

            selected_product = product
            break

    if selected_product is not None:

        update_choice = st.selectbox(
            "What do you want to update?",
            [
                "Change Name",
                "Change Category",
                "Increase Price",
                "Decrease Price",
                "Add Stock",
                "Remove Stock"
            ]
        )

        if update_choice == "Change Name":

            new_name = st.text_input(
                "New Name"
            )

            if st.button("Update"):

                if new_name.strip():

                    selected_product.name = new_name

                    save_products(inventory)

                    st.success(
                        "Product updated successfully."
                    )

                else:

                    st.error("Name cannot be empty.")

        elif update_choice == "Change Category":

            new_category = st.text_input(
                "New Category"
            )

            if st.button("Update"):

                if new_category.strip():

                    selected_product.category = new_category

                    save_products(inventory)

                    st.success(
                        "Product updated successfully."
                    )

                else:

                    st.error("Category cannot be empty.")

        elif update_choice == "Increase Price":

            amount = st.number_input(
                "Amount",
                min_value=0.01
            )

            if st.button("Increase Price"):

                selected_product.increase_price(amount)

                save_products(inventory)

                st.success(
                    "Price updated successfully."
                )

        elif update_choice == "Decrease Price":

            amount = st.number_input(
                "Amount",
                min_value=0.01
            )

            if st.button("Decrease Price"):

                if amount <= selected_product.price:

                    selected_product.decrease_price(amount)

                    save_products(inventory)

                    st.success(
                        "Price updated successfully."
                    )

                else:

                    st.error(
                        "Price cannot become negative."
                    )

        elif update_choice == "Add Stock":

            stock = st.number_input(
                "Stock to Add",
                min_value=1,
                step=1
            )

            if st.button("Add Stock"):

                selected_product.add_stock(stock)

                save_products(inventory)

                st.success(
                    "Stock added successfully."
                )

        elif update_choice == "Remove Stock":

            stock = st.number_input(
                "Stock to Remove",
                min_value=1,
                step=1
            )

            if st.button("Remove Stock"):

                if stock <= selected_product.quantity:

                    selected_product.remove_stock(stock)

                    save_products(inventory)

                    st.success(
                        "Stock removed successfully."
                    )

                else:

                    st.error(
                        "Not enough stock."
                    )

        st.divider()

        st.write("### Current Product")

        display_product(selected_product)

    else:

        st.info(
            "Enter a valid Product ID."
        )


# =========================================================
# REMOVE PRODUCT
# =========================================================

elif menu == "Remove Product":

    st.header("🗑️ Remove Product")

    product_id = st.number_input(
        "Product ID",
        min_value=1,
        step=1
    )

    if st.button(
        "Remove Product",
        type="primary"
    ):

        selected_product = None

        for product in inventory.products:

            if product.product_id == product_id:

                selected_product = product
                break

        if selected_product:

            inventory.products.remove(
                selected_product
            )

            save_products(inventory)

            st.success(
                "Product removed successfully."
            )

        else:

            st.error(
                "Product not found."
            )


# =========================================================
# LOW STOCK
# =========================================================

elif menu == "Low Stock Products":

    st.header("⚠️ Low Stock Products")

    found = False

    for product in inventory.products:

        if product.quantity <= 5:

            display_product(product)

            found = True

    if not found:

        st.success(
            "No low stock products."
        )


# =========================================================
# ADMIN LOGOUT
# =========================================================

elif menu == "Logout" and st.session_state.admin_logged_in:

    st.session_state.admin_logged_in = False

    st.success("Admin Logged Out")

    st.rerun()


# =========================================================
# CUSTOMER REGISTER
# =========================================================

elif menu == "Customer Register":

    st.header("👤 Customer Registration")

    name = st.text_input("Customer Name")

    phone = st.text_input("Phone Number")

    email = st.text_input("Email")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Register",
        type="primary"
    ):

        username_exists = False

        for customer in customers:

            if customer.username == username:

                username_exists = True
                break

        if username_exists:

            st.error(
                "Username already exists."
            )

        elif not name.strip():

            st.error(
                "Name cannot be empty."
            )

        elif not username.strip():

            st.error(
                "Username cannot be empty."
            )

        elif not password:

            st.error(
                "Password cannot be empty."
            )

        else:

            person_id = len(customers) + 1

            customer = Customer(
                person_id,
                name,
                phone,
                email,
                username,
                password
            )

            customers.append(customer)

            save_customers(customers)

            st.success(
                "Customer Registration Successful!"
            )


# =========================================================
# CUSTOMER LOGIN
# =========================================================

elif menu == "Customer Login":

    st.header("🔐 Customer Login")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Login",
        type="primary"
    ):

        logged_customer = None

        for customer in customers:

            if customer.login(
                username,
                password
            ):

                logged_customer = customer
                break

        if logged_customer:

            st.session_state.logged_customer = logged_customer

            st.success(
                "Customer Login Successful!"
            )

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )


# =========================================================
# CUSTOMER DISPLAY PRODUCTS
# =========================================================

elif (
    menu == "Display Products"
    and st.session_state.logged_customer is not None
):

    st.header("📦 Available Products")

    if not inventory.products:

        st.info(
            "No products available."
        )

    else:

        for product in inventory.products:

            display_product(product)


# =========================================================
# CUSTOMER BUY PRODUCT
# =========================================================

elif menu == "Buy Product":

    logged_customer = (
        st.session_state.logged_customer
    )

    st.header("🛒 Buy Product")

    if not inventory.products:

        st.info(
            "No products available."
        )

    else:

        product_options = {}

        for product in inventory.products:

            product_options[
                f"{product.product_id} - {product.name}"
            ] = product

        selected_name = st.selectbox(
            "Select Product",
            list(product_options.keys())
        )

        selected_product = product_options[
            selected_name
        ]

        st.write(
            f"**Price:** ₹{selected_product.price:.2f}"
        )

        st.write(
            f"**Available Stock:** "
            f"{selected_product.quantity}"
        )

        if st.button(
            "Buy Product",
            type="primary"
        ):

            if selected_product.quantity <= 0:

                st.error(
                    "Product is out of stock."
                )

            else:

                order_id = len(orders) + 1

                order = Order(
                    order_id,
                    logged_customer
                )

                order.add_product(
                    selected_product
                )

                logged_customer.buy_product(
                    selected_product
                )

                selected_product.remove_stock(1)

                orders.append(order)

                save_products(inventory)

                st.success(
                    "Product Purchased Successfully!"
                )

                st.subheader(
                    f"Order #{order_id}"
                )

                st.write(
                    "**Customer:**",
                    logged_customer.name
                )

                st.write(
                    "**Product:**",
                    selected_product.name
                )

                st.write(
                    "**Price:**",
                    f"₹{selected_product.price:.2f}"
                )

                st.write(
                    "**Total Amount:**",
                    f"₹{selected_product.price:.2f}"
                )


# =========================================================
# PURCHASE HISTORY
# =========================================================

elif  menu == "Purchase History":

    logged_customer = (
        st.session_state.logged_customer
    )

    st.header("📜 Purchase History")

    if not logged_customer.purchase_history:

        st.info("No purchases yet.")

    else:

        for purchase in logged_customer.purchase_history:

            st.subheader(purchase["name"])

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.write("**Product ID**")
                st.write(purchase["product_id"])

            with col2:
                st.write("**Category**")
                st.write(purchase["category"])

            with col3:
                st.write("**Price**")
                st.write(f"₹{purchase['price']:.2f}")

            with col4:
                st.write("**Quantity Bought**")
                st.write(purchase["quantity"])

            st.divider()

# =========================================================
# VIEW ORDERS
# =========================================================

elif menu == "View Orders":

    logged_customer = (
        st.session_state.logged_customer
    )

    st.header("🧾 My Orders")

    customer_orders = []

    for order in orders:

        if order.customer == logged_customer:

            customer_orders.append(order)

    if not customer_orders:

        st.info(
            "No orders found."
        )

    else:

        for order in customer_orders:

            st.subheader(
                f"Order #{order.order_id}"
            )

            total = 0

            for product in order.products:

                st.write(
                    f"**{product.name}** — "
                    f"₹{product.price:.2f}"
                )

                total += product.price

            st.write(
                f"### Total: ₹{total:.2f}"
            )

            st.divider()


# =========================================================
# CUSTOMER LOGOUT
# =========================================================

elif (
    menu == "Logout"
    and st.session_state.logged_customer
    is not None
):

    st.session_state.logged_customer = None

    st.success(
        "Customer Logged Out"
    )

    st.rerun()