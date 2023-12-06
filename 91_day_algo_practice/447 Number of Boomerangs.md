## solutions

这题目理解了很久，还是搞不懂，先是被 i 迷惑了，以为 xi，yi 和 i 有什么关系，也不知道 k 又是哪里来的。
其实翻译过来就是坐标上任意三个点，A，B，C，如果有一个点到另外两个点具体距离一样则符合要求，记录下来，但是顺序必须是【中左右】或这【中右左】（假设中间一点到左右相等），每个点用 tuple 表示（x,y）

- 用哈希表记录每个点到其他点的距离，距离一样则加一

- 两个循环遍历所有点
- 计算

### code

```python

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res=0
        for i in range(len(points)):
            hashmap=collections.defaultdict(int)
            for j in range(len(points)):
                distant=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                hashmap[distant]+=1
                res+=hashmap[distant]*2-2
        return res

```

### complexsity

space: O(n)
time: O(n\*n)
