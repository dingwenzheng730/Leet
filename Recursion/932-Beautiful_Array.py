'''
For some fixed n, an array nums is beautiful if it is a permutation of the integers 1, 2, ..., n, such that:

For every i < j, there is no k with i < k < j such that nums[k] * 2 = nums[i] + nums[j].

Given n, return any beautiful array nums.  (It is guaranteed that one exists.)

 

Example 1:

Input: n = 4
Output: [2,1,4,3]
Example 2:

Input: n = 5
Output: [3,1,2,5,4]

Precondition:
n >= 1
n always valid
recursion may overflow

Postcondition:
return an array, It is guaranteed that one exists.

C1: n = 1 return any 
C2: n = 2 return any
C3: n > 2

class Solution:
    def beautifulArray(self, N):
        memo = {1: [1]}
        def f(N):
            if N not in memo:
                odds = f((N+1)/2)
                evens = f(N/2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[N]
        return f(N)

Algo:
Divide and Conquer
Runtime: O(n)
Space: O(nlogn)
'''
class Solution:
    def beautifulArray(self, N):
        @lru_cache(None)
        def dfs(N):
            if N == 1: return [1]
            t1 = dfs((N+1)//2)
            t2 = dfs(N//2)
            return [i*2-1 for i in t1] + [i*2 for i in t2]
        
        return dfs(N)