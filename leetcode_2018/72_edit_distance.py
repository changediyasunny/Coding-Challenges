"""
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Running time: O(mn)
Space: O(mn)



The idea would be to reduce the problem to simple ones. For example, there are two words,
"horse" and "ros" and we want to compute an edit distance D for them. One could notice
that it seems to be more simple for short words and so it would be logical to relate
an edit distance D[n][m] with the lengths n and m of input words.

Let's go further and introduce an edit distance D[i][j] which is an edit distance
between the first i characters of word1 and the first j characters of word2.

It turns out that one could compute D[i][j], knowing D[i - 1][j], D[i][j - 1] and D[i - 1][j - 1].
If the last character is the same, i.e. word1[i] = word2[j] the
>> D[i][j] = 1 + min(D[i−1][j],D[i][j−1],D[i−1][j−1]−1)
and if not, i.e. word1[i] != word2[j] we have to take into account the replacement of the last character during the conversion.
>> D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])

"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) # horse
        n = len(word2) # ros

        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        # compute
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]
