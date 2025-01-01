#6.List ordinal value of each element of a word 
word=input('Enter value')
for words in word:
    ordinal=ord(words)
    print('Cardinal value of',words ,'is',ordinal)