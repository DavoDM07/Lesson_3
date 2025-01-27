#Create a string made of the rst, middle and last character of given string with odd number of
#symbols

word = "sevak"
result = word[0] + word[len(word) // 2] + word[-1]
print(result)