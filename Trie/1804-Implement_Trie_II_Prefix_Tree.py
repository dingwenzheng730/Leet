import unittest
'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the string prefix as a prefix.
void erase(String word) Erases the string word from the trie.
 

Example 1:

Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]

Precondition:
m = max length of word
n = number of words
m >= 0
n >= 0
Only lowercase letter
m, n won't overflow
insert duplicate? Allow and will increase that word frenquency

Postcondition:
Trie changes in place
init return none
countwordsequalto return number of equals, can be >= 0
countwordstartingwith return number of statingwith, can be >= 0
erase will return none, if word not in, nothing happens

C1: insert dup
C2: insert new
C3: count word return 0
C4: count word return 1
C5: count word return > 1
C6: count prefix return non 0
C7: count prefix return 1
C8: count prefix return > 1
C9: erase successfully, totally erase
C10: erase successfully, partly erase
C11: erase unsuccessfully
C12: starts with ''
C13: equals ''
C14: Insert after delete

Algo:
Trie, with an addition filed count to identify how many times it has appeared, 
and a word_count to identify the number of whole words

Runtime: 
init: O(1)
insert: O(m)
equal: O(m)
starts: O(m)
erase: O(m)

Space: O(mn)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.word_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.word_count += 1

    def countWordsEqualTo(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
            if not node.count > 0:
                return 0
        return node.word_count
    
    def countWordsStartingWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
            if not node.count > 0:
                return 0
        
        return node.count
    
    def erase(self, word):
        if not self.countWordsEqualTo(word) > 0:
            return 
        node = self.root
        for char in word: 
            node = node.children[char]
            node.count -= 1
        node.word_count -= 1

class TrieTest(unittest.TestCase):
    def test_count_equal_zero(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('apple')
        result = trie.countWordsEqualTo('app')
        self.assertEqual(0, result)

    def test_count_equal_one(self):
        trie = Trie()
        trie.insert('apple')
        result = trie.countWordsEqualTo('apple')
        self.assertEqual(1, result)

    def test_count_equal_bigger(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('apple')
        result = trie.countWordsEqualTo('apple')
        self.assertEqual(2, result)

    def test_count_starts_zero(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('apple')
        result = trie.countWordsStartingWith('bba')
        self.assertEqual(0, result)

    def test_count_starts_one(self):
        trie = Trie()
        trie.insert('apple')
        result = trie.countWordsStartingWith('app')
        self.assertEqual(1, result)

    def test_count_starts_bigger(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('apple')
        result = trie.countWordsStartingWith('app')
        self.assertEqual(2, result)

    def test_erase_fail(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('apple')
        trie.erase('app')
        result = trie.countWordsStartingWith('app')
        self.assertEqual(2, result)

    def test_erase_partly(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('apple')
        trie.erase('apple')
        result = trie.countWordsEqualTo('apple')
        self.assertEqual(1, result)

    def test_erase_complete(self):
        trie = Trie()
        trie.insert('apple')
        trie.insert('apple')
        trie.erase('apple')
        trie.erase('apple')
        result = trie.countWordsStartingWith('app')
        self.assertEqual(0, result)
        
    def test_insert_after_delete(self):
        trie = Trie()
        trie.insert('apple')
        trie.erase('apple')
        trie.insert('apple')
        result = trie.countWordsStartingWith('app')
        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()
