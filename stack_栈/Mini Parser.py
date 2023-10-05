# 给定一个用字符串表示的整数的嵌套列表，实现一个解析它的语法分析器。
#
# 列表中的每个元素只可能是整数或整数嵌套列表
#
# 提示：你可以假定这些字符串都是格式良好的：
#
# 字符串非空
# 字符串不包含空格
# 字符串只包含数字0-9, [, - ,, ]


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return []
        left_list = [l_item for l_item in s.split("[")]
        right_list = [r_item for r_item in left_list.pop().split("]")]
        num_list = [int(item) for item in right_list[0].split(",") if item]
        del right_list[0]
        while left_list:
            l_num_str = left_list.pop()
            l_temp_list = [int(item) for item in l_num_str.split(",") if item]
            l_temp_list.append(num_list)
            num_list = l_temp_list + [
                int(item) for item in right_list[0].split(",") if item
            ]
        # for r_item in left_list.pop().split("]"):
        #     if num_list:
        #         num_list = [num for num in left_list.pop().split(",")] + num_list + [num for num in r_item.split(
        #                 ",")]
        #     else:
        #         num_list = [num for num in r_item.split(",")]
        return num_list[0]


def test_Solution():
    s_obj = Solution()
    assert [1, 2, 3, 4] == s_obj.deserialize("[1,2,3,4]")
    assert [123, [456, [789]]] == s_obj.deserialize("[123,[456,[789]]]")


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.deserialize("[123,456,[788,799,833],[[]],10,[]]")
