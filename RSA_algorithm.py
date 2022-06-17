from random import *


def find_divisior(a, b):
    if b == 0:
        x = 1
        y = 0
        return x, y
    else:
        x1, y1 = find_divisior(b, a % b)
        x = y1
        y = x1 - int(a / b) * y1
        return x, y


def generateKey():
    p = 1103
    q = 1109
    n = p * q
    fn = (p - 1) * (q - 1)
    e = 65537
    x, y = find_divisior(e, fn)
    if x < 0:
        x = x + fn
    d = x
    return (n, e), (n, d)


def encrypt(m, publicKey):
    return pow(m, publicKey[1], publicKey[0])


def decrypt(c, privateKey):
    return pow(c, privateKey[1], privateKey[0])


def text_split(text):
    res = []
    for i in text:
        res.append(ord(i))
    return res


def encrypt_text(m, publicKey):
    text = text_split(m)
    res = []
    shifr = []
    for i in text:
        t = 0
        i = int(i)
        if t == 0:
            res.append(i)
        else:
            res.append((i + res[t-1])%123)
        t += 1
    for i in res:
        shifr.append(encrypt(i, publicKey))
    return shifr

def decrypt_text(list, privateKey):
    res = []
    message = ''
    for i in list:
        t = 0
        i = int(i)
        if t == 0:
            res.append(i)
        else:
            res.append((i - res[t-1])%123)
        t += 1
    for i in res:
        message += chr(decrypt(i, privateKey))
    return message


publicKey, privateKey = generateKey()
m = input("Print something to encrypt\n")
c = encrypt_text(m, publicKey)
print("Encrypted text: ", c)
d = decrypt_text(c, privateKey)
print("Decrypted text: ", d)