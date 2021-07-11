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

In addition to the mapping above, an encoded message may contain the '*' character, which can represent any digit from '1' to '9' ('0' is excluded). For example, the encoded message "1*" may represent any of the encoded messages "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.

Given a string s containing digits and the '*' character, return the number of ways to decode it.

Since the answer may be very large, return it modulo 10^9 + 7.

Input: s = "*"
Output: 9
Explanation: The encoded message can represent any of the encoded messages "1", "2", "3", "4", "5", "6", "7", "8", or "9".
Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G", "H", and "I" respectively.
Hence, there are a total of 9 ways to decode "*".

Input: s = "2*"
Output: 15
Explanation: The encoded message can represent any of the encoded messages "21", "22", "23", "24", "25", "26", "27", "28", or "29".
"21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27", "28", and "29" only have 1 way.
Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".

Input: *10
Output: 9 

Precondition: 
n = len(s)
n >= 1
always contains *
All valid input

Postcondition:
s stay unchanged

C1: only *
C2: one *
C3: Mult *
C4: With 0
C5: With 1
C6: With 2

Algo:
DP:
Definition: dp[i] = the number of combinations that can be achieved with s[:i]
Base Case : dp[0] = 1
RR: dp[i+1] is determined by dp[i] and dp[i-1]
result: dp[n]
Runtime: O(n)
Space: O(n)
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        m = 10**9 + 7
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        if s[0] == '*':
            dp[1] = 9
        elif s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        
        for i in range(1, n):
            if s[i] == '*':
                dp[i+1] = 9 * dp[i] % m
                if s[i-1] == '1':
                    dp[i+1] = (dp[i+1] + 9 * dp[i-1]) % m
                elif s[i-1] == '2':
                    dp[i+1] = (dp[i+1] + 6 * dp[i-1]) % m
                elif s[i-1] == '*':
                    dp[i+1] = (dp[i+1] + 15 * dp[i-1]) % m
            else:
                dp[i+1] = dp[i] if s[i] != '0' else 0 
                
                if s[i-1] == '1':
                    dp[i+1] = (dp[i+1] + dp[i-1]) % m
                elif s[i-1] == '2' and int(s[i]) <= 6:
                    dp[i+1] = (dp[i+1] + dp[i-1]) % m
                elif s[i-1] == '*':
                    dp[i+1] = (dp[i+1] + dp[i-1] * (2 if int(s[i]) <= 6 else 1)) % m
        return dp[n]
                
                  

        