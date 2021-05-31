'''
Aim: To output the total number of distinct inputs on a single line.

We'll use sets here. An element will only get added in a set if it's not 
already present. Using this idea, we can have all distinct inputs in the
end.

'''

# getting the number of total elements to be added
N=int(input().strip())
# initializing an empty set
s=set()
for i in range(0,N):
    # getting all the elements 
    p=input().strip()
    # adding the inputs in the set
    # it will retain only unique inputs
    s.add(p)
# printing out the total number of distinct inputs
print(len(s))         

'''

COMPLEXITY:
	
	 Time Complexity -> O(N)
	 Space Complexity -> O(1)
     
Sample Input:
7
UK
China
India
UK
Russia
USA
Germany

Sample Output:
6

Explanation:
All unique inputs --> UK, China, India, Russia, USA, Germany [6]
Hence, the output is 6.

'''