def solution(A, K):
    # Check if the array is empty
    if not A:
        return A

    # If all elements are the same or if K is a multiple of the length, no rotation is needed
    if len(set(A)) == 1 or K % len(A) == 0:
        return A

    # Calculate the effective rotation
    pos = K % len(A)

    # Rotate the array by slicing
    return A[-pos:] + A[:-pos]


# 注意边界值判断
# 注意列表切片操作，第二个不是A[:pos-1],搞复杂了，要么都用正向索引，要么都用负向索引
