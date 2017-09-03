# !/usr/bin/env python
# coding:utf-8
"""
Created by tzw0745 on 2017/9/3.
"""
from source.CaesarCipher import caesar_encrypt, caesar_decrypt


def vigenere_encrypt(plain_text, key):
    """
    维吉尼亚加密法加密
    :param plain_text: 明文
    :param key: 密钥，只包含英文字母的字符串
    :return: 密文
    """
    key = key.lower()
    if not key.isalpha():
        raise ValueError('key not correct')

    result_arr = []
    n = 0
    for ch in plain_text:
        if not ch.isalpha():
            result_arr.append(ch)
            continue

        if key[n] == 'a':
            result_arr.append(ch)
        else:
            result_arr.append(caesar_encrypt(ch, ord(key[n]) - 97))
        n = (n + 1) % len(key)
    return ''.join(result_arr)


def vigenere_decrypt(cipher_text, key):
    """
    维吉尼亚加密法解密
    :param cipher_text: 密文
    :param key: 密钥，只包含英文字母的字符串
    :return: 明文
    """
    key = key.lower()
    if not key.isalpha():
        raise ValueError('key not correct')

    result_arr = []
    n = 0
    for ch in cipher_text:
        if not ch.isalpha():
            result_arr.append(ch)
            continue

        if key[n] == 'a':
            result_arr.append(ch)
        else:
            result_arr.append(caesar_decrypt(
                ch, ord(key[n]) - 97)[0]['text'])
        n = (n + 1) % len(key)
    return ''.join(result_arr)


def main():
    plain_text = 'Two big mad jocks help fax every quiz.'
    key = ''.join(['fxx', 'k', 'that', 'shit'])
    print('The origin string    :', plain_text)
    print('The Vigenere Key     :', key)

    print('encrypting...')
    cipher_text = vigenere_encrypt(plain_text, key)
    print('After Vigenere Cipher:', cipher_text)

    print('decrypting...')
    plain_text = vigenere_decrypt(cipher_text, key)
    print('After Decrypt        :', plain_text)


if __name__ == '__main__':
    main()
