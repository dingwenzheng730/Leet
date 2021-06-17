'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

Precondition: len(logs) >= 1
              len(logs[i]) >= 3
              All valid files

Input: ["dig1 5 6 3", "let1 he ha df"]
Output:["let1 he ha df", "dig1 5 6 3"]

'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def getOrderValue(nums):
            num_list = nums.split(" ", 1)
            
            identifier = num_list[0]
            content = num_list[1]

            if not content[0].isdigit():
                return (0, content, identifier)
            else:
                return (1, )
        return sorted(logs, key=getOrderValue)