#12.Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.

#SIMPELE WAY
word=input('Enter the string:')
print(word[0]+(len(word)-1)*'$')

#Other way
word=input('Enter the string:')
word=word[0]+(len(word)-1)*'$'
print(word)
