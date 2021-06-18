'''
There are n cities numbered from 1 to n.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

Precondition: negative weight? No
n >= 1
connections unique connections
always can connect? -1 

C1: n = 1 return 0
C2: no connection strategy return -1

Input: 3 [[1,2,10], [1,3,3], [2,3,4]]
Output: 7

MST 
sort edges by weights,
pick edge and connect
when all nodes connected, stop
DSU 
'''
class DSU():
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.rank = [1 for _ in range(n+1)]

    def find(self, node):
        while node != self.parents[node]:
            node = self.parents[node]
        return node


    def union(self, city1, city2):
        root1 = self.find(city1)
        root2 = self.find(city2)

        if root1 == root2:
            return

        if self.rank[root1] > self.rank[root2]:
            self.parents[root2] = root1
            self.rank[root1] += self.rank[root2]
        else:
            self.parents[root1] = root2
            self.rank[root2] += self.rank[root1]
        

    def isconnected(self, city1, city2):
        return self.find(city1) == self.find(city2)


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        cost = 0

        dsu = DSU(n)
        connections.sort(key=lambda x:x[2])
        for connect in connections:
            city1 = connect[0]
            city2 = connect[1]
            if not dsu.isconnected(city1, city2):
                dsu.union(city1, city2)
                cost += connect[2]
                count += 1
        if n = 1:
            return 0
        if count == n-1:
            return cost
        return -1