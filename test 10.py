# Parent class
class User:
    name = "Tom"
    email = ' '
    password = "1234abcd"
    account = 0

# Child class
class Employee(User):
    base_pay = 11.00
    department = 'General'

# Child class
class Customer(User):
    mailing_address = ' '
    mailing_list = True

# Creating instances of the child classes
employee = Employee()
customer = Customer()

# Displaying information
print("Employee Information:")
print(f"Name: {employee.name}")
print(f"Base Pay: ${employee.base_pay}")
print(f"Department: {employee.department}")
print()

print("Customer Information:")
print(f"Name: {customer.name}")
print(f"Mailing Address: {customer.mailing_address}")
print(f"Mailing List: {customer.mailing_list}")
