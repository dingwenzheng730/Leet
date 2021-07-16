/**
 * order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input: 
order = "cba"
str = "abcd"
Output: "cbad"
Explanation: 
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a". 
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Input: order = 'abcdef' str='bca'
Output: 'abc'

Input:
Output:

Precondition:
order.length = m
str.length = n
m >= 1
n >= 1
only lowercase letters
elements in order are unique

Postcondition:
input stay unchanged

C1: some char in order not in str
C2: Only 1 in order and str
C3: all char in order in str
class Solution {
    public String customSortString(String S, String T) {
        // count[char] = the number of occurrences of 'char' in T.
        // This is offset so that count[0] = occurrences of 'a', etc.
        // 'count' represents the current state of characters
        // (with multiplicity) we need to write to our answer.
        int[] count = new int[26];
        for (char c: T.toCharArray())
            count[c - 'a']++;

        // ans will be our final answer.  We use StringBuilder to join
        // the answer so that we more efficiently calculate a
        // concatenation of strings.
        StringBuilder ans = new StringBuilder();

        // Write all characters that occur in S, in the order of S.
        for (char c: S.toCharArray()) {
            for (int i = 0; i < count[c - 'a']; ++i)
                ans.append(c);
            // Setting count[char] to zero to denote that we do
            // not need to write 'char' into our answer anymore.
            count[c - 'a'] = 0;
        }

        // Write all remaining characters that don't occur in S.
        // That information is specified by 'count'.
        for (char c = 'a'; c <= 'z'; ++c)
            for (int i = 0; i < count[c - 'a']; ++i)
                ans.append(c);

        return ans.toString();
    }
}

Algo:
Hashmap:
build a map, mapping each word -> occurence O(n)
for each element in order, repeat according to its occurence in the map and at last put all unrelated O(mn)
Runtime: O(mn) m at most 26, so O(n)
Space: O(n)
*/

/**
 * @param {string} order
 * @param {string} s
 * @returns {string}
 */
 var customSortString = function(order, s) {
    let mapping = new Map();
    let result = '';
    for (let i=0; i < s.length; i++) {
        if (!mapping.has(s[i])) {
            mapping.set(s[i], 1);
        } else {
            mapping.set(s[i], mapping.get(s[i]) + 1);
        }
    }
    
    for (let j=0; j < order.length; j++) {
        let repeat = 0;
        
        if (mapping.has(order[j])) {
            repeat = mapping.get(order[j]);
            mapping.set(order[j], 0);
        } 
        for (let i=0; i < repeat; i++) {
            result+=order[j];
        }

    }
    
    allKeys = [...mapping.keys()];
    for (let x=0; x<allKeys.length; x++) {
        for (let k=0; k < mapping.get(allKeys[x]); k++) {
            result += allKeys[x];
        } 
    }

    return result;

};