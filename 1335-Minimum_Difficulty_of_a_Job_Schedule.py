'''
You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the i-th job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done in that day.

Given an array of integers jobDifficulty and an integer d. The difficulty of the i-th job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

Precondition: days >= 1, len(jobs) >= 1, jobs[i] >= 0
len(jobs) = n                          
days = d

Input: [1,2,3,4,5] d = 3
Output: 1 + 4 + 5 = 10

C1: days > len(jobs) return -1

Brute force:
for each d, try each index O(n^d)

DP:
dp[n, k]: The min diff can be achieved with length n from begining, in k days 
Solution: dp[n, k]
dp[n, k] = min for (dp[j, k-1] + max for j in range(j, n))
dp[0, 0] = 0
'''

class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d or not jobDifficulty or d == 0:
            return -1

        n = len(jobDifficulty)

        maxInRange = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): maxInRange[i][i] = jobDifficulty[i]
        for l in range(2, n+1):
            for i in range(n):
                j = i+l-1
                if j>=n: continue
                maxInRange[i][j] = max(maxInRange[i+1][j-1], jobDifficulty[i], jobDifficulty[j])

        dp = [[math.inf for _ in range(d+1)] for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, min(i+1, d+1)):
                for k in range(j, i+1):
                    dp[i][j] = min(dp[i][j], dp[k-1][j-1] + maxInRange[k-1][i-1])
        return dp[n][d]
