#5.Form a list of vowels selected from a given word
word=input("Enter the word:")
vovel="aeiou"
word=word.lower()
for words in word:
 if words in vovel:
    print(words)