''' 
An integer x is said to be Noble given an array if the number of integers greater than x are equal to x.
If noble integer is not found output is -1. 
'''

def nobleint(lst,number):
    x = 0
    lst.sort()
    for i in range(0, number - 1):
        if lst[i] == lst[i + 1]:
            continue
        if lst[i] == number - i - 1:
            x = 1
            return number - i - 1
    if x == 0:
        return -1

number = int(input('Enter the number of elements:'))
lst = list(map(int, input('Enter the elements:').split()))
nobleInteger = nobleint(lst, number)
if nobleInteger==-1:
    print("Noble Integer not present")
else:
    print("Noble Integer =",nobleInteger)

'''
Sample Output
Enter the number of elements:4
Enter the elements:7 3 9 81
Noble Integer = 3

'''

