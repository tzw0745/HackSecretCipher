# coding:utf-8
"""
只替换字母的简单替换加密法比较容易进行暴力破解
同时这里的暴力破解方法非常依赖字典容量，需要在english.py里读取words_alpha.txt
"""
import random
import re
import string
from collections import defaultdict
from itertools import product

from source.english import word_pattern, pattern_words, is_english

# LETTERS = ''.join([
#     string.digits,
#     string.ascii_letters,
#     string.punctuation,
#     ' \t'
# ])
LETTERS = string.ascii_lowercase


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


def force_sub_decrypt(ciphertext: str):
    """
    暴力破解简单替换加密法，非常依赖字典容量
    :param ciphertext: 密文
    :return: 所有可能的密钥及解密结果
    """
    if not isinstance(ciphertext, str):
        raise TypeError('Param "ciphertext" must be str')
    if not ciphertext.islower():
        raise ValueError('Param "ciphertext" must be lower str')

    # 找出26个密文字母的所有候选明文字母
    candidate = {}
    for _c_word in set(re.findall(r'[a-z]+', ciphertext)):
        _c_ch2p_ch = defaultdict(set)
        for _p_word in pattern_words(word_pattern(_c_word)):
            for _i, _c in enumerate(_c_word):
                _c_ch2p_ch[_c].add(_p_word[_i])
        for _c in _c_ch2p_ch:
            candidate[_c] = _c_ch2p_ch[_c] if _c not in candidate \
                else (candidate[_c] & _c_ch2p_ch[_c])
    # 排除掉已确定的候选明文字母
    _certain = set()
    for _c in candidate.keys():
        if len(candidate[_c]) == 1:
            _certain.add(list(candidate[_c])[0])
    for _c in candidate.keys():
        if len(candidate[_c]) > 1:
            candidate[_c] -= _certain
    # 填充未找到的密文字母
    _uncertain = set(LETTERS) - _certain
    for _c in LETTERS:
        if _c not in candidate:
            candidate[_c] = set(_uncertain)

    # 暴力破解
    _key_list = product(*[list(candidate[_c]) for _c in LETTERS])
    _key_list = filter(lambda _k: set(_k) == set(LETTERS), _key_list)
    keys_rev = [''.join(_k) for _k in _key_list]
    keys = [__rev_key(_k) for _k in keys_rev]

    res = []
    for i, key in enumerate(keys_rev):
        plaintext = sub_encrypt(ciphertext, ''.join(key))
        res.append({'key': keys[i], 'plaintext': plaintext})
    return res


def __rev_key(key: str):
    return ''.join(LETTERS[key.find(_c)] for _c in LETTERS)


def main():
    plaintext = '\t'.join([
        'In cryptography, a substitution cipher is a method of encrypting'
        ' by which units of plaintext are replaced with ciphertext, '
        'according to a fixed system; the "units" may be single letters '
        '(the most common), pairs of letters, triplets of letters, mixtures'
        ' of the above, and so forth. The receiver deciphers the text by '
        'performing the inverse substitution.',
        'Substitution ciphers can be compared with transposition ciphers. '
        'In a transposition cipher, the units of the plaintext are '
        'rearranged in a different and usually quite complex order, but '
        'the units themselves are left unchanged. By contrast, in a '
        'substitution cipher, the units of the plaintext are retained in '
        'the same sequence in the ciphertext, but the units themselves '
        'are altered.',
        'There are a number of different types of substitution cipher. '
        'If the cipher operates on single letters, it is termed a simple '
        'substitution cipher; a cipher that operates on larger groups of '
        'letters is termed polygraphic. A monoalphabetic cipher uses fixed '
        'substitution over the entire message, whereas a polyalphabetic '
        'cipher uses a number of substitutions at different positions in '
        'the message, where a unit from the plaintext is mapped to one of '
        'several possibilities in the ciphertext and vice versa.'
    ])
    plaintext = plaintext.lower()  # 简单替换加密法，统一为小写
    key = list(LETTERS)
    random.shuffle(key)
    key = ''.join(key)

    print('--- Substitution Cipher Demon ---')
    print('Origin String :', plaintext)
    print('Key           :', key)

    print('\nEncrypting...')
    ciphertext = sub_encrypt(plaintext, key)
    print('Ciphertext    :', ciphertext)

    print('\nForce Decrypting...')
    res = force_sub_decrypt(ciphertext)
    for info in res:
        if not is_english(info['plaintext'], 1.0):
            continue
        print('Key {0:<9} : {1}'.format(info['key'], info['plaintext']))


if __name__ == '__main__':
    main()
