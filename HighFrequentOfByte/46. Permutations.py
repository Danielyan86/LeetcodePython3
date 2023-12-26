# 正向思维，从0个元素开始加，这种方法最容写，没有格外多余的步骤，也符合人的排序思维
# 一开始就通过for循环分成了n叉树
# 在每一个子树里面遍历全局的列表，如果元素已经存在了，则跳过
# 最后每个子树列表长度和传入列表一样的时候表示已经遍历了，加入结果res即可
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def traceback(lst):
            if len(lst) == len(nums):
                res.append(lst)
                return
            for n in nums:
                if n not in lst:
                    traceback(lst + [n])

        res = []
        traceback([])
        return res
