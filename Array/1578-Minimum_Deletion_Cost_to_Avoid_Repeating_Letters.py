'''
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Input: s = 'a' cost = [72]
Output: 0

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.

Precondition: 
len(s) = len(cost) = n
n >= 1

C1: only 1 reuturn 0 
C2: need remove
C3: No need remove

Two pointer:
for each letter, while next one is equal, add to a list, update max cost for this letter
when hitting end of all words or next word is not equal,
cost + sum of the list, minus the max cost

Runtime: O(n)
Space: O(1)
'''

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        ans = 0
        left = 0
        while left < n:
            right = left + 1
            while right < n and s[left] == s[right]:
                right += 1     
            if right == n:
                costs = cost[left:]
            else:
                costs = cost[left:right]
                    
            maxCost = max(costs)    
            ans += sum(costs) - maxCost
                
            left = right
            
        return ans
        