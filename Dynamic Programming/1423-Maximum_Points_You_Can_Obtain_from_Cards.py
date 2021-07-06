'''
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Input:
Output:

Input:
Output:


Precondition:
let len(cards) = n 
n >= 1
1<= k <= n

C1: k = n
C2: n = k = 1
C3: k < n

Algo:
Brute Force: O(2^k)

Greedy: cannot guarantee optimal

DP: 
getting the max score that can be achieved with all from front
for k iteration,  try [:i] from front [i:k] from back, if the total score is bigger, update the max value
for each i, only need front_score from 0 to i and back_score from i to k so we can use a var to replace the array to store

Runtime: O(k)
Space: O(1)
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front_score = 0
        back_score = 0
        n = len(cardPoints)

        for i in range(k):
            front_score += cardPoints[i]
        
        max_score = front_score

        for i in range(k-1, -1, -1):
            back_score += cardPoints[n-(k-i)]
            front_score -= cardPoints[i]
            current_score = back_score + front_score
            max_score = max(max_score, current_score)
        return max_score