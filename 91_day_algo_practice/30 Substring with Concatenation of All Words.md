### solutions

字典计数法：如果某一个连续的字符分割出来的字符 list 的每个 word 的数目和希望的一样，则满足需求，记录下标

- 统计 words 里面每个 word 出现次数
- 遍历字符串下标
- 因为每个 word 长度相等，下标+3 为一个 word，如果在字典里面，则从当前下标开始取整个 words 长度，并分割成新的 words list
- 统计新的 words list 和期望比较

### code

```python


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        words_counter = collections.Counter(words)
        word_l = len(words[0])
        words_l = word_l * len(words)
        index = 0
        while index + words_l <= len(s) and index < len(s):
            if s[index : index + word_l] in words_counter:
                tmp_list = [
                    s[j : j + word_l] for j in range(index, index + words_l, word_l)
                ]
                if collections.Counter(tmp_list) == words_counter:
                    res.append(index)
            index += 1
        return res
```

### complexity

n 为 s 长度
m 为 words 长度

- time: 小于 O（n\*n）
- space： O（n+m）
