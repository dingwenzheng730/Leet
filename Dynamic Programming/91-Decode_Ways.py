'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Input: s = "5"
Output: 1

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Precondition:
n = len(s)
n >= 1

Postcondition:
s stay unchanged
result > 0

C1: n = 1
C2: n = 2
C3: n >= 3
C4: contains 0

Algo:
DP:
Definition: dp[i] = number of combinations with s[:i]
Base Case: dp[0] = 1
           dp[1] = 1 if s[0] not 0
RR: dp[i+1] is determined only by dp[i] and dp[i-1]
Result: dp[n]

Runtime: O(n)
Space: O(n)
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(1, n):
            if s[i] != '0':
                dp[i+1] = dp[i]
            if s[i-1] == '1':
                dp[i+1] = dp[i+1] + dp[i-1]
            elif s[i-1] == '2' and int(s[i]) <= 6:
                dp[i+1] = dp[i+1] + dp[i-1]
        return dp[n]
