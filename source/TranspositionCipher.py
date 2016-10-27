# !/usr/bin/env python
# coding:utf-8

"""
说明：用换位加密法加密字符串
参数：plainText为待加密字符串，key为加密密钥
参数：key要小于字符串长度的一半
返回：加密后的字符串
"""
def TranEncrypt(plainText, key):
    if key * 2 > len(plainText):
        raise ValueError('key should less than a half of plainText length')

    encryptArr = []
    for col in range(key):
        for point in range(col, len(plainText), key):
            encryptArr.append(plainText[point])

    return ''.join(encryptArr)

def TranDecrypt(cipherText, key=None):
    """
    说明：用换位加密法解密字符串，自己写的版本
    参数：cipherText为被加密的字符串，key为解密密钥
    参数：当key为空时暴力破解，遍历从2到n/2的密钥（n为字符串长度）
    返回：列表，解码或暴力破解的结果
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
    说明：用换位加密法解密字符串，作者写的版本
    参数：解密密钥key和待解密字符串message
    返回：被解密的字符串
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
    print(TranDecrypt1(8, encryptStr))
    for decryptList in TranDecrypt(encryptStr):
        print(decryptList)


if __name__ == '__main__':
    main()
