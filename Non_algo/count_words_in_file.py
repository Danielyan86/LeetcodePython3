import collections


def count_words_in_file(filename):
    with open(filename) as f:
        content = f.read()
    word_count = collections.defaultdict(int)
    for word in content.split():
        word_count[word] += 1
    return word_count


if __name__ == "__main__":
    res = count_words_in_file("word_count_test.txt")
    print(res)
