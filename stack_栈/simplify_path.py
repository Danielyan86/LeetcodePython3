# 给定一个文档 (Unix-style) 的完全路径，请进行路径简化。
#
# 例如，
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack = []  # 使用栈存储目录
        path_list = [p for p in path.split("/") if p and p != "."]
        for pa in path_list:
            if pa == "..":  # 返回上一级目录则弹出
                if path_stack:
                    path_stack.pop()
            else:  # 否则入栈
                path_stack.append(pa + "/")
        return "/" + "".join(path_stack).rstrip("/")


def test_solution():
    solution = Solution()
    assert "/home" == solution.simplifyPath("/home/")
    assert "/c" == solution.simplifyPath("/a/./b/../../c/")
    assert "/" == solution.simplifyPath("/.")
    assert "/" == solution.simplifyPath("/..")


if __name__ == '__main__':
    solution = Solution()
    # res = solution.simplifyPath("/home/")

    # print(res)
    res = solution.simplifyPath("/..")
    print(res)
