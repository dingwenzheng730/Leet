'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2

Input: text = 'he'
Output: 0

Input: text = 'leetcode'
Output: 0

Precondition:
n = len(text)
len(n) >= 1
English words only

Postcondition:
text unchange

C1: 0 ballon 
C2: one ballone 
C3: mult ballon
C4: n < 6

Algo:
build a map O(n)
for the map, if word has at least one, for l, o, it should have two, result + 1 O(n/6)=O(n)
return result

Runtime: O(n)
Space: O(n)
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if len(text) < 6: return 0

        count = collections.Counter(text)
        result = 0
        while count['b'] >= 1 and count['l'] >= 2 and count['o'] >= 2 and count['n'] >= 1:
            count['b'] -= 1
            count['l'] -= 2
            count['o'] -= 2
            count['n'] -= 1
            result += 1
        return result
        