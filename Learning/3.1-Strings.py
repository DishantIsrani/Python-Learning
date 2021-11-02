a= "Israni"
name="Dishant"
print(type(name))

#concatenation of string 
print(name + a)

print(name[0])
print(name[1])

#name[3] = r --> this does not work you cant change a index 


#slicing(breaking) the strings 
print(name[0:3])
print(name[1:4])
#can leave it blank also 
print(name[:4]) #same as name[0:4]
print(name[0:]) #same as name[0:end]


#negative indices in this the last element is -1 
c=name[-3:-1] #is same as name[3:5]
print(c) 

d=name[-1]
print(d)


#slicing with skip values 
e=name[1:7:2] #the last 2 is the skip value 
print(e)



