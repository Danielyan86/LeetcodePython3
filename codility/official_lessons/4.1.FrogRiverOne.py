def solution(X, A):
    pos_set = set()  # Start with an empty set
    for time, pos in enumerate(A):
        if 1 <= pos <= X:  # Only consider positions in the range [1, X]
            pos_set.add(pos)  # Add the position to the set
        if len(pos_set) == X:  # Check if all positions [1, X] are covered
            return time
    return -1  # If not all positions are covered
