
def decimalTobinary (num):
    la = []
    if num < 0:
        return '-' + decimalTobinary(abs(num))
    while True:
        num, remainder = divmod(num, 2)
        la.append(str(remainder))
        if num == 0:
            return ''.join(la[::-1])





def binaryTodecimal(string_num):
    return str(int(string_num, 2))





if __name__ == '__main__':
    print(decimalTobinary(11))
    print(len(decimalTobinary(11)))
    print(binaryTodecimal("11100000000000000"))
