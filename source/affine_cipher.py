# coding:utf-8
import math
import string

LETTERS = ''.join([
    string.digits,
    string.ascii_letters,
    string.punctuation,
    ' \t'
])


def affine_encrypt(plaintext: str, key_a: int, key_b: int):
    """
    仿射加密法加密文本，公式：E(x) = (key_a * x + key_b) % len(LETTERS)
    :param plaintext: 明文
    :param key_a: 密钥a，不为0且需要和len(LETTERS)互质
    :param key_b: 密钥b
    :return: 密文，字符串
    """
    if not isinstance(plaintext, str):
        raise TypeError('Param "plaintext" must be str')
    if not isinstance(key_a, int) or not isinstance(key_b, int):
        raise TypeError('Param "key_a" and "key_b" must be int')
    if key_a == 0 or math.gcd(key_a, len(LETTERS)) != 1:
        raise ValueError('Param "key_a" not correct')
    key_b = key_b % len(LETTERS)
    if not plaintext or key_a == 1 and key_b == 0:
        return plaintext

    def _encrypt(_c):
        _index = LETTERS.find(_c)
        return _c if _index == -1 else \
            LETTERS[(_index * key_a + key_b) % len(LETTERS)]

    return ''.join(map(_encrypt, plaintext))


def affine_decrypt(ciphertext: str, key_a: int, key_b: int):
    """
    仿射加密法解密文本
    :param ciphertext: 密文
    :param key_a: 密钥a，不为0且需要和len(LETTERS)互质
    :param key_b: 密钥b
    :return: 明文，字符串
    """
    if not isinstance(ciphertext, str):
        raise TypeError('Param "plaintext" must be str')
    if not isinstance(key_a, int) or not isinstance(key_b, int):
        raise TypeError('Param "key_a" and "key_b" must be int')
    if key_a == 0 or math.gcd(key_a, len(LETTERS)) != 1:
        raise ValueError('Param "key_a" not correct')
    key_b = key_b % len(LETTERS)
    if not ciphertext or key_a == 1 and key_b == 0:
        return ciphertext

    m = inverse_mod(key_a, len(LETTERS))

    def _decrypt(_c):
        _index = LETTERS.find(_c)
        return _c if _index == -1 else \
            LETTERS[(_index - key_b) * m % len(LETTERS)]

    return ''.join(map(_decrypt, ciphertext))


def force_affine_decrypt(ciphertext: str):
    """
    暴力破解仿射加密法
    :param ciphertext: 密文串
    :return: 所有可能的密码与明文的列表
    """
    res = []
    for key_a in range(1, len(ciphertext), 1):
        for key_b in range(1, len(ciphertext), 1):
            try:
                plain_text = affine_decrypt(ciphertext, key_a, key_b)
            except ValueError:
                continue
            res.append({'key_a': key_a, 'key_b': key_b,
                        'plaintext': plain_text})
    return res


def inverse_mod(a: int, b: int):
    """
    扩展欧几里得算法求模反
    :param a: 一个数
    :param b: 另一个数
    :return: a和b的模反
    """
    if not isinstance(a, int) or not isinstance(b, int) \
            or math.gcd(a, b) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, b
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), \
                                 (u3 - q * v3), v1, v2, v3
    return u1 % b


def main():
    plaintext = 'Two big mad jocks help fax every quiz. 123'
    key_a = 9997
    key_b = 8

    print('--- Affine Cipher Demon ---')
    print('Origin String :', plaintext)
    print('Key           :', key_a, key_b)

    print('\nEncrypting...')
    ciphertext = affine_encrypt(plaintext, key_a, key_b)
    print('Ciphertext    :', ciphertext)

    print('\nForce Decrypting...')
    res = force_affine_decrypt(ciphertext)
    from source.english import is_english
    for info in res:
        if not is_english(info['plaintext']):
            continue
        key = '{}, {}'.format(info['key_a'], info['key_b'])
        print('Key {0:<9} : {1}'.format(key, info['plaintext']))


if __name__ == '__main__':
    main()
