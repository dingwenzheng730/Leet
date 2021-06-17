'''
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Precondition: Valid
              n >= 1
              len(edges) >= 1

Input: [[0,1][1,2][3,4]]
Output: 2

'''
class Solution:
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        total_count = 0
        visited = [0 for i in range(n)]
        mapping = defaultdict(list)
        
        def dfs(node):
            visited[node] = 1
            for v in mapping[node]:
                if visited[v] == 0:
                    dfs(v) 
                    
        for edge in edges:
            mapping[edge[0]].append(edge[1])
            mapping[edge[1]].append(edge[0])
            
        for x in range(len(visited)):
            if visited[x] == 0:
                total_count += 1
                dfs(x)
        return total_count