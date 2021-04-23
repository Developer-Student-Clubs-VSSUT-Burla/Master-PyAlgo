"""
Given two strings - text and pattern, find the starting index
of the first occurrence of the pattern in the text. For eg:

INPUT
Enter text: bccdacbeeacbx
Enter pattern: acb
OUPUT
Pattern found at index 4

Even though 'acb' occurs in text at both indices 4 and 9, 4
is considered as index of first occurrence has been asked. 
"""

#Total number of possible characters
total_char = 256
#Large prime number, to limit hash values to a certain range
prime_num = 10**9 + 9

def string_search(text, pattern):
    pat_len = len(pattern)
    text_len = len(text)

    #Hash values for pattern and text respectively
    pat_hash = text_hash = 0 

    #Flag to determine if pattern was ever found
    pattern_found = False

    #Calculating hash for pattern and first substring in text of same length
    #as pattern
    for i in range(0, pat_len):
        pat_hash = ((total_char*pat_hash) + ord(pattern[i])) % prime_num
        text_hash = ((total_char*text_hash) + ord(text[i])) % prime_num
    
    #Variable storing total_char raised to power (length of pattern - 1), 
    #required to quickly calculate hash value of each window of text
    count_power = 1
    for i in range(0, pat_len - 1):
        count_power = (count_power*total_char) % prime_num
    
    #Comparing pattern with each window of text (sliding over text)
    for i in range(0, text_len - pat_len + 1):

        #If hash values are equal, individual characters of pattern 
        #and current substring need to be matched
        if (pat_hash == text_hash):
            flag = True
            for j in range(0, pat_len):
                if(pattern[j] != text[i+j]):
                    flag = False
                    break
            if(flag):
                pattern_found = True
                print("Pattern found at index {0}".format(i))
                break
        
        #To calculate hash value of next substring, we remove leading character
        #and add a new character at the end of present substring
        if(i != (text_len - pat_len)):
            text_hash = (ord(text[i + pat_len]) + total_char*(text_hash - (ord(text[i])*count_power))) % prime_num

            #Due to modulo operator, we might encounter a negative hash value, 
            #which needs to be converted into positive value
            if (text_hash < 0):
                text_hash += prime_num

    if(not(pattern_found)):
        print("Given text does not contain given pattern")
    
#Taking input from user
text = input("Enter text: ")
pattern = input("Enter pattern: ")
string_search(text, pattern)
        
"""
Average Time complexity: O(pattern length + text length)
Space complexity: O(1) 

SAMPLE INPUT 1
Enter text: hello, welcome and bye
Enter pattern: and
OUTPUT
Pattern found at index 15

SAMPLE INPUT 2
Enter text: learning python python python
Enter pattern: python 
OUTPUT
Pattern found at index 9
"""