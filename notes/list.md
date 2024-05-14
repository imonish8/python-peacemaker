# list methods are 

- append - addinng item to the end of the list/
- extend - adding another list or appending items from another list.
- insert - insert an item in specified postion.
- remove - remove the first occurrence of the spcified value.
- pop - remove and return an item at specified index/ position.
- Subset - extract a subset of the list.
- clear - remvoies alll the items from the list.
- count - returns the number of the occurence of the specified value in the list.
- sort(key=None, reverse=False):
- reverse() - reverses the entire values in list.


my_list = [1, 2, 3, 4]
mixed_list = ["hello", 3 , true, 3.12] >>> mixed list can contain the different data structures or even a list inside a mixed list.

print any index you want from list using index just like you used to do in java.

my_list.append(3)
append usage

my_list.extend([2,5])
extend usage 

my_list.insert(2, 2.5) >>> my_list.insert(indexNo, value which you want to insert to this index)
inserting 2.5 at index 2

my_list.remove(4) >>> remove the first occurence of value which you want to remove, this will only remove the first occurence, do it as much as the occurence is or use loop to remove multiple occurence while iterating.

popped_item = my_list.pop(0) 
specified value in the pop will result in popping out the value from the list and retirng it that is printing it to console.

# index(x[, start[, end]]): Return the index of the first occurrence of a specified value within a specified range.

co

subset = my_list[1 : 4] 
subset is slicing the list from given first index to desired index.

my_list.reverse()
reverses the entire list in the opposite direction.

my_list.copy()
returns the shallow copy of the list. this does not mean to have the exact copy when in storage the pool of memoery will have one list named my_list with two different location, so when try to print the copied list uou will fail, because the shallow copy is jyst shallow.

# List as Stack

Stakc in possible in list because of the flexible properities of the list like append , pop etc.

# list as queue and list as deque.

list as queue means first in first out
list as deque means both-side in any-side out.

# List , List Comprehsion done, Nest List Comprehsion is left only.

# All methods are revised throughly.

# got it.

[References](https://docs.python.org/3/tutorial/datastructures.html)