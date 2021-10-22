a=[1,4,5, 67,6]

print(a)
print(a[3])

print("The index 0 element before changing ", a[0])
a[0]= 7
print("The index 0 element after changing ", a[0])
print(a) 

# we can create a list with diff data types
b=[4,"dishant" , False, 8.7]
print(b)


# LIST SLICING 
names=["harry",  "dishant", "kanta", 45]
print(names[0:2])
print(names[-4:-1])
print(names[4:0:-1])
print(names[4::-1])

list1= [1,2,3,4,5,6,7,8,9]
print(list1[2::-1]) #to get the first number dont input the second condition