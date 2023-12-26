class Solution:
    def jumpFloorII(self, number):
        if number == 0 or number == 1:
            return 1
        number_list = [1, 1]
        for each in range(2, number + 1):
            number_list.append(0)
            number_list[each] = sum(number_list)
        return number_list[number]


if __name__ == "__main__":
    s = Solution()
    print(s.jumpFloorII(0))
    print(s.jumpFloorII(1))
    print(s.jumpFloorII(2))
    print(s.jumpFloorII(3))
    print(s.jumpFloorII(4))
