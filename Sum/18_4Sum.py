'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Input: nums = [1,2,3,4], target = 10
Output: [[0,1,2,3]]

Precondition: 
Result exists? No
len(nums) >= 1
a,b,c,d distinct

C1: len(nums) < 4 return []
C2: len(nums) = 4 and match
C3: len(nums) = 4 and no match
C4: len(nums) > 4 no match
C5: len(nunms) > 4 match

Brute Force:
loop over loop, try a, b, c, d for all possible index
Runtime: O(n^4)

Hashmap:
Two sum of two sum
Runtime: O(n^3)
Space: O(n)

'''
class Solution:
    def kSum(self, nums, target, k):
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return []
        if k == 2:
            return self.twoSum(nums, target)
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for result_set in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + result_set)
        return res

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        s = set()
        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)