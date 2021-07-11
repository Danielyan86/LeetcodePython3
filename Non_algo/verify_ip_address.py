def verify_ip_address(ip_address: str):
    num_list = ip_address.split(".")
    length = len(num_list)
    if length != 4:
        print("length is not right")
        return False
    flag_list = []
    for num in num_list:
        if num.isdigit():
            flag_list.append(verify_num(num))
        else:
            return False
    if False in flag_list:
        return False
    else:
        return True


def verify_num(num: str):
    if num.startswith("0") and len(num) != 1:
        return False
    if 0 <= int(num) <= 255:
        return True
    else:
        print(f"num:{num} is illegal")
        return False


def test_happy_scenario():
    assert verify_ip_address("192.168.1.1") is True
    assert verify_ip_address("255.168.0.1") is True
    assert verify_ip_address("256.168.01.1") is False
    assert verify_ip_address("256.168.-1.1") is False
    assert verify_ip_address("192.AA.01.1") is False


if __name__ == '__main__':
    test_ip_1 = ["192.168.01.1"]
    for ip in test_ip_1:
        res = verify_ip_address(ip)
