# coding:utf-8
import random
import string

LETTERS = ''.join([
    string.digits,
    string.ascii_letters,
    string.punctuation,
    ' \t'
])


def vigenere_encrypt(plaintext: str, key: str):
    """
    维吉尼亚加密法加密文本
    :param plaintext: 明文
    :param key: 密钥，长度至少为1的字符串，且必须为LETTERS的子集
    :return: 密文，字符串
    """
    if not isinstance(plaintext, str):
        raise TypeError('Param "plaintext" must be str')
    if not isinstance(key, str):
        raise TypeError('Param "key" must be str')
    if not key or set(key) - set(LETTERS):
        raise ValueError('Param "key" not correct')
    if not plaintext or key == LETTERS[0]:
        return plaintext

    global _offset
    _offset = 0

    def _encrypt(_c):
        global _offset
        _key_ch = key[_offset]
        _offset = (_offset + 1) % len(key)
        _index = LETTERS.find(_c)
        return _c if _index == -1 else \
            LETTERS[(_index + LETTERS.find(_key_ch)) % len(LETTERS)]

    return ''.join(map(_encrypt, plaintext))


def vigenere_decrypt(ciphertext: str, key: str):
    """
    维吉尼亚加密法解密文本
    :param ciphertext: 密文
    :param key: 密钥，长度至少为1的字符串，且必须为LETTERS的子集
    :return: 明文，字符串
    """
    if not isinstance(key, str):
        raise TypeError('Param "key" must be str')
    if not key or set(key) - set(LETTERS):
        raise ValueError('Param "key" not correct')

    _len = len(LETTERS)
    key_rev = [LETTERS[(_len - LETTERS.find(_c)) % _len] for _c in key]
    return vigenere_encrypt(ciphertext, ''.join(key_rev))


def main():
    plaintext = 'Two big mad jocks help fax every quiz. 123'
    key = list(LETTERS)
    random.shuffle(key)
    key = ''.join(key)

    print('--- Vigenere Cipher Demon ---')
    print('Origin String :', plaintext)
    print('Key           :', key)

    print('\nEncrypting...')
    ciphertext = vigenere_encrypt(plaintext, key)
    print('Ciphertext    :', ciphertext)

    print('\nDecrypting...')
    plaintext = vigenere_decrypt(ciphertext, key)
    print('Plaintext     :', plaintext)


if __name__ == '__main__':
    main()
