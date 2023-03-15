
# Python Day 2

Day two is all about functional programming and getting use to the way python executes code.  

Below you will find a list of standard test questions and their general answers. Following that is a section of coding practice problems for you to try out.


# Python Test Questions
1. What is Python? What are some of its key features?
    - Python is a high-level, interpreted programming language that is easy to learn and use. It is known for its simplicity, readability, and versatility. Some key features of Python include dynamic typing, automatic memory management, and support for object-oriented, functional, and procedural programming paradigms.
2. Explain the difference between a list and a tuple in Python.
    - In Python, a list is a mutable sequence of elements, while a tuple is an immutable sequence of elements. Lists are typically used for collections of homogeneous elements, while tuples are used for collections of heterogeneous elements that represent a single entity, such as a coordinate or a date.
3. What is the difference between an integer and a float in Python?
- An integer is a whole number, while a float is a number with a decimal point. Integers are represented in Python as int objects, while floats are represented as float objects. In general, floats are used for more precise calculations that involve decimal values, while integers are used for integer-based calculations.
4. How do you create a dictionary in Python?
- In Python, a dictionary is created using curly braces {} and contains a set of key-value pairs separated by colons. For example: my_dict = {"apple": 1, "banana": 2, "orange": 3}.
5. What is the difference between "==" and "is" in Python?
- "==" is used to compare the values of two objects in Python, while "is" is used to compare the object identities. "==" returns True if the values of the two objects are equal, while "is" returns True if the two objects have the same memory address.
6. How do you define a function in Python?
- In Python, a function is defined using the "def" keyword followed by the function name and parameters. The body of the function is indented and contains the instructions to be executed when the function is called. For example:
```
def multiply(a, b):
    return a * b

```
7. How do you import a module in Python?
- In Python, you can import a module using the "import" keyword, followed by the name of the module. For example: import math.
8. Explain what a decorator is in Python.
- In Python, a decorator is a special type of function that can modify the behavior of another function without changing its source code. Decorators are denoted by the "@" symbol followed by the decorator name. For example:
```
@my_decorator
def my_function():
    # function body

```
9. What is a generator in Python? How is it different from a list?
- In Python, a generator is a special type of iterator that generates values on the fly rather than storing them in memory. Generators are created using the "yield" keyword, and are typically used for large or infinite sequences of values that cannot be stored in memory. A list, on the other hand, is a collection of values that are stored in memory.
10. How do you handle errors in Python?
- In Python, errors can be handled using try-except blocks. The try block contains the code that may raise an exception, while the except block contains the code to be executed if an exception is raised. For example:
```
try:
    # code that may raise an exception
except Exception as e:
    # code to handle the exception

```
# Python Coding Problems
1. Write a Python function to calculate the factorial (*the product of an integer and all the integers below it*) of a given number.
2. Write a Python program to find the sum of all the even numbers in a given list.
    - `[139, 111, 121, 119, 184, 198, 32, 68, 176, 154]` = 812
    - `[14, 133, 84, 0, 119, 103, 12, 37, 67, 94]` = 204
    - `[112, 184, -24, 198, 107, -169, 134, 88, 41, 94]` = 786
3. Write a Python program to reverse a given string.
4. Write a Python function to check whether a given number is prime or not.
5. Write a Python program to sort a list of integers in ascending order.
6. Write a Python function to check whether a given string is a palindrome or not.
7. Write a Python program to find the second smallest number in a given list.
8. Write a Python function to calculate the area of a rectangle.
9. Write a Python program to remove all the duplicates from a given list.
10. Write a Python program to convert a given string to lowercase.