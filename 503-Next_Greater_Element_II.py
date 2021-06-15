'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        input: [1,2,3,4,5,6]
        output: [2,3,4,5,6,-1]

        input: [6,2,3,5,4]
        output: [-1, 3, 5, 6, 6]
        
        C1: len(nums) == 0: return []
        C2: len(nums) == 1: return [-1]

        Brute Force: O(n^2)

        '''

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [-1]
        
        n = len(nums)
        result = [-1 for _ in range(n)]
        stack = []
        i = 2*n -1
        while i >= 0:
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if not stack:
                result[i%n] = -1
            else:
                result[i%n] = stack[-1]
            stack.append(nums[i%n])
            i -=1
            
        return result