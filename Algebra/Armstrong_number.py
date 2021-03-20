#Program to check if the user entered number is an Armstrong number or not


num = int(input("Enter a number: "))
sum = 0
# Changed num variable to string and calculated the length (number of digits)
order = len(str(num))
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")



#Input: 153
#Output: 153 is an Armstrong number
#Input: 8208
#Output: 8208 is an Armstrong number
#Input: 567
#Output: 567 is not an Armstrong number

#Time Complexity: O(log(n))
#Space Complexity: O(1)