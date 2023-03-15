# # use mutible list every call
# def f1(x=[]):
#     length = len(x)
#     x.append(length)
#     return x

# print(f1([1,2]))
# print(f1(['a', 'b', 'c']))
# print(f1())
# print(f1())

# print(f1.__defaults__)

# # use a empty list every call
# def f(x, l=None):
#     if l is None:
#         l = []
#     for i in range(x):
#         l.append(i * i)
#     return l

# def greet():
#     # variable defined outside the inner function
#     name = "John"
    
#     # return a nested anonymous function
#     return lambda: "Hi " + name

# # call the outer function
# message = greet()

# # call the inner function
# print(message())

# # Output: Hi John


# # Python program to illustrate
# # enumerate function in loops
# l1 = ["eat", "sleep", "repeat"]

# # printing the tuples in object directly
# for ele in enumerate(l1):
#     print (ele)

# # changing index and printing separately
# for count, ele in enumerate(l1, 100):
#     print (count, ele)

# # getting desired output from tuple
# for count, ele in enumerate(l1):
#     print(count)
#     print(ele)



# def is_vowel(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False

# # sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# # using filter function
# filtered = filter(is_vowel, sequence)

# print('The filtered letters are:')
# for s in filtered:
#     print(s)


keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 
# but this line shows dict comprehension here 
myDict = { k:v for (k,v) in zip(keys, values)}
print(myDict)
