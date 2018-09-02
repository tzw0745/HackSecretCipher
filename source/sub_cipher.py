# coding:utf-8
import random
import string

LETTERS = ''.join([
    string.digits,
    string.ascii_letters,
    string.punctuation,
    ' \t'
])


def sub_encrypt(plaintext: str, key: str):
    """
    替换加密法加密文本
    :param plaintext: 明文
    :param key: 密钥，LETTERS的一种排列组合
    :return: 密文，字符串
    """
    if not isinstance(plaintext, str):
        raise TypeError('Param "plaintext" must be str')
    if not isinstance(key, str):
        raise TypeError('Param "key" must be str')
    if not len(key) == len(LETTERS) or \
            not set(key) == set(LETTERS):
        raise ValueError('Param "key" not correct')
    if not plaintext or plaintext == LETTERS:
        return plaintext

    def _encrypt(_c):
        _index = LETTERS.find(_c)
        return _c if _index == -1 else key[_index]

    return ''.join(map(_encrypt, plaintext))


def sub_decrypt(ciphertext: str, key: str):
    """
    替换加密法解密文本
    :param ciphertext: 密文
    :param key: 密钥，LETTERS的一种排列组合
    :return: 明文，字符串
    """
    if not isinstance(key, str):
        raise TypeError('Param "key" must be str')
    if not len(key) == len(LETTERS) or \
            not set(key) == set(LETTERS):
        raise ValueError('Param "key" not correct')

    return sub_encrypt(ciphertext, __rev_key(key))


def __rev_key(key: str):
    return ''.join(LETTERS[key.find(_c)] for _c in LETTERS)


def main():
    plaintext = 'Two big mad jocks help fax every quiz. 123'
    key = list(LETTERS)
    random.shuffle(key)
    key = ''.join(key)

    print('--- Substitution Cipher Demon ---')
    print('Origin String :', plaintext)
    print('Key           :', key)

    print('\nEncrypting...')
    ciphertext = sub_encrypt(plaintext, key)
    print('Ciphertext    :', ciphertext)

    print('\nDecrypting...')
    plaintext = sub_decrypt(ciphertext, key)
    print('Plaintext     :', plaintext)


if __name__ == '__main__':
    main()
