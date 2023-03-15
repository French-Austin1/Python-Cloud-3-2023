import pandas, random
from new_module import add
from math_stuff import double

# These are found in the two modules in the directory
print(double.time_two(5))
print(add.add_nums(5,17))

# Lambda can be used here instead of defining a function
x = lambda a, b: a + b
print(x(5, 17)) 

# Another use of lambda
def maker(x):
    return lambda a: a*x

doubler = maker(2)
tripler = maker(3)
print(doubler(4))
print(tripler(4))


# You can also use the lambda function in conjunction with the map function
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# map() will run a function against every item in an iterable.
final_list = list(map(lambda x: x*2, li))
print(final_list)


# This is an example of a generator function. Generator functions use yield instead of return
# The output of a generator function is a generator object. This can be used with either a for loop
# or by using the next() function.
def gen_example(num):
    while num>0:
        yield num
        num-=1

z = gen_example(25)
g = gen_example(5)
for i in z:
    print(z)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# Here we are using a module named pandas to work with an excel spreadsheet.

# We also leverage the power of the context-manager to open a text file and get the information within then close it when it is done.
cities_list = []
with open("cities.txt", "r") as f:
    [ cities_list.append(i) for i in f.readlines() ]

# Reading the excel and using dictionary comprehension for later use of the data.
wb = pandas.read_excel("./cities-and-states.xlsx")
city_state = { i:j for (i,j) in zip(wb.cities, wb.States)}

# Here we are geting a couple of random numbers from the random module.
# We then are printing the state that matches the City provided.
for i in range(10):
    rand_num = random.randint(0,999)
    print("City: {}State: {}\n".format(cities_list[rand_num],city_state.get(cities_list[rand_num].strip())))
