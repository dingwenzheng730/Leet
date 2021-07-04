'''
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

Precondition:
len(roads) >= 0
n >= 2

C1: len(roads) = 0 return 0
C2: General 

Go over roads to build all neighbor list for each city, O(n)
for each pair, calculate the rank for these two cities with above array O(n^2)
return thx max 

# O(1) for compute val 
def compute_val(city1, city2, set1, set2):
    if city1 in set2: # it is equalivent to city2 in lst1 
        return len(set1)+len(set2)-1
    else:
        return len(set1)+len(set2)

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # edge case 
        if len(roads) == 0:
            return 0 
        
        # parse roads list to dict
        # key: value = city: set of neighboring cities 
        d = {}
        for city1, city2 in roads:
            if not (city1 in d):
                d[city1] = set() 
            if not (city2 in d):
                d[city2] = set() 
                
            d[city1].add(city2)
            d[city2].add(city1)
        
        # sorted the dictionary by num. of neighbors => enable us to perform early-stop 
        sorted_lst = sorted(d.items(), key=lambda x:len(x[1]), reverse=True) # O(n*log(n))
        
        max_val = float('-inf')
        for i, (city1, set1) in enumerate(sorted_lst):
            for j in range(i+1, len(sorted_lst)):
                city2, set2 = sorted_lst[j]
                val = compute_val(city1, city2, set1, set2)
                max_val = max(max_val, val)
                
                # early stop 
                # if we are equal to max_val, we may get max_val+1 due to double-count
                # but if we are <= max_val, we will not able to be better than max_val 
                if val <= max_val-1:
                    break 
                
        return max_val 

'''
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) == 0:
            return 0
        
        edge_count = [0]*n
        connected = set()
        
        for road in roads:
            edge_count[road[0]] += 1
            edge_count[road[1]] += 1
            connected.add((road[0],road[1]))
            connected.add((road[1],road[0]))
        
        max_rank = 0
        for i in range(n):
            for j in range(i+1,n):
                if (i,j) in connected:
                    max_rank = max(max_rank,edge_count[i]+edge_count[j]-1)
                else:
                    max_rank = max(max_rank,edge_count[i]+edge_count[j])
                    
        return max_rank
