#Rehan Javaid rj3dxu
def check (num):
    """
    This purpose of this function is to determine whether or not an input represents a valid credit card number based on calculations
    :param num: Any positive integer
    :return: if the integer is less than 10 or the value obatined from the function's calculations is not divisble by 10, the function returns false
    otherwise the function will return true if the value obtained from the function's calculations is divisble by 10
    """
    if num < 10:
        return False
    num = str(num)
    new_list = []
    for i in range(int(num[0]), int(num[-1])):
        a = 2*int(num[i])
        i+=2
        new_list.append(a)
        continue
    addition_multiply2 = sum(new_list)
    new_list2 = []
    for i in range(int(num[0]), int(num[-1])):
        b = int(num[i+1])
        i+=2
        new_list2.append(b)
        continue
    addition = sum(new_list2)
    test_value = addition + addition_multiply2
    if test_value % 10 == 0:
        return True
    else:
        return False


