#python program for reverse string variation.

#input  
input_str="I.love.to.contribute.in.Master-PyAlgo"

#spliting input string by the specified separator which is "."
words = input_str.split('.')

print(input_str)
#create empty list of name string
string=[]

for x in words:
    string.insert(0,x)
# join list elements with a character which is ".".
result="."
result=result.join(string)

#print result
print(result)