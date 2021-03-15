Reverse String Variation

This have some twist in it. we have to Reverse string word by word taken in positive order.

exapmle:
 INPUT: "I.LOVE.OPEN.SOURCE."

 OUTPUT: "SOURCE.OPEN.LOVE.I"

here what we have to  Reverse this string such string meaning remain same if we read it from right to left side after the ouput.
 it sounds same with our input.

SOLUTION: solution of this question can easily done by two methods of python (split and join).
here is our input
input_str="I.love.to.contribute.in.Master-PyAlgo"

WE use split method for spliting every element of string by separator given is('.')
words = input_str.split('.')
it actually returns a list of strings after breaking the given string by the specified separator which is ('.').
after this our words list look like this :

['I', 'love', 'to', 'contribute', 'in', 'Master-PyAlgo']

print(input_str)

here we create empty list which name is string.
string=[]

In this loop we actually use insert method of python which usually use in list.
but the main thing is we insert every element from end of words list. so what we do here
insert(0,x) means it insert first element of words list in string list and move on the after
it insert second element of words list and at 0 place so first element which is inserted before 
moves to right.
and then this loop work.
for x in words:
    string.insert(0,x)

here is string after this loop

['Master-PyAlgo', 'in', 'contribute', 'to', 'love', 'I']

Now we have to add "." by after all element of string list .
we use join function .
 the use of join function to join list elements with a character and here character is '.'. 

joins elements of string list by '.' and stores in sting result 
result="."
result=result.join(string)
print(result)

final OUTPUT
Master-PyAlgo.in.contribute.to.love.I