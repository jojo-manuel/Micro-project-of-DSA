#10.Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums to same value (c) whether any value occur in both
list1=list(map(int,input("Enter the list by space seperation for list1").split()))
list2=list(map(int,input("Enter the list by space seperation for list2").split()))

if len(list1) == len(list2):
    print('length is of both list is same')
elif len(list1) > len(list2):
    print('list1 is greater')
else:
    print('list2 is greater')
    
if sum(list1) == sum(list2):
    print('length is of both list is same')
elif sum(list1) > sum(list2):
    print('list1 is greater')
else:
    print('list2 is greater')
    
