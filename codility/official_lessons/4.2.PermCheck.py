# time complexity: O(2N)
def solution(A):
    # Implement your solution here
    arr = A
    arr_set = set()
    for n in arr:
        arr_set.add(n)
    for i in range(1, len(arr) + 1):
        if i not in arr_set:
            return 0
    return 1


# this is a very clever solution, using the all() function to check if all elements are within [1..N] and the set has exactly N elements
def solution(A):
    N = len(A)
    arr_set = set(A)  # Directly create the set from A

    # Check if all elements are within [1..N] and the set has exactly N elements
    if len(arr_set) == N and all(1 <= n <= N for n in arr_set):
        return 1
    else:
        return 0


# this is the simplest solution, using a set to store unique elements and check if the length of the set is equal to N
def solution(A):
    N = len(A)
    unique_elements = set()

    for element in A:
        # Check if element is within the range [1..N], if the element is out of range, end the function early
        if element < 1 or element > N:
            return 0
        unique_elements.add(element)

    # Check if we have exactly N unique elements
    if len(unique_elements) == N:
        return 1
    else:
        return 0
