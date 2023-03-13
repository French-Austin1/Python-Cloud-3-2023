
# Python Day 1

## What is Python?

Python is a high-level, general-purpose programming language. It is dynamically typed meaning a variable can be assigned an object and the
type will be assigned at runtime. It has a garbage collector to manage the memory being used and clean up anything that is no longer needed.

Python is both an interpreted and compiled language, it is compiled down to byte-code and interpeted by the Python virtual machine.

## Terms and definitions:
- Basic Data Types: Numeric, Text, Boolean
- Numeric Data: Integers `(1, 2, 3, 10, -14)`, Floats `(3.14, 42.8, -0.15729)`
- String: A text data type, written in python as:
    - 'Hello'
    - "Hello"
    - '''Hello'''
    - """Hello"""
- Boolean: True or False, can also be represented as an empty object `(0, '', "", (), [], None)` for false or a non-empty object `(1, "hi", [13,15], (13,15))` for true.
- Compound Data Types:
    - Tuples `(10,20), ("x","y", 12, "Banana")` - Ordered, immutable and allows duplicate items. Can contain multiple data-types
    - Sets `{"Apple", "Orange", "Banana"}` - Unordered, mutable and do not allow duplicate items. Can contain multiple data-types. `frozenset()` is an immutable version of a set.
    - Lists `[1, 2, 5, "Apple", [14, "blue"]]` - Ordered, mutable and allows duplicates. Can contain multiple data-types
    - Dicts `{"First Name" : "Austin", "Height in Inches" : 70}` - Key : Value pairs, mutable and allows duplicate Values but does not allow duplicate keys. Can contain multiple data-types.
- Objects: Almost everything in python is an object. it's simply a collection of data and methods.
- Class: A Blueprint/Reference to an object. String is a class and `"hello"` is an object of class String with methods like `.upper()`.
- Operators: built in functions to preform actions on objects.
    - Assingment Operator: `=`
    - Comparison Operators: `<, >, ==, !=`
    - Logical Operators: `and, or, not`
    - Identity Operators: `is, is not`
    - Membership Operators: `in, not in`
