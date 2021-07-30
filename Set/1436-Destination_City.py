'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"

Precondition:
n = len(paths) > 0
No cycle, result guaranteed
only one result

Postcondition:
paths unchanged
return a str:the dest

C1: n = 1 
C2: n > 1

Algo:
Hashset, two pass, go throurh to get all dest in a map
go through again, if any dest is also an origin, remove it
return the remaining dest
Runtime: O(n)
Space: O(n)
'''
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest_set = set()
        for orign, dest in paths:
            dest_set.add(dest)
        for orign, dest in paths:
            if orign in dest_set:
                dest_set.remove(orign)
        return dest_set.pop()

        # Same algo, use set operator
        # return list(set(dst for (src, dst) in paths) - set(src for (src, dst) in paths))[0]

        '''
        Simulate flight process
        myDict=defaultdict(str)
        for start,end in paths:
            myDict[start]=end
        while True:
            if myDict[end]:
                end=myDict[end]
            else:
                return end
        '''