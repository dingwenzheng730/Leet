'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

Precondition:
only ASCII 
m = len(s) >= 1
n = len(words) >= 1
k = len(words[i]) >= 1

Postcondition:
words stay unchanged
return int: number of subsequence

C1: return 0
C2: return > 0

Algo:
Brute Force:
for each word in words, try each char
O(nm + total length of words)

Build a dict, mapping from char -> list of (origin word,fullfilled number of char)
go through s, for each char ,update the dict, if  fullfilled >= len(word), add one to result

Runtime: O(n) + total length of words
Runtime: O(total length of words)
'''
class Solution(object):
    def numMatchingSubseq(self, s, words):
        waiting_dict=defaultdict(list)
        for word in words:
            waiting_dict[word[0]].append((word,0))

        result = 0
        for char in s:
            temp_list=waiting_dict[char]
            waiting_dict[char]=list()
            while temp_list:
                word,pos=temp_list.pop()
                pos+=1
                if pos>=len(word): result+=1
                else: waiting_dict[word[pos]].append((word,pos))
                    
        return result