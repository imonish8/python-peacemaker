## The del statement¶

the del statements are alternate to the .pop method of list, which infact deletes the value by mentioneing the Index of the element in the list, without even returning it.

del statement can be used to slice the list or remove the entire list.

>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]


<img src ="notes/Screenshot 2024-05-15 at 2.35.37 PM.png">

## More on del statment

The del statement in Python is used to remove an element from a collection or to delete a variable from the current scope. Its functionality varies depending on what it's applied to:

### 1. Deleting Elements from a Collection: If you want to remove an item from a list given its index or a slice of indices, you can use del. For example:

'''python

my_list = [1, 2, 3, 4, 5]
del my_list[2]  # Removes the element at index 2 (value: 3)
print(my_list)  # Output: [1, 2, 4, 5]

del my_list[1:3]  # Removes elements from index 1 to index 2
print(my_list)  # Output: [1, 5]


'''

### 2. Deleting Variables: You can also use del to delete variables from the current scope, making them no longer accessible. For example:

'''
x = 5
print(x)  # Output: 5

del x
print(x)  # Raises NameError: name 'x' is not defined


'''

### 3. Deleting Attributes: In Python, you can also delete attributes of objects using del. For instance:

'''py
class MyClass:
    def __init__(self):
        self.x = 5
        self.y = 10

obj = MyClass()
print(obj.x)  # Output: 5

del obj.x
print(obj.x)  # Raises AttributeError: 'MyClass' object has no attribute 'x'

'''