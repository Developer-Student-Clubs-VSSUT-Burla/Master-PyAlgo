n = int(input())
s = n**2
sum = 0
while s:
    sum = sum+(s % 10)
    s = s//10


if sum == n:
    print(n, "is a neon number")
else:
    print(n, "is not a neon number")
