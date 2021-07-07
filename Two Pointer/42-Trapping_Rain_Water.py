'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Precondition:

C1: len(height) = 0
C2: len(height) = 1
C3: 

Input: [0, 1, 0, 2, 0, 1]
Output: 2
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0
        result = 0
        left = 0
        right = len(height)-1
        max_left= height[left]
        max_right = height[right]
        
        while left <= right:
            if max_left <= max_right:
                if max_left >= height[left]:
                    result += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if max_right >= height[right]:
                    result += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        return result

                
