
#I have successfully executed this in python online gdb.
def neon(n):
    s = n**2
    sum = 0
    while s:
        sum = sum+(s % 10)
        s = s//10
    if sum == n:
        return 1
    else:
       return 0
n = int(input())

if neon(n)==1:
    print(n, "is a neon number")
else:
    print(n, "is not a neon number")
    
#Sample Input: 9
#sample output: 9 is a neon number

