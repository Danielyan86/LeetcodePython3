class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # no need to convert k into list
        # no need to create a new list, update the num directly
        carry = 0
        # travsal the list first
        for i in range(len(num) - 1, -1, -1):
            tmp = k % 10  # get the last number of K
            s = num[i] + tmp + carry
            carry = s // 10
            num[i] = s if s < 10 else s % 10

            k //= 10  # pop out the last number of K

        while k > 0:
            s = k % 10 + carry
            carry = s // 10
            if s >= 10:
                s = s % 10
            num.insert(0, s)  # insert to first one
            k //= 10
        # add the last 1 to the first
        if carry == 1:
            num.insert(0, 1)
        return num
