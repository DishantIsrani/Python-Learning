l1=[1,8,7,2,21,15]
print(l1)

# THIS WILL SORT THE L1 ITSELF WE WONT HAVE TO SAVE IT IN OTHER VARIABLE 
l1.sort()
print("\nThis is the sorted list",l1)

# THIS WILL REVERSE 
l1.reverse()
print("\nThis is the reverse list",l1)


# THIS WILL APPEND AT THE END IN THE LIST 
l1.append(76)
print("\nThis will append at end of the list",l1)


# THIS WILL INSERT AT THE GIVEN INDEX FOR EXAMPLE l1.insert(index, value) 
l1.insert(0, 100)
print("\nThis will insert at given index of the list",l1)


# THIS WILL POP THE ELEMENT AT THE GIVEN INDEX l1.pop(index)
l1.pop(4)
print("\nThis will pop at given index of the list",l1)


# THIS WILL REMOVE THE GIVEN ELEMENT FROM THE LIST l1.remove(element)
l1.remove(2)
print("\nThis will remove the given element from the list",l1)


