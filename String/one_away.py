""" This program is written to check if a String can be modified into another String by only one single operation that can be
1. replacement
2. delete
3. insert
"""
def is_Edit_Distance_One(string_1, string_2):                                 #Defination of the function
    String_1_length = len(string_1)                                           # Check the length of both the Strings
    String_2_length = len(string_2)

    if abs(String_1_length - String_2_length) > 1:                            #If length difference is greater than 1 this program holds invalid
        return False

    count = 0
    i = 0
    j = 0
    while i < String_1_length and j < String_2_length:                       #intialize the loop

        if string_1[i] != string_2[j]:                                       # if any charachter diffrents at a particular postion then increment count and  assign false
            if count == 1:
                return False

            if String_1_length > String_2_length:                           #if 1st string is greater than incremment i
                i += 1
            elif String_2_length < String_1_length:                         #else string2 is greater than increment j
                j += 1
            else:                                                            #length equal of the string1 and string2
                i += 1
                j += 1

            count += 1

        else:
            i += 1
            j += 1

    if i < String_1_length or j < String_2_length:                         #If we dont traverse the end of the string1 or string2 then incremment count
        count += 1

    return count == 1


string_1 = input("Enter the 1st String: ")
string_2 = input("Enter the 2nd String: ")
if is_Edit_Distance_One(string_1, string_2):
    print("It is possible to modify the array by one operation")
else:
    print("It is not possible to modify the array by one operation")

"""
Enter the 1st String: abc
Enter the 1st String: adc
Output: It is possible to modify the array by one operation

Enter the 1st String: pale
Enter the 1st String: palww
Output: It is not possible to modify the array by one operation


"""
