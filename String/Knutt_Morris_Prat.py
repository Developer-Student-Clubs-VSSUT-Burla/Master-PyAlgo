'''
The Knuth–Morris–Pratt string-searching algorithm searches for occurrences of a "word" W within a main "text string" S
by employing the observation that when a mismatch occurs, 
the word itself embodies sufficient information to determine where the next match could begin.
''' 
def calculateLps(pattern, lps):
    length = 0
    lps[0] = 0

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def KMPSearch(pattern, text):
    sizePattern = len(pattern)
    sizeText = len(text)

    lps = [0] * sizePattern
    j = 0

    calculateLps(pattern, lps)

    i = 0
    while i < sizeText:
        if pattern[j] == text[i]:
            i+=1
            j+=1

        if j == sizePattern:
            print("Pattern found at " + str(i - j + 1))
            j = lps[j - 1]
        elif i < sizeText and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

text = input("Enter the text:")
pattern = input("Enter the pattern to find:")
KMPSearch(pattern, text)

'''
Sample Output
Enter the text:somnomtomlomgomkomhomlomgomlom
Enter the pattern to find:lom
Pattern found at 10
Pattern found at 22
Pattern found at 28

'''

