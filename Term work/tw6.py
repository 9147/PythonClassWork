'''
Create an object-oriented program that allows you to enter data for customers and
employees.
Problem Details

Create a Person class that provides attributes for first name, last name, and emailaddress. This
class should provide a property or method that returns the person’s fullname.
Create a Customer class that inherits the Person class. This class should add anattribute for a
customer number.
Create an Employee class that inherits the Person class. This class should add anattribute for a
PAN number.
The program should create a Customer or Employee object from the data entered bythe user,
and it should use this object to display the data to the user. To do that, theprogram can use the
isinstance() function to check whether an object is a Customer orEmployee object.
'''

class Person:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"


class Customer(Person):
    def __init__(self, first_name, last_name, email_address, customer_number):
        super().__init__(first_name, last_name, email_address)
        self.customer_number = customer_number


class Employee(Person):
    def __init__(self, first_name, last_name, email_address, pan_number):
        super().__init__(first_name, last_name, email_address)
        self.pan_number = pan_number


def main():
    people = []  # List to store created objects

    while True:
        print("Menu:")
        print("1. Add Customer")
        print("2. Add Employee")
        print("3. Display All")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            first_name = input("Enter customer's first name: ")
            last_name = input("Enter customer's last name: ")
            email_address = input("Enter customer's email address: ")
            customer_number = input("Enter customer number: ")

            customer = Customer(first_name, last_name, email_address, customer_number)
            people.append(customer)  # Add the object to the list
            print("Customer added successfully.")
        elif choice == 2:
            first_name = input("Enter employee's first name: ")
            last_name = input("Enter employee's last name: ")
            email_address = input("Enter employee's email address: ")
            pan_number = input("Enter PAN number: ")

            employee = Employee(first_name, last_name, email_address, pan_number)
            people.append(employee)  # Add the object to the list
            print("Employee added successfully.")
        elif choice == 3:
            print("\nAll Created Objects:")
            for person in people:
                print(type(person).__name__)  # Display the class name (Customer or Employee)
                print(f"Full Name: {person.get_fullname()}")
                print(f"Email Address: {person.email_address}")
                if isinstance(person, Customer):
                    print(f"Customer Number: {person.customer_number}")
                elif isinstance(person, Employee):
                    print(f"PAN Number: {person.pan_number}")
                print("-" * 20)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
