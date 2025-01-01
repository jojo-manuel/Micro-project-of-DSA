#14.Create a string from given string where first and last characters exchanged.
word=input('Enter the string:')
word=word[-1]+word[1:-1]+word[0]
print(word)
