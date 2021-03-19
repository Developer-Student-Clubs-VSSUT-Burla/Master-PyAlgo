#In this file there is a ATM question brief intro

#Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5(read next line)
#and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges)   ---(read next)
#For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.
#Input
#Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

#Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

#Output
#Output the account balance after the attempted transaction, given as a number with two digits of precision.
#If there is not enough money in the account to complete the transaction, output the current bank balance.


#-------------------------------------------------------------------------------------------------------------------------------------




# let's dive into the question......

#   WAY OF APPROACH: 1) read the question (twice)
# 2) Give a explanation to yourself so that the question will be crystal clear
# 3) Note where are some exceptions in the questions
# 4) write the code what you understood rather than directly entering to answer




# first line : There's one girl , she want to withdraw some money ((money = "X" $US)) . Here , X must be a multiple of "5" . X can be
#  5 10 15 ..............2000 . As, the limit of x is upto 2000 .
# second line : The girl is having enough money for the withdrawal including bank charges . In the next let's see what exactly is charges
# third line : For each successful withdrawal the bank charges 0.50 $US . Tru to understand as it is very important in the code
# So , the bank charges will be deducted if and only if there is a successful withdrawal i.e., if x is a multiple of 5 .

# let's see some inputs and outputs :
# Example - Successful Transaction
# Input:
# 30 120.00

# Output:
# 89.50

# Example - Incorrect Withdrawal Amount (not multiple of 5)
# Input:
# 42 120.00
#
# Output:
# 120.00

#Example - Insufficient Funds
#Input:
#300 120.00

#Output:
#120.00



#CODE  :

# The code is very simple as we read the method of approach

# The first thing is first taking input as the python follows indentation be careful.
# while taking input we use input() function .

a,b=input().split()  # Here I used a as 'x' and b as 'y' . 'a' stand for money and 'y' stands for how much balance does pooja have
a=int(a) #Here the 'a' value is int if we observe the examples clearly we can understand
b=float(b) # But the  'b' value is float why? because in the 'OUTPUT' it's mentioned that 'y' is of float type with two digits precision
if a%5==0 and a+0.50<=b: # for finding remaining balance
    rem_bal=b-a-0.50
    print('%.2f'%rem_bal)
else:
    print('%.2f'%b) # while printing the output use two digit precision even if you are printing b in the else part.


#NOTE : Some points to think of while writing the code is , as python follows indentation while taking input and while writing code ,
# just be sure to write .spilt() function .The function .split() takes same line next input i.e., 1 2 in this way . If you do not
# mention then while passing test cases code shows error . so as to overcome this situation use spilt() . Anyway for clarification
# use with .split() and normally i.e., a=int(input()) b=float(input()) then you can understand inmportance of the function.