def convert(n1):
    pointer = len(n1) - 1
    while n1[pointer] == '0':
        pointer -= 2
    if pointer % 2 != 0:
        return n1[:pointer + 1]
    else:
        return n1[:pointer + 1] + '0'


num = input("Print hex to cnvert \n")
length = len(num[2:]) // 2
little_endian = int(convert(num), 16)
big_endian = int(num, 16)
print('Value:', num)
print('Number of bytes:', length)
print('Little-endian:', little_endian )
print('Big-endian:', big_endian)
print(hex(little_endian) + '0' * (2 * (length - len(str(little_endian)) + 2)))
print(hex(big_endian))
