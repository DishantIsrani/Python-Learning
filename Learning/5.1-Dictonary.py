myDict={
    "fast": "In a quick manner",
    "dishant" : "Learning",
    "marks": [1,4, 5,6,7],
    "anotherdict": {'harry':'player', 'dishant': 'tsec'} #one more dictonary in a dictonary
}

print(myDict['Fast'])
print(myDict['Dishant'])
print(myDict['marks'])
print(myDict['anotherdict'])
#to print the dictonary(anotherdict) inside the mydict
print(myDict['anotherdict']['harry'])


# you CAN ALSO CHANGE A VALUE IN THE DICTONARY LIKE BELOW
myDict['marks']=[45, 46, 47]
print(myDict['marks'])
