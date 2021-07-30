'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Input: Input: nums = [5], k = 1
Output: 0

Input: Input: nums = [5,6,5], k = 0
Output: 1

Precondition:
No int overflow
n=len(nums)
n >= 0
k >= 0

Postcondition:
nums unchanged
return num of unique k pairs

C1: result = 0
C2: n = 0
C3: n = 1
C4: mult large one
C5: mult small one
C6: k = 0

Algo:
Brute Force: 
try each pair
O(n^2)

Sort and two pointer
O(nlogn)

Hashmap two pass:
init a seen pair set
first get map: k+num -> i
second if num = k+num and j != i, and the pair not in seen, append (nums[i],nums[j])

Runtime: O(n)
Space: O(n)

'''
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mapping = {}
        seen = set([])
        for i in range(n):
            mapping[nums[i]+k] = i

        for j in range(n):
            if nums[j] in mapping:
                i = mapping[nums[j]]
                if i != j and (max(nums[i], nums[j]), min(nums[i], nums[j])) not in seen:
                    seen.add((max(nums[i], nums[j]), min(nums[i], nums[j])))
        return len(seen)

        