def hasAllcodes(s, k) :
	substring = set()
	for i in range (len(s) -k + 1):
		substring.add(s[i:i+k])
	return len(substring) == pow(2, k)

#input
s = str(input("Enter Binary String: "))
k = int(input("Enter length of substring: "))
if (hasAllcodes(s,k)):
	print("YES")
else:
	print("NO")
