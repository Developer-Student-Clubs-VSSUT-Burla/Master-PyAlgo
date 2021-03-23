# Function to get trailing zeroes
def trailingZeroes(number):
    #initialise to 0
    rem = 0
    # Till Number is graeter than zero loop will execute
    while number > 0:
        # keep diving by 5
        number //= 5
        # add to rem
        rem += number
    # rem has the answer
    return rem
    
    
# taking input
number = int(input('Enter Number for calculating trailing Zeroes : '))
    
# gtting the solution
solution = trailingZeroes(number)

# printing to console
print(solution)


# Input: number = 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.

# Input: number = 5
# Output: 1
# Explanation: 5! = 120
