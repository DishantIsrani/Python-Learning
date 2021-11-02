story="i am learning python from code with harry and now i am on srting literals from harry"

#string functions 
print(len(story))
print(story.capitalize()) # will cap the first word

print(story.endswith("hjek"))
print(story.endswith("als"))

print(story.count("h"))
print(story.count("ar"))
print(story.count("i am"))

print("this will give the index")
print(story.find("i am"))
print(story.find("harry"))
print(story.find("hary"))


print(story.replace("harry", "Dishant"))


#escape sequence character 
name = "my name is \tdishant.\n this is a new line using -> \\n"
print(name)