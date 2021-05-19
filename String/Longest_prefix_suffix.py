''' Given a string find the length of the longest proper prefix which is also a proper suffix
    ex- string:abbabb   length=3 as abb is pefix and suffix both'''

# using pre-processing technique of KMP

def longest_pre_suff(s):
    #list for storing length
    A=[-1]
    k=-1
    for i in range(1,len(s)):
        while k>-1 and s[k+1]!=s[i]:
            k=A[k]
        if  s[k+1]==s[i] :
            k+=1
        A.append(k)
    return A[-1]+1

if __name__ == '__main__':

    s = input("Enter string:")
    print("Length of Longest Prefix Suffix is :"+str(longest_pre_suff(s)))

'''
Sample Output:
Enter string:aaaa
Length of Longest Prefix Suffix is :3

Enter string:babababab
Length of Longest Prefix Suffix is :7
'''