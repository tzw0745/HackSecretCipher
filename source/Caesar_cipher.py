# !/usr/bin/env python
# coding:utf-8
from source.English import isEngSen


def CaesarCipher(plainText, key):
    """
    凯撒加密
    :param plainText: 明文
    :param key: 密钥，0-25
    :return: 凯撒加密后的字符串
    """
    # 检查密钥范围
    if key < 0 or key > 25:
        raise ValueError

    encryptArr = []
    for ch in plainText:
        # 如果不是字符和则不用加密
        if not ch.isalpha() and not ch.isdigit():
            encryptArr.append(ch)
            continue

        if ch.isalpha():
            # 加密并循环字母
            i = ord(ch) + key
            if ch.islower() and not chr(i).islower() \
                    or ch.isupper() and not chr(i).isupper():
                i -= 26
        else:
            i = ord(ch) + key % 10
            if ch.isdigit() and not chr(i).isdigit():
                i -= 10
        encryptArr.append(chr(i))
    return ''.join(encryptArr)


def DeCaesarCipher(cipherText, key=None):
    """
    凯撒解密
    :param cipherText: 密文
    :param key: 密钥，有时解密，无时暴力破解
    :return: [[key, plainText], ...]
    """
    if key:
        r = range(key, key + 1, 1)
    else:
        r = range(26)
    result = []
    # 如果带key则r只有一个元素，不带key时r有26个元素
    for key in r:
        decryptArr = []
        for ch in cipherText:
            # 如果不是字符则不用解密
            if not ch.isalpha() and not ch.isdigit():
                decryptArr.append(ch)
                continue

            if ch.isalpha():
                # 解密并循环字母
                i = ord(ch) - key
                if ch.islower() and not chr(i).islower() or \
                                ch.isupper() and not chr(i).isupper():
                    i += 26
            else:
                i = ord(ch) - key % 10
                if ch.isdigit() and not chr(i).isdigit():
                    i += 10
            decryptArr.append(chr(i))

        result.append([key, ''.join(decryptArr)])

    return result


def main():
    plainText = 'our bank password is 123456'
    keyNum = 8
    print('The origin string    :', plainText)
    print('The Caesar Cipher Key:', keyNum)

    cipherText = CaesarCipher(plainText, keyNum)
    print('encrypting...')
    print('After Caesar Cipher  :', cipherText)

    print('\nforce decrypting...')
    for key, plainText in DeCaesarCipher(cipherText):
        if isEngSen(plainText):
            print('Key #{0}: {1}'.format(key, plainText))


if __name__ == '__main__':
    main()
