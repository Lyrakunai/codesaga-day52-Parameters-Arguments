# Codesaga – Day 52
# Topic: Parameters, Arguments, Positional Arguments, Keyword Arguments


# --------------------------------------------------
# PRACTICE 1 – Parameters vs Arguments
# --------------------------------------------------

def student_profile(name, age):
    print("Name:", name)
    print("Age:", age)


student_profile("Nainu", 17)


# --------------------------------------------------
# PRACTICE 2 – Positional Arguments
# --------------------------------------------------

def calculate(a, b):
    print("First:", a)
    print("Second:", b)


calculate(8, 4)


# --------------------------------------------------
# PRACTICE 3 – Keyword Arguments
# --------------------------------------------------

def profile(name, age, city):
    print(name)
    print(age)
    print(city)


profile(name="Riya", age=17, city="Patna")


# --------------------------------------------------
# PRACTICE 4 – Mixed Positional + Keyword Arguments
# --------------------------------------------------

def order(item, quantity, price):
    total = quantity * price

    print("Item:", item)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Total:", total)


order("Book", 3, price=200)


# --------------------------------------------------
# PRACTICE 5 – Positional-Only Parameters
# --------------------------------------------------

def create_user(name, age, /, city):
    print(name)
    print(age)
    print(city)


create_user("Nainu", 17, city="Patna")


# --------------------------------------------------
# PRACTICE 6 – Keyword-Only Parameters
# --------------------------------------------------

def transfer(account_from, account_to, amount, *, note):
    print("From:", account_from)
    print("To:", account_to)
    print("Amount:", amount)
    print("Note:", note)


transfer(
    "Bara",
    "Riya",
    50000,
    note="Payment"
)


# --------------------------------------------------
# PRACTICE 7 – Positional-Only + Normal + Keyword-Only
# --------------------------------------------------

def create_account(name, age, /, city, *, account_type):
    print(name)
    print(age)
    print(city)
    print(account_type)


create_account(
    "Nainu",
    17,
    city="Patna",
    account_type="Student"
)


# --------------------------------------------------
# PRACTICE 8 – Real Function Interface
# --------------------------------------------------

def place_order(product, quantity, /, *, price, payment_method):
    total = quantity * price

    print("Product:", product)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Payment:", payment_method)
    print("Total:", total)


place_order(
    "Laptop",
    2,
    price=50000,
    payment_method="UPI"
)