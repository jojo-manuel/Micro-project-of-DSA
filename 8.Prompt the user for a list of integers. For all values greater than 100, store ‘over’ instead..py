#8.Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
list1=list(map(int,input("Enter the list by space seperation").split()))

for a in range (len(list1)):
    if list1[a]>99:
        list1[a]=('over')
print(list1)
