# List
mylists = [1,2.3,"Hello",["Hello", 2,5.6]]
# List properties
# mutable
# can be nested
# faster
# stores data of different types
# negative indexing

# Method Description
# append(): 	Adds an element at the end of the list
# clear():  	Removes all the elements from the list
# copy():   	Returns a copy of the list
# count():  	Returns the number of elements with the specified value
# extend(): 	Add the elements of a list (or any iterable), to the end of the current list
# index():  	Returns the index of the first element with the specified value
# insert(): 	Adds an element at the specified position
# pop():    	Removes the element at the specified position
# remove(): 	Removes the first item with the specified value
# reverse():    Reverses the order of the list
# sort():   	Sorts the list

# tuple
mytuples = (3,1,3,5,1,2,3,4,5,4,5,4,12,4,8,4,2,1,1,4,5,6,6,8,7,8,9,2,5)
mytuples2 = (23)
print(type(mytuples))#this becomes a tuple
print(type(mytuples2))#this becomes a int
# can be nested
# faster
# immutable
# stores data of different types
# negative indexing

# Method Description
# count(): Returns the number of times a specified value occurs in a tuple
print(mytuples.count(1))
# index(): Searches the tuple for a specified value and returns the position of where it was found
print(mytuples.index(5))