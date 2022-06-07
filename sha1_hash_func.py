def iterator(to_hash):
    while to_hash:
        chunk = to_hash & (2 ** 448 - 1)
        size = len(bin(chunk)) - 2
        chunk = (chunk << 1) + 1
        chunk = chunk << (512 - size - 1)
        chunk += size
        yield chunk
        to_hash = to_hash >> 448

def leftrotate(to_rot, step):
    return ((to_rot >> 32 - step) | (to_rot << step)) & (2 ** 512 - 1)

def byte_split(value):
    lst = []
    while value:                                #big word split to small pieces
        lst.append((value & (2 ** 32 - 1)))
        value = value >> 32
    return lst

def text_convert(text, encoding='utf-8', errors='surrogatepass'):
    bits = int.from_bytes(text.encode(encoding, errors), 'big')         #text to binary-num convertation
    return bits

def sha1_hash_func(to_hash, h0=0x67452301, h1=0xEFCDAB89, h2=0x98BADCFE, h3=0x10325476, h4=0xC3D2E1F0):
    res_hash = 0
    for chunk in iterator(to_hash):         #main hash func
        w = byte_split(chunk)
        for i in range(16, 80):
            w.append(leftrotate((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 5))
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        for i in range(80):
            if 0 <= i <= 19:
                f = (b and c) or ((not b) and d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b and c) or (b and d) or (c and d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6
            temp = (leftrotate(a, 5) + f + e + k + w[i]) % (2 ** 32)
            e = d
            d = c
            c = leftrotate(b, 30)
            b = a
            a = temp
        h0 = h0 + a % (2 ** 32)
        h1 = h1 + b % (2 ** 32)
        h2 = h2 + c % (2 ** 32)
        h3 = h3 + d % (2 ** 32)
        h4 = h4 + e % (2 ** 32)
        chunk_hash = h0 << 128 | h1 << 96 | h2 << 64 | h3 << 32 | h4
        res_hash += chunk_hash
        res_hash %= 1 << 512
    return hex(res_hash)


to_hash = input("Print something to hash\n")
if to_hash.isdigit():
    print("Result hash:")
    print(sha1_hash_func(int(to_hash)))
else:
    print("Result hash:")
    to_hash = text_convert(to_hash)
    print(sha1_hash_func(to_hash))
