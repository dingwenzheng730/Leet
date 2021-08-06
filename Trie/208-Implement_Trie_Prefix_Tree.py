import unittest
'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

>>> trie1 = Trie()
>>> trie1.insert('apple')
>>> trie1.insert('apple')
>>> trie1.insert('banana')
>>> trie1.search('apple')
True
>>> trie1.startsWtih('app')
True
>>> trie.startsWith()



Precondition:
m = max length of word
n = word in trie
only lowercase english words
suppose size won't overflow
insert duplicate? nothing happens
insert ''? nothing
Search ''? if it is in, true
startsWith ''? True

Postcondition:
the Tire changes
insert->void
search->bool
startswith->bool

C1: insert duplicate
C2: insert new
C3: insert ''
C4: search in
C5: search not in
C6: starts with
C7: starts not with

Algo:
dict of dict
tail of dict is '#'
Runtime:
init: O(1)
insert: O(m)
search: O(m)
startsWith: O(m)

Space: O(mn)
'''
class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.children['#'] = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return '#' in node.children
    
    def startsWith(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class TestTrie(unittest.TestCase):
    def test_search_success(self):
        trie = Trie()
        trie.insert('apple')
        result = trie.search('apple')
        self.assertEqual(result, True)

    def test_startsWith_success(self):
        trie = Trie()
        trie.insert('apple')
        result = trie.startsWith('app')
        self.assertEqual(result, True)

    def test_search_fail(self):
        trie = Trie()
        trie.insert('bangaga')
        result = trie.search('apple')
        self.assertEqual(result, False)

    def test_startsWith_fail(self):
        trie = Trie()
        trie.insert('bangaga')
        result = trie.startsWith('app')
        self.assertEqual(result, False)

    def test_empty_search_success(self):
        trie = Trie()
        trie.insert('')
        result = trie.search('')
        self.assertEqual(result, True)

    def test_empty_search_fail(self):
        trie = Trie()
        trie.insert('hi')
        result = trie.search('')
        self.assertEqual(result, False)
    
    def test_startsWith_empty(self):
        trie = Trie()
        trie.insert('bangaga')
        result = trie.startsWith('')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
        
