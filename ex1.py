#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
#the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string
#is less than 3, leave it unchanged.

simple_string = "abc"
if simple_string[-3:] == "ing":
    simple_string += "ly"
else:
    simple_string += "ing"
print(simple_string)
