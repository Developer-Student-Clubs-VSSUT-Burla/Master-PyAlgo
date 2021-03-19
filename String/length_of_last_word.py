
def length_last_word(A):
    arr = A.split(' ')
    size = len(arr)
    if(size == 1):
        return len(A)

    last_word = arr[-1]
    return last_word


string = input("Enter the string : ")
# Printing the length
print(len(length_last_word(string)))
