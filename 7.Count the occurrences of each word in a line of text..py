#7.Count the occurrences of each word in a line of text.
line=input('Enter the paragraph:')
word=line.split()
for words in word:
    num=word.count(words)
    print({words:num})