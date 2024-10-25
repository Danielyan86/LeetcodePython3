A binary gap within a positive integer `N` is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of `N`.

For example:

- Number 9 has binary representation `1001` and contains a binary gap of length 2.
- Number 529 has binary representation `1000010001` and contains two binary gaps: one of length 4 and one of length 3.
- Number 20 has binary representation `10100` and contains one binary gap of length 1.
- Number 15 has binary representation `1111` and has no binary gaps.
- Number 32 has binary representation `100000` and has no binary gaps.

Write a function:

```python
def solution(N):
```

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example:

Given N = 1041, the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.
Given N = 32, the function should return 0, because N has binary representation 100000 and thus no binary gaps.
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

## solution

1. if we use the split method to convert the string into list and calculate the length of each list, the it need an extra space.
2. use iterate way to solve it

## some extra key points

- only need to strip the right 0
- the split method of python naturally remove the split diameter

## 破题

### 主干

分析题之后，其实主任务就是数两个 1 之前的 0 的个数，因此一遍循环就可以搞定。也就是每次遇到 1 的时候计数器置 0，然后开始数数

### 分支

- 数字需要转化成字符串，利用内置函数 bin
- 去掉前面的标志位, OB
- bin 之后左边是不会有 0 的
- 可以直接用 split 方法，但是会占用额外的内存空间

### 测试用例

如果是一个参数的用例，直接写传入的值
如果是多个，采用这种格式([3, 8, 9, 7, 6], 3)
