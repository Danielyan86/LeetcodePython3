class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrace(conbination, start_i):
            if len(conbination) == len(digits):
                res.append(conbination)
            else:
                for ch in phone[digits[start_i]]:
                    backtrace(conbination + ch, start_i + 1)

        res = []
        backtrace("", 0)
        return res
