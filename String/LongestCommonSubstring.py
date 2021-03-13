#Longest Common Substring
def longestCommonSubstring(str1, str2):
    n, m = len(str1), len(str2)
    maxlen = 0
    endingIndex = 0
    dp = [[0 for x in range(m + 1)] for y in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > maxlen:
                    maxlen = dp[i][j]
                    endingIndex = i
            else:
                dp[i][j] = 0
    return str1[endingIndex - maxlen: endingIndex]

s1 = input()
s2 = input()
print(longestCommonSubstring(s1, s2))

# input:
# abcdef
# efghij
#
# output:
# ef