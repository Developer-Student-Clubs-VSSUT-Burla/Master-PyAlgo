'''
Aim: The score of a single word is 2 if the word contains an even number of 
vowels. Otherwise, the score of this word is 1. The score for the whole list 
of words is the sum of scores of all words in the list. The aim is to output
this score for the entered string.

'''

# function to check for vowels
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u']

# function to calculate score of the string
def score_words(words):
    # initializing the score to 0
    score = 0
    for word in words:
        # initializing the number of vowels to 0
        num_vowels = 0
        for letter in word:
            # if found a vowel, increment the counter
            if is_vowel(letter):
                num_vowels += 1
        # if the total number of vowels is even, then score should increment by 2        
        if num_vowels % 2 == 0:
            score += 2
        # if the total number of vowels is odd, then score should increment by 1 
        else:
            score +=1
    # printing out the final score
    return score

# getting the total word count of the string as input
n = int(input())
# splitting the string into words
words = input().split()
# calling function to compute the score
print(score_words(words))

'''

COMPLEXITY:
	
	 Time Complexity -> O(N^2)
	 Space Complexity -> O(N)
     
Sample Input:
3
all the best

Sample Output:
3

Explanation:
Total number of words --> all, the, best [3]
vowel count in 'all' --> 1, hence, score = 1
vowel count in 'the' --> 1, hence, score = 1
vowel count in 'best' --> 1, hence, score = 1
Total score = 1 + 1 + 1 = 3.

'''