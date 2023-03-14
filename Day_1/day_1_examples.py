'''tuples'''

my_tuple = (10, 20, 30)
my_str = ("Hello World!", "hello")

# Adding tuples together to make a new tuple
a = my_tuple + my_str

# Casting a tuple to a list in order to append an item.
a = list(my_tuple)
a.append(my_str)
my_tuple = tuple(a)


'''Lists'''

my_list = ["Jason","Austin","Taite"]

# Return a the list in reverse order
my_list[:-1] 

# Get an element out of a list (Zero indexed)
my_list[2]

# Add an element to the end of the list
my_list.append("Bryan")

'''Sets'''

my_set = {"Austin", "Bryan", "Nathen"}
your_set = {"Kyle", "Bryan", "Tyler"}

# add an element to a set. This would not make any change to the set as it already exists within it.
my_set.add("Austin")

# Find the difference between sets
diff = my_set.difference(your_set)

# Update a set with a union of itself and others
my_set.update()

# Remove an element from the set
my_set.discard("Austin")

# What would my_set be here?
print(my_set)

'''dicts'''

my_dict = {"First Name":"Austin", }

# you can add items to a dict by using a new Key as an index
my_dict["Last Name"] = "French"

# use the .get() function to get specific values, if you use this 
my_dict.get("First Name")

# You can also get the value by calling an index in the dict
my_dict["First Name"]

# Returns a set-like object of all the of the keys, the same can be done with .values()
my_dict.keys()
my_dict.values()


