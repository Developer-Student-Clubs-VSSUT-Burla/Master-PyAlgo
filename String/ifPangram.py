#[Solution] - program to check if given string is pangram or not #59

import string 
def check_pangram(strChk): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
    	if char not in strChk.lower(): 
    		return False
    return True

strChk = input('String : ')
if(check_pangram(strChk) == True): 
	print("The String is a Pangram .") 
else: 
	print("The String is not a Pangram .")
