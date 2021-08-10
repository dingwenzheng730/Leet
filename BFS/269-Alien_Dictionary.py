'''
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

n: number of words in list
c: number of char in the list
u: number of unique char in list
Runtime: O(c)
Space: O(u+min(u^2, n)) or O(1)
'''

from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_dict = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})

        for first_word, second_word in zip(words, words[1:]):
            for first_char, second_char in zip(first_word, second_word):
                if first_char != second_char:
                    if second_word not in adj_dict[first_char]:
                        adj_dict[first_char].add(second_char)
                        in_degree[second_char] += 1
                    break
            else:
                if len(second_word) < len(first_word): return ''

        result = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            ch1 = queue.popleft()
            result.append(ch1)
            for ch2 in adj_dict[ch1]:
                in_degree -= 1
                if in_degree[ch2] == 0:
                    queue.append(ch2)
        
        if len(result) < len(in_degree):
            return ''
        return ''.join(result)


        