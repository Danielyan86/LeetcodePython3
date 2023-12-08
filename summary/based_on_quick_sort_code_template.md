## Partition 函数

首先，先写 partition 模板

```python
def partition(nums, left, right):
    pivot = nums[left]#取左边第一个为标杆
    l,r = left, right
    while(i < j):
        while(i<j and nums[j]>=pivot): #从后往前查找，直到找到一个比pivot更小的数
            j-=1
        nums[i] = nums[j] #将更小的数放入左边
        while(i<j and nums[i]<=pivot): #从前往后找，直到找到一个比pivot更大的数
            i+=1
        nums[j] = nums[i] #将更大的数放入右边
    #循环结束，i与j相等
    nums[i] = pivot #待比较数据放入最终位置
    return i #返回待比较数据最终位置
```

## 快速排序

```python
    def quicksort(self, nums, left, right):
        if left < right:  # 如果l==r,表示长度相等，直接返回
            index = self.partition(nums, left, right)  # index位置不会再变，重新划分分区递归调用
            self.quicksort(nums, left, index - 1)
            self.quicksort(nums, index + 1, right)
        return nums
```

## topk 切分

将快速排序改成快速选择，即我们希望寻找到一个位置，这个位置左边是 k 个比这个位置上的数更小的数，右边是 n-k-1 个比该位置上的数大的数，我将它命名为 topk_split，找到这个位置后停止迭代，完成了一次划分。

```python
def topk_split(nums, k, left, right):
    #寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
    if (left<right):
        index = partition(nums, left, right)
        if index==k:
            return
        elif index < k:
            topk_split(nums, k, index+1, right)
        else:
            topk_split(nums, k, left, index-1)
```

### 获得第 k 大的数

def topk_large(nums, k):
#parttion 是按从小到大划分的，如果让 index 左边为前 n-k 个小的数，则 index 右边为前 k 个大的数
topk_split(nums, len(nums)-k, 0, len(nums)-1) #把 k 换成 len(nums)-k
return nums[len(nums)-k]
