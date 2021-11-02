t = (1,3, 4, 5)  #creating a tuple
print(t)
print(t[0])

#************************************************

# YOU CANNOT UPDATE A TUPLE
# t[0]= 45 # this will give an error 

#************************************************

#empty tuple
t1= ()
print(t1)

# when creating a tuple with one value you need to end it with a coma 
t2 = (5,)
t3 = (5)  #this is a wrong way to create a tuple with a single element 
print(t2)
print(t3)



#************************************    TUPLE METHODS
t5 = (1, 5, 6, 8, 9, 1)

# THIS WILL COUNT HOW MANY TIMES THE ELEMENT APPEARS IN THE TUPLES  t.count(element)
print("The number 1 appears", t5.count(1) , "times")

# TO CHECK THE ELEMENT IS PRESENT ON WHICH INDEX
print("The elemetn 6 is present at index", t5.index(6))