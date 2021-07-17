def count_characters(long_str: str):
    character_dic = {}
    max_number = 3
    total_count = 0
    for c in long_str:
        if c in character_dic:
            character_dic[c] = character_dic[c] + 1
        else:
            character_dic[c] = 1
    for key in character_dic:
        if character_dic[key] >= max_number:
            total_count = total_count + 1
    print(character_dic)
    print(total_count)
    print("*" * 10)


if __name__ == '__main__':
    count_characters("testeqweqwetertre")
    count_characters("")
    count_characters("test")
    count_characters("aaaaaaaaa")
