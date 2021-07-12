'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false

Input: s='a', t='b'
Output: True

Input: s="badc", t="baba"
Output: False

Precondition:
len(s) = m
len(t) = n
m = n >= 1
only english words

Postcondition:
words stay unchanged

C1: only 1 char, True
C2: True
C3: s has dup mapping
C4: t has dup mapping

Algo:
create a mapping
for each index, 
if s[i] not in the mapping
assign mapping[s[i]] = t[i]
if s[i] in the mapping and t[i] is not this value, return False
do the same thing for t[i]
return True
Runtime: O(n)
Space: O(1), Since the size of ASCII char set is fixed

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mapping1 = {}
        mapping2 = {}
        for i in range(n):
            if s[i] not in mapping1:
                mapping1[s[i]] = t[i]
            else:
                if t[i] != mapping1[s[i]]:
                    return False
            if t[i] not in mapping2:
                mapping2[t[i]] = s[i]
            else:
                if s[i] != mapping2[t[i]]:
                    return False
        return True