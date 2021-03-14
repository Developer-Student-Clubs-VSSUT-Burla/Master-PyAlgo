
# Input : X = "AGGTAB"  , Y = "GXTXAYB"
# Output : Lenght of LCS is 4


# Input : X = "OPENSOURCE" , Y = "OPENSOUP"
# Output : Lenght of LCS is 7

# Time Complexity : O(len(X)*len(Y))
# Space Complexity : O(len(X)*len(Y))


def lcs(X,Y): 
    ## Finding LCS Function starts here 
    length_X = len(X)                                                           
    length_Y= len(Y) 
    ## using list compreshension for finding 'List_res'
    List_res= [[None]*(length_Y+1) for element in range(length_X+1)]


    ## loop over the length of Words
    for i in range(length_X+1): 
        for j in range(length_Y+1):                                                
            ## as nothing is common b/w them
            if i == 0 or j == 0 : 
                List_res[i][j] = 0                                                 
            ## as we have common elements     
            elif X[i-1] == Y[j-1]: 
                List_res[i][j] = List_res[i-1][j-1]+1                             
            else: 
                ## as we want longest so max() is being used 
                List_res[i][j] = max(List_res[i-1][j] , List_res[i][j-1])          
             
    return List_res[length_X][length_Y] 


# Driver program to test the above function 
X = input('Enter the First String : ')
Y = input('Enter the Second String : ')
print("Length of LCS is ", lcs(X, Y)) 


