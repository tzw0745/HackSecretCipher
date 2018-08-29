# coding:utf-8
import math


def tran_encrypt(plaintext: str, key: int):
    """
    换位加密法加密文本
    :param plaintext: 明文
    :param key: 密钥，大于0
    :return: 密文，字符串
    """
    if not isinstance(plaintext, str):
        raise TypeError('Param "plaintext" must be str')
    if not isinstance(key, int) or not key > 0:
        raise TypeError('Param "key" must be int and bigger than 0')
    if not plaintext or key <= 1 or key >= len(plaintext):
        return plaintext

    loops = math.ceil(len(plaintext) / key)
    ciphertext_arr = []
    for i in range(key):
        for loop in range(loops):
            if i + loop * key < len(plaintext):
                ciphertext_arr.append(plaintext[i + loop * key])
    return ''.join(ciphertext_arr)


def tran_decrypt(ciphertext: str, key: int):
    """
    换位加密法解密文本
    :param ciphertext: 密文
    :param key: 密钥，大于0
    :return: 明文，字符串
    """
    if not isinstance(ciphertext, str):
        raise TypeError('Param "ciphertext" must be str')
    if not isinstance(key, int) or not key > 0:
        raise TypeError('Param "key" must be int and bigger than 0')
    if not ciphertext or key <= 1 or key >= len(ciphertext):
        return ciphertext

    loops = math.ceil(len(ciphertext) / key)
    ciphertext_arr = list(ciphertext)
    # insert blank
    blank_count = loops * key - len(ciphertext)
    for i in range(blank_count):
        ciphertext_arr.insert(len(ciphertext_arr) - i * loops, ' ')
    plaintext = tran_encrypt(''.join(ciphertext_arr), loops)
    # delete inserted blank
    return plaintext[:len(plaintext) - blank_count]


def force_tran_decrypt(ciphertext: str):
    """
    暴力破解换位加密法
    :param ciphertext: 密文串
    :return: 所有可能的密码与明文的列表
    """
    res = []
    for loops in range(1, len(ciphertext), 1):
        key = math.floor(len(ciphertext) / loops)
        res.append({'key': key, 'plaintext': tran_decrypt(ciphertext, key)})
    return res


def main():
    plaintext = 'Two big mad jocks help fax every quiz. 123'
    key = 8

    print('--- Transposition Cipher Demon ---')
    print('Origin String :', plaintext)
    print('Key           :', key)

    print('\nEncrypting...')
    ciphertext = tran_encrypt(plaintext, key)
    print('Ciphertext    :', ciphertext)

    print('\nForce Decrypting...')
    res = force_tran_decrypt(ciphertext)
    from source.english import is_english
    for info in res:
        if not is_english(info['plaintext']):
            continue
        print('Key {0:<9} : {1}'.format(info['key'], info['plaintext']))


if __name__ == '__main__':
    main()
