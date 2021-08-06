import unittest
'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Precondition:
size of element in the dict: n
max length of a word: m
can have any number of '.', '.' can only be used in search
m >= 0
n >= 0
m, n won't overflow
word only in 26 lowercase english word and '.'
Add dup? allow

Postcondition:
the datastructure should be changed
addword return void
search return bool

C1: add '', search ''
C2: search return true
C3: search return false
C4: only one '.'
C5: mult '.'
C6: no '.'

Algo:
Hashmap: O(mn)
add word to trie
Runtime: O(m)
Space: O(m)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.children['#'] = True
        

    def search(self, word):
        def recur_search(w, root):
            node = root
            for i, char in enumerate(w):
                if not char in node.children:
                    if char == '.':
                        for possible in node.children:
                            if possible != '#' and recur_search(w[i+1:], node.children[possible]):
                                return True
                    return False
                else:
                    node = node.children[char]
            return '#' in node.children
        
        return recur_search(word, self.root)
        

class WordDictTest(unittest.TestCase):
    def testNoDotSuccess(self):
        word_dict = WordDictionary()
        word_dict.addWord('hi')
        result = word_dict.search('hi')
        self.assertEqual(True, result)

    def testOneDotSuccess(self):
        word_dict = WordDictionary()
        word_dict.addWord('dog')
        result = word_dict.search('d.g')
        self.assertEqual(True, result)

    def testMoreDotSuccess(self):
        word_dict = WordDictionary()
        word_dict.addWord('head')
        result = word_dict.search('h..d')
        self.assertEqual(True, result)

    def testSearchFail(self):
        word_dict = WordDictionary()
        word_dict.addWord('head')
        result = word_dict.search('h...d')
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()
