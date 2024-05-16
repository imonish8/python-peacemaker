# Def
dictionary are key-value pair in python inside curly braces and there are many operations that can be performed on the dictionary using provided methods. 

# Methods
- clear()
  my_dict.clear()

- copy()
  new_dict = my_dict.copy()

- .fromkeys()
 new_dict = my_dict.fromkeys(['a', 'b' , 'c'] , 0)

- .get(key)
 value = my_dict.get('key' , 'default_value')

- .items() 
 items = my_dict.items()

- .keys()
 allKeys = my_dict.keys()

- .pop(key)
 removes and return the mentioned key.

- .popitem(key, value)
 removes the key-value pair from the dictonary if available.

- .setdefault(key)
 returns if available in dictionary, if not there, then inserts the given key in dictionary with default value to key-value pair.

- .update([other]) 
 updates the dictionary with key-value pair.

- .values()
 Displayes all the values in the dictionary.

# more on dictionary 

Dictionary: In python, Dictionary is an ordered (since Py 3.7) [unordered (Py 3.6 & prior)] collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized.