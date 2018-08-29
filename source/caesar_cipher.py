# coding:utf-8
import string

LETTERS = ''.join([
    string.digits,
    string.ascii_letters,
    string.punctuation,
    ' \t'
])


def caesar_encrypt(plaintext: str, key: int):
    """
    凯撒加密法加密文本
    :param plaintext: 明文
    :param key: 密钥
    :return: 密文，字符串
    """
    if not isinstance(plaintext, str):
        raise TypeError('Param "plaintext" must be str')
    if not isinstance(key, int):
        raise TypeError('Param "key" must be int')
    key = key % len(LETTERS)
    if not plaintext or not key:
        return plaintext

    def _encrypt(_c):
        _index = LETTERS.find(_c)
        return _c if _index == -1 else \
            LETTERS[(_index + key) % len(LETTERS)]

    return ''.join(map(_encrypt, plaintext))


def caesar_decrypt(ciphertext: str, key: int):
    """
    凯撒加密法解密文本
    :param ciphertext: 密文
    :param key: 密钥
    :return: 明文，字符串
    """
    key = len(LETTERS) - key % len(LETTERS)
    return caesar_encrypt(ciphertext, key)


def force_caesar_decrypt(ciphertext: str):
    """
    暴力破解凯撒加密法
    :param ciphertext: 密文
    :return: 所有可能的密码与明文的列表
    """
    res = []
    for key in range(len(LETTERS)):
        plaintext = caesar_decrypt(ciphertext, key)
        res.append({'key': key, 'plaintext': plaintext})
    return res


def main():
    plaintext = 'Two big mad jocks help fax every quiz. 123'
    key = 8

    print('--- Caesar Cipher Demon ---')
    print('Origin String :', plaintext)
    print('Key           :', key)

    print('\nEncrypting...')
    ciphertext = caesar_encrypt(plaintext, key)
    print('Ciphertext    :', ciphertext)

    print('\nForce Decrypting...')
    res = force_caesar_decrypt(ciphertext)
    from source.english import is_english
    for info in res:
        if not is_english(info['plaintext']):
            continue
        print('Key {0:<9} : {1}'.format(info['key'], info['plaintext']))


if __name__ == '__main__':
    main()
