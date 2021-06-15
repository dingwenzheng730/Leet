class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        C1: [] -> []
        C2: [neg] -> return original
        '''
        ans = []
        for aster in asteroids:
            while ans and ans[-1] > 0 and aster < 0:
                if abs(aster) > ans[-1]:
                    ans.pop()
                    continue
                elif abs(aster) == ans[-1]:
                    ans.pop()
                break
            else:
                ans.append(aster)

        return ans

