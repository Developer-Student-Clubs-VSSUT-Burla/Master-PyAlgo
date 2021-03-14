#Finding out the length of the Longest Increasing Subsequence

def get_Length_LIS(list_elements):  
    
    LIS = []                    #Declaring a list and initializing it with 1 for length of list_elements
    for i in range(len(list_elements)):
        LIS.append(1) 
  
    for i in range (1 , len(list_elements)): 
        for j in range(0 , i): 
            if (list_elements[i] > list_elements[j] and LIS[i] <= LIS[j]) : 
                LIS[i] = LIS[j] + 1
  
    #Now finding the maximum LIS
    maximum_LIS = 0
 
    for i in range(len(list_elements)): 
            maximum_LIS = max( maximum_LIS , LIS[i]) 
    
    return maximum_LIS

  
#main
if __name__=="__main__":
    
    #Input from user
    L=[]
    n=int(input("Enter number of elements for list: "))
    for i in range(n):
        L.append(int(input("Enter element: ")))
    print("The list you entered is: ", L)
    
    length_LIS = get_Length_LIS(L)
    print()
    print ("Length of Longest Increasing Subsequence is", length_LIS ) 

#Sample Output
# L = [13, 4, 5, 24, 6, 8, 1] 
# Output: 4

#Time Complexity: O(n^2)