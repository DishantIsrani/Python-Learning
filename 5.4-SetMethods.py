a =set()
print(a)
print(type(a))

#  METHOD 1  *****************
a.add(5)
a.add(6)
a.add(6)
a.add(6) # REPATING THE VALUE CANNOT CHANGE THE SET
#even if we add 6 more than 1 time it will still come only once cuase sets is not repetetive

# LIST OR DICTONARY OR ANY DATA THAT IS NOT HASHABLE CANNOT BE ADDED IN THE SET AS LIST CAN BE CHANGED AND SET CANNOT BE CHANGED 
# a.add([4,5,6])
#a.add({4:5})

# WE CAN ADD TUPLE IN PLACE OF LIST AS TUPPLE IS ALSO NOT CHANGEABLE
a.add((4,5,6))
a.add(7)
a.add(9)
print(a)


#  METHOD 2  *****************
# prints the lenght of the set 
print(len(a))



#  METHOD 3  *****************
# REMOVE 5 FROM SET A AND IT WILL GIVE AN ERROR IF THE ELEMENT IS NOT IN THE SET 
a.remove(6)
print(a)


#  METHOD 4  *****************
# it will remove any on random  element and return that element 
print(a.pop())


#  METHOD 5  *****************
# claer will clear all the elements in the set 
print(a.clear)


#  METHOD 6  *****************
b = {5, 7, 8, 9, 10}
c = {19, 4, 7, 5, 3, 9, 11}

print(b.union)
print(c.union)

