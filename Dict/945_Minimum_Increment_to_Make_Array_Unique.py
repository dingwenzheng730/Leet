'''
Given an array of integers nums, a move consists of choosing any nums[i], and incrementing it by 1.

Return the least number of moves to make every value in nums unique.

Example 1:

Input: nums = [1,2,2,3]
Output: 2
Explanation:  After 1 move, the array could be [1, 2, 3].

Precondition:
no int overflow
n = len(nums)
40000 > n >= 0
40000 > nums[i] >= 0

Postcondition:
nums stay unchanged
return min move number

C1: n=0
C2: n=1
C3: no steps required
C4: no repeat adding for one number
C5: repeating adding for one number

Algo:
Bucket:
build a dict for num -> count for all possible num
go through all num, when seeing a duplicate num, put it inside a list
when seeing the first available value, pop one from dup nums, add the difference to result
Runtime: O(n)
Space: O(n)
'''
class Solution:
    MAX_POSSIBLE = 90000
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        taken = []

        result = 0
        for i in range(Solution.MAX_POSSIBLE):
            if count[i] >= 2:
                taken.extend([i]*(count[i]-1))
            elif taken and count[i] == 0:
                result += i - taken.pop()
        return result