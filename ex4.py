#Append new string in the middle of a given (even number of characters) string Example:

word = "python"
new_word = "NEW"
result = word[:len(word) // 2] + new_word + word[len(word) // 2:]
print(result)
