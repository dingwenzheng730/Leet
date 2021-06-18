'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Precondition: len(nums) >= 1

C1: len(nums) = 1 return [0]
C2: len(nums) = 0 imposs
C3: len(nums) > 1

Input: [1, 3, 2, 4]
Output: [1, 1, 0, 0]

merge_sort, record time of swap
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [[nums[i], i] for i in range(n)]
        result = [0] * n
        
        def new_merge_sort(arr, left, right):
            if right - left <= 1:
                return 
            mid = (left+right)//2
            new_merge_sort(arr, left, mid)
            new_merge_sort(arr, mid, right)
            merge(arr, left, right, mid)
            
        def merge(arr, left, right, mid):
            i = left
            j = mid
            temp = []
            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    result[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i < mid:
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1
            while j < right:
                temp.append(arr[j])
                j += 1
            for i in range(left, right):
                arr[i] = temp[i - left]
        new_merge_sort(arr, 0, n)
        
        return result