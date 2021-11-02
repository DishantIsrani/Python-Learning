myDict={
    "fast": "In a quick manner",
    "dishant" : "Learning",
    "marks": [1,4, 5,6,7],
    "anotherdict": {'harry':'player', 'dishant': 'tsec'}, #one more dictonary in a dictonary
    1 : 24
}

# MEHTOD 1 ********************

# PRINTS ALL THE KEYS IN THE DICTONARY
print("\n",myDict.keys())
print("\n",type(myDict.keys())) #this will be class of dict its dict keys

#to change the type of the keys to list
print("\n",list(myDict.keys())) 
 

# MEHTOD 2 ********************

# PRINTS ALL THE VALUE IN THE DICTONARY
print("\n",myDict.values())
print("\n",list(myDict.values())) 


# MEHTOD 3 ********************

# PRINTS ALL THE ITEMS/CONTENTS IN THE DICTONARY IN (KEY : VALUE) PAIR
print("\n",myDict.items())


# MEHTOD 4 ********************
print("\n",myDict)

# TO UPDATE AN EXISTING DICTONARY
updateDict={
    'updated new' :'lastest update',
    'again': 'added'
}
myDict.update(updateDict) #updates by adding the (key : value) pair from updatedict
myDict.update({'other way':' to update without making other dict'}) 
print("\n", myDict)


# MEHTOD 4 ********************

#if we put .get it will return none if the key is not in the dict but the next line will give an error if we dont put get
print("\n", myDict.get('dishant'))
print("\n", myDict['dishant'])

#the below key is not present in the dict so .get will give none and the other will give error
print("\n", myDict.get('dishant2'))
# print("\n", myDict['dishant2'])

