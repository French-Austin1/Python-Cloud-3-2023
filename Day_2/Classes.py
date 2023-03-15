


class Employee():
    ''' An Employee of the company.'''
    def __init__(self, id: int, first_name: str, last_name: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = "{}.{}@mysite.com".format(last_name, first_name)
        self.sec_level = 0

    def check_email(self):
        print("you have no new emails {}, check back later.".format(self.first_name))

    def check_admin(self):
        if self.sec_level:
            print("Your an admin!")
        else:
            print("Your not an admin!")

class Admin(Employee):
    ''' An Admin, child class of an employee'''
    def __init__(self, id, first_name, last_name):
        super().__init__(id, first_name, last_name)
        self.sec_level = 1


# create an employee and set it to a variable.
x = Employee(1,"a","b")

# call a method inside a class object
x.check_email()