'''
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Precondition:
all lower case engword
word in worddict
len(worddict) >= 2
len(word) >= 1
word1 != word2

C1: worddict only contains 2
C2: single match
C3: mult match
class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        int i1 = -1, i2 = -1;
        int minDistance = words.length;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(word1)) {
                i1 = i;
            } else if (words[i].equals(word2)) {
                i2 = i;
            }

            if (i1 != -1 && i2 != -1) {
                minDistance = Math.min(minDistance, Math.abs(i1 - i2));
            }
        }
        return minDistance;
    }
}
'''
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1, i2 = -1, -1
        min_distance = len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                i1 = i 
            elif wordsDict[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                min_distance = min(min_distance, abs(i1-i2))
        return min_distance

        