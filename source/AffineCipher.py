# !/usr/bin/env python
# coding:utf-8
"""
Created by tzw0745 on 2017/9/2.
"""
import math

from source.IsEnglish import is_english

LETTERS = ''.join([chr(x) for x in range(32, 127, 1)])


def affine_encrypt(plain_text, key_a, key_b, letters=None):
    """
    仿射加密法加密
    :param plain_text: 明文
    :param key_a: 乘数加密法密钥，大于1并和字符集长度互质
    :param key_b: 凯撒加密法密钥，大于0
    :param letters: 字符集，默认为预设字符集
    :return: 密文
    """
    s = letters if letters else LETTERS
    if key_a < 2 or math.gcd(key_a, len(s)) != 1:
        raise ValueError('key a not correct')
    key_b = key_b % len(s)
    if key_b < 1:
        raise ValueError('key b not correct')

    return ''.join(s[(s.find(x) * key_a + key_b) % len(s)]
                   for x in plain_text)


def inverse_mod(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), \
                                 (u3 - q * v3), v1, v2, v3
    return u1 % m


def affine_decrypt(cipher_text, key_a=None, key_b=None, letters=None):
    """
    仿射加密法解密
    :param cipher_text: 密文
    :param key_a: 乘数加密法密钥，大于1并和字符集长度互质，无时暴力破解
    :param key_b: 凯撒加密法密钥，大于0，无时暴力破解
    :param letters: 字符集，默认为预设字符集
    :return: 明文
    """
    s = letters if letters else LETTERS
    if key_a is not None and key_b is not None:
        if key_a < 2 or math.gcd(key_a, len(s)) != 1:
            raise ValueError('key a not correct')
        key_b = key_b % len(s)
        if key_b < 1:
            raise ValueError('key b not correct')

        key_a = inverse_mod(key_a, len(s))
        return ''.join(s[(s.find(x) - key_b) * key_a % len(s)]
                       for x in cipher_text)

    force_result = []
    for key_a in range(2, len(s), 1):
        for key_b in range(1, len(s), 1):
            try:
                text = affine_decrypt(cipher_text, key_a, key_b, s)
            except ValueError:
                continue
            force_result.append({'key_a': key_a,
                                 'key_b': key_b,
                                 'text': text})
    return force_result


def main():
    plain_text = 'Two big mad jocks help fax every quiz. 123'
    key_a = 123456789
    key_b = 123456789
    print('The origin string    :', plain_text)
    print('The Affine Cipher Key:', key_a, key_b)

    print('encrypting...')
    cipher_text = affine_encrypt(plain_text, key_a, key_b)
    print('After Affine Cipher  :', cipher_text)

    print('\nforce decrypting...')
    for info in affine_decrypt(cipher_text):
        if is_english(info.get('text')):
            print('Key #{key_a}, #{key_b}: {text}'.format_map(info))


if __name__ == '__main__':
    main()
