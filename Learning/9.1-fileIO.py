#open is a bultin function and it is usd to open files and it defines the mode that is read or write eg open("filename",'mode') 
# # f = open('python self/sample.txt', 'r') # and default mode is r
# f = open('python self/sample.txt')

# # f.read() this will read the data in the file 
# data = f.read()
# # data = f.read(5) # this will read only first 5 characters  
# print(data)
# f.close()





# # ****READLINE this will only give the first line of the text doc and ***READLINES it will give "list" of all the lines  
# data = f.readline()
# print(data, end="")
# data = f.readline() #using readline multiple times will give the next lines in the doc 
# print(data)
# f.close()




# MODES 
# read -r 
# write - w
# append - a
# update - +
# to read from binary - rb
# to read from text - rt  # the t is default you dont have to add it manually 




# # write in a file will overwrite the whole content 
# f = open('python self/sample2.txt', 'w')
# f.write("I will be writitng with this code in the sample text and a new file sample2 text will be created")
# f.write("I will be adding the second line in this")
# f.close()



# # to add content at the end of the file we use append 
# f = open('python self/sample2.txt', 'a')
# f.write("I will be appending the sample2 txt with this code")
# f.close()



# # USING THE WITH FUNCTION 
# with o f.read()
# with oppen('python self/sample2.txt', 'r') as f:
#     a =en('python self/sample2.txt', 'w') as f:
#     a = f.write("me")

# print(a)