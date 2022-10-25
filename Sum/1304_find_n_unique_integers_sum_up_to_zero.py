'''
Input: int n, 1 <= n <= 100
Output: list of int

General Cases:
input: 1 -> 0 
input: odd -> 0, 1...floor(n/2), -1...-floor(n/2)
input: even -> 0,1...floor(n/2), -1...floor(n/2)

Precondition: 1 <= n <= 100
Postcondition: output sum to be 0

Algo: just find a easy way to generate one possible way
deal with n = 1, odd or even

Test Cases
n = 1
n = 2
n = 3
n = 5
'''
class Solution(object):
    def sumZero(self, n):
        if n == 1:
            return [0]
        if n % 2 == 0:
            result = []
            for i in range(1, n/2+1):
                result.append(-1*i)
                result.append(i)
            return result
        if n % 2 != 0:
            result = [0]
            for i in range(1, int(n/2)+1):
                result.append(-1*i)
                result.append(i)
            return result


