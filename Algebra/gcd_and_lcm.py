# Python program to find LCM AND GCD of two numbers
#WE KNOW THAT (a x b) = GCD(a,b) * LCM (a,b)

def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)

# Function to return LCM of two numbers
def lcm(a,b):
	return (a / gcd(a,b))* b

# Driver program to test above function
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))
print('HCF of', a, 'and', b, 'is', gcd(a, b))