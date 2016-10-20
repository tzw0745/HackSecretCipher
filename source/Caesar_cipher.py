'''
参数：接收源字符串，密钥
参数：密钥范围为0-25
返回：经过凯撒加密后的字符串
'''
def CaesarCipher(string, key):
    # 检查密钥范围
    if key < 0 or key > 25:
        raise ValueError

    encryptArr = []
    for ch in string:
        # 如果不是字符和则不用加密
        if not ch.isalpha() and not ch.isdigit():
            encryptArr.append(ch)
            continue

        if ch.isalpha():
            # 加密并循环字母
            i = ord(ch) + key
            if ch.islower() and not chr(i).islower()\
                or ch.isupper() and not chr(i).isupper():
                i -= 26
        else:
            i = ord(ch) + key % 10
            if ch.isdigit() and not chr(i).isdigit():
                i -= 10
        encryptArr.append(chr(i))
    return ''.join(encryptArr)


'''
参数：接收加密后的字符串。可选参数为key
返回：无key时暴力破解凯撒加密，返回长26的数组。每个元素为：[key, originStr]
返回：有key时返回用key解凯撒加密后的结果：[key, originStr]
'''
def DeCaesarCipher(string, key=None):
    if key:
        r = range(key, key+1, 1)
    else:
        r = range(26)
    result = []
    # 如果带key则r只有一个元素，不带key时r有26个元素
    for key in r:
        decryptArr = []
        for ch in string:
            # 如果不是字符则不用解密
            if not ch.isalpha() and not ch.isdigit():
                decryptArr.append(ch)
                continue

            if ch.isalpha():
                # 解密并循环字母
                i = ord(ch) - key
                if ch.islower() and not chr(i).islower()\
                    or ch.isupper() and not chr(i).isupper():
                    i += 26
            else:
                i = ord(ch) - key % 10
                if ch.isdigit() and not chr(i).isdigit():
                    i += 10
            decryptArr.append(chr(i))

        result.append([key, ''.join(decryptArr)])

    return result


def main():
    secretStr = 'My bank password is 123456'
    keyNum = 8
    print('The origin string    :', secretStr)
    print('The Caesar Cipher Key:', keyNum)

    encryptStr = CaesarCipher(secretStr, keyNum)
    print('encrypting...')
    print('After Caesar Cipher  :', encryptStr)

    print('\nforce decrypting...')
    for key, decryptStr in DeCaesarCipher(encryptStr):
        print('Key #{0}: {1}'.format(key, decryptStr))

if __name__ == '__main__':
    main()
