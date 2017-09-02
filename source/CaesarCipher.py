# !/usr/bin/env python
# coding:utf-8
from source.IsEnglish import is_english


def caesar_encrypt(plain_text, key):
    """
    凯撒加密法加密
    :param plain_text: 明文
    :param key: 密钥，1-25
    :return: 凯撒加密后的字符串
    """
    # 检查密钥范围
    if not 1 <= key <= 25:
        raise ValueError('key error')

    result_arr = []
    for ch in plain_text:
        if ch.islower():
            i = ord(ch) + key
            i = i if chr(i).islower() else i - 26
        elif ch.isupper():
            i = ord(ch) + key
            i = i if chr(i).isupper() else i - 26
        elif ch.isdigit():
            i = ord(ch) + key % 10
            i = i if chr(i).isdigit() else i - 10
        else:
            i = ord(ch)
        result_arr.append(chr(i))
    return ''.join(result_arr)


def caesar_decrypt(cipher_text, key=None):
    """
    凯撒解密
    :param cipher_text: 密文
    :param key: 密钥，1-25，有时解密，无时暴力破解
    :return: [[key, plainText], ...]
    """
    if key:
        if not 1 <= key <= 25:
            raise ValueError('key error')
        r = [key]
    else:
        r = range(1, 26, 1)

    return list(map(lambda x: {'key': x, 'text': caesar_encrypt(cipher_text, 26 - x)}, r))


def main():
    plain_text = 'Two big mad jocks help fax every quiz. 123'
    key = 8
    print('The origin string    :', plain_text)
    print('The Caesar Cipher Key:', key)

    print('encrypting...')
    cipher_text = caesar_encrypt(plain_text, key)
    print('After Caesar Cipher  :', cipher_text)

    print('\nforce decrypting...')
    for info in caesar_decrypt(cipher_text):
        if is_english(info.get('text')):
            print('Key #{key}: {text}'.format_map(info))


if __name__ == '__main__':
    main()
