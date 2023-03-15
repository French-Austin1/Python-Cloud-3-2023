import logging
from Classes import Employee, Admin


# This is the logging module, by doing this config I can control what gets logged and the format.
logging.basicConfig(filename="./Python-Log.txt",
                    filemode="a",
                    format='%(asctime)s,%(name)s [%(levelname)s] %(message)s',
                    level=logging.INFO)

# Then we get the logger to start our log.
logger = logging.getLogger("Python Loops")


# Defining a fuction to keep from having to write this twice for the loop.
def make_employee(employee_id):
    '''Creates an Employee or an Admin and returns it.'''
    print("Employee Number {}".format(i+1))
    print("------------------")
    first_name, last_name, admin = "","",""  # I am assigning and empty string to each of the vars here.

# Here we use a while loop to ensure that first_name fits our end criteria.
    while len(first_name) < 1 or first_name.isnumeric():
        first_name = str(input("First Name: "))
    while len(last_name) < 1 or last_name.isnumeric():
        last_name = str(input("Last Name: "))
    while admin.casefold() != "y" and admin.casefold() != "n":
        admin = str(input("Is this an Admin? [y,n]"))
    
# This decides whether we create an employee or an admin account
    if admin.casefold() == "y":
        return Admin(employee_id,first_name, last_name)
    else:
        return Employee(employee_id, first_name, last_name)

"""-------------------------------------------------------------------------------------------"""

# This is the start of a while loop that will run until running == False
running = True
while running: # The same as while running == True:
    users = []
    print("Welcome to Day 2 of the python course.\nToday we are going to be learning about loops.\n")
    try:
        num_users = int(input("To get us started, How many Employees would you like to add today? "))
    except Exception as e:
        logger.error(e)

    # Here we are trying to create all of the employees. 
    # We use a try and except block to catch any errors and log them.
    try:
        if num_users < 1:
            print("There are no users to add.")
        else:
            try:
                for i in range(num_users):
                    if i == 0:
                        print("Alright, let's get started!\n")
                        users.append(make_employee(i))  # Here I am calling a function from the append method of the list.
                        print()                         # This will append whatever the result of make_employee() is to the list.
                    else:
                        users.append(make_employee(i))
                        print()
            except Exception as e:
                raise e             # We raise the exception because we want a higher level to handle it.


        # Finally we print out our new emails and any new admins
            print("These are the emails of the new users.\n")
            for user in users:
                print("{}".format(user.email))
            print("\nThese are the new Admins.\n")
            for user in users:
                if user.sec_level:
                    print("{}".format(user.first_name))

# We catch, print and log any exceptions.
    except Exception as e:
        print(e)
        logger.error(e)

# And check if we want to run the loop again.
    run_check = ''
    while run_check != "y" and run_check != "n":
        run_check = str(input("\nWould you like to quit? [y,n]"))
    if run_check.casefold() == "y":
        running = False
