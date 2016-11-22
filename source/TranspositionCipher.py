# !/usr/bin/env python
# coding:utf-8
from source.English import isEngSen


def TranEncrypt(plainText, key):
    """
    换位加密法加密字符串
    :param plainText: 明文
    :param key: 密钥，小于明文长度的一半
    :return: 密文
    """
    if key * 2 > len(plainText):
        raise ValueError('key should less than a half of plainText length')

    encryptArr = []
    for col in range(key):
        for point in range(col, len(plainText), key):
            encryptArr.append(plainText[point])

    return ''.join(encryptArr)


def TranDecrypt(cipherText, key=None):
    """
    用换位加密法解密字符串
    :param cipherText: 密文
    :param key: 密钥，有时解密，无时暴力破解（密钥遍历2-n/2）
    :return: [[key, plainText], ...]
    """
    if key:
        r = range(key, key + 1, 1)
    else:
        import math
        r = range(2, len(cipherText) // 2 + 1, 1)

    import math
    result = []
    for key in r:
        blockLen = math.ceil(len(cipherText) / key)
        shadedBlockP = key - ((blockLen * key) - len(cipherText))

        startPointArr = [0]
        for i in range(1, key, 1):
            if i <= shadedBlockP:
                startPointArr.append(startPointArr[i - 1] + blockLen)
            else:
                startPointArr.append(startPointArr[i - 1] + blockLen - 1)

        plainTextArr = []
        for offset in range(blockLen):
            for i, p in enumerate(startPointArr):
                if i >= shadedBlockP and offset >= blockLen - 1:
                    continue
                if p + offset >= len(cipherText):
                    continue
                plainTextArr.append(cipherText[p + offset])

        result.append([key, ''.join(plainTextArr)])

    return result


def TranDecrypt1(key, message):
    """
    用换位加密法解密字符串,原书版本
    :param key: 密钥
    :param message: 密文
    :return: 明文
    """
    import math
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0
    for ch in message:
        plaintext[col] += ch
        col += 1

        if (col == numOfColumns) or ((col == (numOfColumns - 1)) and (row >= (numOfRows - numOfShadedBoxes))):
            col = 0
            row += 1

    return ''.join(plaintext)


def main():
    secretStr = 'Common sense is not so common.'
    keyNum = 8
    print('The origin string    :', secretStr)
    print('The Cipher Key       :', keyNum)

    encryptStr = TranEncrypt(secretStr, keyNum)
    print('encrypting...')
    print('After Cipher         :', encryptStr)

    print('\nforce decrypting...')
    for key, plainText in TranDecrypt(encryptStr):
        if isEngSen(plainText):
            print(key, plainText)


if __name__ == '__main__':
    main()
