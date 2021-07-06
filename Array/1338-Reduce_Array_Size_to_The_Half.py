import collections
import math
'''
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.

Input: [1, 2]
Output: 1

Input: [7,7,7,7,7,7]
Output: 1

Precondition:
len(arr) = n
n >= 1
n is even

C1: min num of element
C2: General
C4: All same elements

Algo:
Greedy(Sort): 
build dict of freq O(n)
Sort by freq O(nlogn)
keep pushing element and stop when the remaining size < half O(n)

Greedy(Heap): No imporvment 

Bucket Sort:
Observation: We only care about number of freq, and don't care about what numbers are for this freq
Same as sorting greedy but with bucket sort
largest occurance: m
Runtime: O(m+n), here O(n)
Space: O(m)

'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counts = collections.Counter(arr)
        max_value = max(counts.values())
        
        buckets = [0] * (max_value + 1)

        for count in counts.values():
            buckets[count] += 1

        set_size = 0
        to_remove_size = n // 2
        bucket = max_value
        while to_remove_size > 0:
            max_needed_from_bucket = math.ceil(to_remove_size / bucket)
            set_increase = min(buckets[bucket], max_needed_from_bucket)
            set_size += set_increase
            to_remove_size -= set_increase * bucket
            bucket -= 1

        return set_size
