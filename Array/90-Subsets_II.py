'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Input: nums = []
Output: []

Precondition:
n = len(nums) >= 0
only int, no overflow
may duplicate

Postcondition:
list of list: all possible subsets
should not return duplicate

C1: n = 0
C2: n = 1
C3: duplcate in result

Algo:
Brute force:
for each element, decide it is in or not in, append everything inside a set
convert set to 

sort and add it up:
when meeting duplicate, only starts adding from last subset size
O(n*2^n)
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        subsets =[[]]
        subsize = 0 

        for i in range(n):
            start_index = subsize if i >= 1 and nums[i] == nums[i-1] else 0
            subsize = len(subsets)
        
            for j in range(start_index, subsize):
                curr_set = subsets[j][:] #Copy O(n)
                curr_set.append(nums[i])
                subsets.append(curr_set)

        return subsets
        