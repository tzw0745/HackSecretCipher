# !/usr/bin/env python
# coding:utf-8
"""
Created by tzw0745 on 2016/11/14.
"""
from source.ModInverse import GCD, ModInverse

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]\
^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def SplitKey(key):
    """
    分解仿射加密密钥：乘数加密密钥，凯撒加密密钥
    :param key: 仿射加密密钥
    :return: set(乘数加密密钥，凯撒加密密钥)
    """
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return keyA, keyB


def CheckKeys(keyA, keyB, mode):
    """
    验证仿射加密密钥：乘数加密密钥，凯撒加密密钥的有效性
    :param keyA: 乘数加密密钥
    :param keyB: 凯撒加密密钥
    :param mode: 'encrypt'或'decrypt'
    :return: 无，如密钥无效，则程序将退出
    """
    if mode == 'encrypt' and keyA == 1:
        exit('仿射加密：乘数加密密钥不能为1。')
    if mode == 'encrypt' and keyB == 0:
        exit('仿射加密：凯撒加密密钥不能为0。')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        temp = '仿射加密：乘数加密的密钥必须大于0，凯撒加密的密钥必须在0和{}之间。'
        exit(temp.format(len(SYMBOLS) - 1))
    if GCD(keyA, len(SYMBOLS)) != 1:
        exit('仿射加密：乘数加密密钥必须和{}互质。'.format(len(SYMBOLS)))


def AffineEncrypt(plainText, key):
    """
    仿射加密法用密钥加密明文成密文
    :param plainText: 明文
    :param key: 密钥
    :return: 密文
    """
    keyA, keyB = SplitKey(key)
    CheckKeys(keyA, keyB, 'encrypt')
    cipherText = []
    for symbol in plainText:
        p = SYMBOLS.find(symbol)
        ch = symbol if p == -1 else SYMBOLS[(p * keyA + keyB) % len(SYMBOLS)]
        cipherText.append(ch)

    return ''.join(cipherText)


def AffineDecrypt(cipherText, key):
    """
    仿射加密法用密钥解密密文成明文
    :param cipherText: 密文
    :param key: 密钥
    :return: 明文
    """
    keyA, keyB = SplitKey(key)
    CheckKeys(keyA, keyB, 'decrypt')
    plainText = []
    modInvA = ModInverse(keyA, len(SYMBOLS))

    for symbol in cipherText:
        p = SYMBOLS.find(symbol)
        ch = symbol if p == -1 else SYMBOLS[(p - keyB) * modInvA % len(SYMBOLS)]
        plainText.append(ch)

    return ''.join(plainText)


if __name__ == '__main__':
    plain = """"A computer would deserve to be called intelligent if it \
could deceive a human into believing that it was human." -Alan Turing"""
    print('origin text   :', plain)
    key = 2023
    print('\nthe key of affine cipher :', key)

    cipher = AffineEncrypt(plain, key)
    print('\nafter encrypt :', cipher)

    plain = AffineDecrypt(cipher, key)
    print('\nafter decrypt :', plain)
