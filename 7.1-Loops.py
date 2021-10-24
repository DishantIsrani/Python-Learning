# WHILE LOOPS 

# i = 0
# while i < 10:
#     print("Yes "+ str(i))
#     i=i+1

# print("done")



# # printing a list with while 
# fruits = ["orange", "mango", "banana", "apple", "grape", "jamun", "watermelon"]
# i=0 

# while i < len(fruits):
#     print(fruits[i])
#     i=i+1





# FOR LOOPS 

fruits = ["orange", "mango", "banana", "apple", "grape", "jamun", "watermelon"]

for item in fruits:
    print(item)


print("\n\n\n")


# FOR LOOP WITH ELSE
for a in range(10):
    print(a)
else: 
    print("this is inside else of FOR LOOP")


print("\n\n\n")


# FOR LOOP WITH BREAK
#the ELSE PART IN THE FOR LOOP WONT BE EXECUTED AS THE FOR LOOP IS NOT SUCESSFULL TERMINATION AND TERMINATED BY BREAK

for b in range(10):
    print(b)
    if b==5:
        break
else:
    print("this is inside else of FOR LOOP")
    



print("\n\n\n")
# FOR LOOP WITH CONTINUE 
# AT C =5 IT WILL SKIP THE LOOP AND PRINT THE NEXT NUMBER THAT IS 6 

for c in range(10):
    if c==5:
        continue
    print(c)



# PASS STATEMENT is similar to null statement it does nothing

d = 4

if i>0:
    pass

while i>6:
    pass



