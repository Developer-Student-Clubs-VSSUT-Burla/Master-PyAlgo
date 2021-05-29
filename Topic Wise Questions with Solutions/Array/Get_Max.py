"""
Query : Get Max
Task:
Given two vectors A and B of length a and b respectively and an integer N .
We have to make a maximum number of length N from the integers given in the two vectors A and B
such that the relative order of the digits from the same vector should be retained

Output a string of the obtained maximum number.

"""

"""
Attribute: a)The input vectors
           b)The considerable size
"""
def getMax(vector, size):
    list1 = []
    len_vector=len(vector)
    req_len = len_vector-size
    
    ind=0
    while ind < len_vector:
        len_list1=len(list1)
        while len_list1 and req_len>0  and vector[ind]>list1[-1]:
            list1.pop()
            req_len -= 1
        list1.append(vector[ind])
        ind+=1
    return list1[:size]


"""
Attribute: a)The input vectors
           b)The considerable size
Merge according to the greater number           
"""

def getMerged(get_list1,get_list2):
    res = []
    ptr1= 0
    ptr2 = 0
    len_get_list1=len(get_list1)
    len_get_list2=len(get_list2)
    while (ptr1<len_get_list1 and ptr2<len_get_list2) :
        if get_list1[ptr1]>get_list2[ptr2]:
            res.append(get_list1[ptr1])
            ptr1+=1
        else:
            res.append(get_list2[ptr2])
            ptr2+=1
    
    # Copy the remaining elements of get_list1, if there
    # are any
    while ptr1 < len_get_list1:
        res.append(get_list1[ptr1])
        ptr1+=1
  
    # Copy the remaining elements of get_list2, if there
    # are any
    while ptr2 < len_get_list2:
        res.append(get_list2[ptr2])
        ptr2+=1
    return res

#Driver-Code  
if __name__ == "__main__":
    
    #Input two list of integers
    print("Input First list Numbers:")
    A = list(map(int , input().split(' ')))
    print("Input Second list Numbers:")
    B = list(map(int , input().split(' ')))
    
    #Input N : length of the maximum number to be made
    print("Input the length of the maximum number to be made:")
    N = int(input())
    
    a = len(A)
    b = len(B)
      
    #Initializing an output array
    output = [0]*N
    len1=0
    while (len1<=N):
        #Checking the condition because that will not suffice our answer
        if len1>a or (N-len1)>b: 
            len1+=1
            continue 
        #Get the maximum possible number and get it merged 
        get_list1 = getMax(A, len1)
        get_list2 = getMax(B, (N-len1))           
        output = max(output, getMerged(get_list1,get_list2))
        len1+=1
          
    #Creating list of string items 
    output = [str(item) for item in output]
    
    # Join list items using join()
    answer = int("".join(output))
    
    print("Maximum possible number of size " + str(N))
    print(answer)
      
  
"""
Sample Test Cases
Example #1:
Input: A = [8 9] B = [1 0] N = 4
Output: 8910

Example #2:
Input: A = [1 7] B= [9 5] N = 3
Output: 975

Time Complexity : O((a+b)^3))
"""
  
  


