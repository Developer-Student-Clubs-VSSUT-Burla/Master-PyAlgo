#enter elements of array
elements = list(map(int,input("enter elements of array: ").split()))

mini=100000
maxi=0

for a in elements:
	if (a<mini):
		mini=a
	if(a>maxi):
		maxi=a

print("Maximum Element is : ",maxi)
print("Minimum Element is : ",mini)

