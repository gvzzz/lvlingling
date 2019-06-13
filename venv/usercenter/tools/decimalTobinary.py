
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
    print(decimalTobinary(126))
    print(len(decimalTobinary(126)))
    print(binaryTodecimal("100000000000000000000000"))
