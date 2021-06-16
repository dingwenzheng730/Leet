'''
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15

C1: days = 0  impossible
C2: len(weights) = 0 impossible
C3: days > len(weights) -> max of weight of prodcuts

Brute Force: starting from max weight of products, add 1 everytime and see if the shipping days = days
O((sum-max)*n) n = len(weights)

Trick: Binary Search O(n*log(sum-max))

DP: Nope
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        n = len(weights)

        result = math.inf
        while start <= end:
            mid = start + (end - start) // 2
            if self.is_valid(weights, days, mid):
                result = mid
                end = mid - 1
            else:
                start = mid + 1
        return result
    
    def is_valid(self, weights, days, capacity):
        day = 1
        curr_total = 0
        n = len(weights)
        for i in range(n):
            curr_total += weights[i]
            if curr_total > capacity:
                day+=1
                curr_total = weights[i]
        if day <= days:
            return True
        return False
