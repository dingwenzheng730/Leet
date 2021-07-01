'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Precondition: len(nums) >= 0
              No overflow of int
C1: len(nums) < 3 return []
C2: Dup answer
C3: No Dup answer
'''

class Solution:
    def twoSum(self, nums, target):
        res = []
        s = set()
        for i in range(len(nums)):
            if len(res) == 0 or res[-1][1] != nums[i]:
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
            s.add(nums[i])
        return res
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for result_set in self.twoSum(nums[i+1:], 0-nums[i]):
                    res.append([nums[i]] + result_set)
        return res

        