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
-  only need to strip the right 0
-  the split method of python naturally remove the split diameter
