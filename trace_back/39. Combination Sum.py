class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(lst, start, target):
            if target == 0:
                result.append(lst.copy())
                return
            for i in range(start, len(candidates)):
                # 利用减法实现，
                if target - candidates[i] >= 0:
                    lst.append(candidates[i])
                    # Allow the current candidate to be reused (unlimited times)
                    backtrack(lst, i, target - candidates[i])
                    # 动态维护的list
                    lst.pop()

        result = []
        # candidates.sort()
        backtrack(list(), 0, target)
        return result
