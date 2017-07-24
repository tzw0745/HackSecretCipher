# !/usr/bin/env python
# coding:utf-8
from source.IsEnglish import is_english


def caesar_cipher(plain_text, key):
    """
    凯撒加密
    :param plain_text: 明文
    :param key: 密钥，0-25
    :return: 凯撒加密后的字符串
    """
    # 检查密钥范围
    if key < 0 or key > 25:
        raise ValueError

    result_arr = []
    for ch in plain_text:
        # 忽略非字母和数字
        if not ch.isalpha() and not ch.isdigit():
            result_arr.append(ch)
            continue

        if ch.islower():
            i = ord(ch) + key
            if not chr(i).islower():
                i -= 26
        elif ch.isupper():
            i = ord(ch) + key
            if not chr(i).isupper():
                i -= 26
        else:
            i = ord(ch) + key % 10
            if not chr(i).isdigit():
                i -= 10
        result_arr.append(chr(i))
    return ''.join(result_arr)


def caesar_decipher(cipher_text, key=None):
    """
    凯撒解密
    :param cipher_text: 密文
    :param key: 密钥，0-25，有时解密，无时暴力破解
    :return: [[key, plainText], ...]
    """
    if key:
        # 检查密钥范围
        if key < 0 or key > 25:
            raise ValueError
        r = [key]
    else:
        r = range(26)

    result_arr = []
    for key in r:
        decrypt_arr = []
        for ch in cipher_text:
            # 忽略非字母和数字
            if not ch.isalpha() and not ch.isdigit():
                decrypt_arr.append(ch)
                continue

            if ch.islower():
                i = ord(ch) - key
                if not chr(i).islower():
                    i += 26
            elif ch.isupper():
                i = ord(ch) - key
                if not chr(i).isupper():
                    i += 26
            else:
                i = ord(ch) - key % 10
                if not chr(i).isdigit():
                    i += 10
            decrypt_arr.append(chr(i))

        result_arr.append([key, ''.join(decrypt_arr)])

    return result_arr


def main():
    plain_text = 'Two big mad jocks help fax every quiz. 123'
    key = 8
    print('The origin string    :', plain_text)
    print('The Caesar Cipher Key:', key)

    cipher_text = caesar_cipher(plain_text, key)
    print('encrypting...')
    print('After Caesar Cipher  :', cipher_text)

    print('\nforce decrypting...')
    for key, plain_text in caesar_decipher(cipher_text):
        if is_english(plain_text):
            print('Key #{0}: {1}'.format(key, plain_text))


if __name__ == '__main__':
    main()
