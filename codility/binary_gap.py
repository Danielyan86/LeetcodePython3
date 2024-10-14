# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution2(N):

    longest_gap = 0
    bin_str = str(bin(N))[2:]
    bin_str = bin_str.strip("0")
    bin_lists = bin_str.split("1")  #  need extra space for storing the list
    for bl in bin_lists:
        longest_gap = max(len(bl), longest_gap)
    return longest_gap


def solution(N: int):
    bin_str = str(bin(N))[2:]
    bin_str = bin_str.rstrip(
        "0"
    )  # this method ensure the the string start and end end number is 1
    longest_gap = current_gap = 0
    for n in bin_str:
        if n == "1":
            current_gap = 0
        elif n == "0":
            current_gap = current_gap + 1
        longest_gap = max(current_gap, longest_gap)
    return longest_gap


if "__main__" == __name__:
    print(solution(1041))  # Expected output: 5
    print(solution(32))  # Expected output: 0
