# !/usr/bin/env python
# coding:utf-8
import math

from source.IsEnglish import is_english


def tran_encrypt(plain_text, key):
    """
    换位加密法加密字符串
    :param plain_text: 明文
    :param key: 密钥，大于1，不大于明文长度的一半
    :return: 密文
    """
    plain_arr = list(plain_text)
    if not 1 < key <= len(plain_arr) / 2:
        raise ValueError('key error')

    encrypt_arr = []
    for i, ch in enumerate(plain_arr):
        if not ch:
            continue
        for sept in range(i, len(plain_text), key):
            encrypt_arr.append(plain_arr[sept])
            plain_arr[sept] = None

    return ''.join(encrypt_arr)


def tran_decrypt(cipher_text, key=None):
    """
    用换位加密法解密字符串
    :param cipher_text: 密文
    :param key: 密钥，大于1，不大于明文长度的一半。无密钥时暴力破解
    :return: [[key, plainText], ...]
    """
    if key:
        if not 1 < key <= len(cipher_text) // 2:
            raise ValueError('key error')
        r = [key]
    else:
        r = range(2, len(cipher_text) // 2 + 1, 1)

    result = []
    for key in r:
        cipher_arr = list(cipher_text)
        ceil = int(math.ceil(len(cipher_arr) / key))
        if len(cipher_arr) % key != 0:
            for i in range(len(cipher_arr) % key + 1, key + 1, 1):
                cipher_arr.insert(i * ceil - 1, '')
        result.append([key, tran_encrypt(cipher_arr, ceil)])
    return result


def main():
    plain_text = 'Two big mad jocks help fax every quiz. 123'
    key = 8
    print('The origin string    :', plain_text)
    print('The Caesar Cipher Key:', key)

    cipher_text = tran_encrypt(plain_text, key)
    print('encrypting...')
    print('After Caesar Cipher  :', cipher_text)

    print('\nforce decrypting...')
    for key, plain_text in tran_decrypt(cipher_text):
        if is_english(plain_text):
            print('Key #{0}: {1}'.format(key, plain_text))


if __name__ == '__main__':
    main()
