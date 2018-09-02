# coding:utf-8
"""
Created by tzw0745 at 2018/9/2
"""
import random
import re
import string
from collections import defaultdict
from itertools import product

from source import sub_cipher
from source.english import word_pattern, pattern_words, is_english

sub_cipher.LETTERS = string.ascii_lowercase

words_file = 'words_370k.txt'  # 这里用到破解方法比较依赖字典容量


def force_sub_decrypt(ciphertext: str):
    """
    暴力破解简单替换加密法
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
        c_ch2p_ch = defaultdict(set)
        for _p_word in pattern_words(word_pattern(_c_word), words_file):
            for _i, _c in enumerate(_c_word):
                c_ch2p_ch[_c].add(_p_word[_i])
        for _c in c_ch2p_ch:
            candidate[_c] = c_ch2p_ch[_c] if _c not in candidate \
                else (candidate[_c] & c_ch2p_ch[_c])
    # 排除掉已确定的候选明文字母
    _certain = set()
    for _c in candidate.keys():
        if len(candidate[_c]) == 1:
            _certain.add(list(candidate[_c])[0])
    for _c in candidate.keys():
        if len(candidate[_c]) > 1:
            candidate[_c] = candidate[_c] - _certain
    # 填充未出现的密文字母和不确定的密文字母
    _uncertain = set(sub_cipher.LETTERS) - _certain
    for _c in sub_cipher.LETTERS:
        if _c not in candidate:
            candidate[_c] = {'*'}
        elif not candidate[_c]:
            candidate[_c] = set(_uncertain)

    # 遍历所有可能密钥进行暴力破解
    _all_key = product(*[list(candidate[_c]) for _c in sub_cipher.LETTERS])
    keys_rev = []
    for _key_tuple in _all_key:
        _key_str = ''.join(_key_tuple)
        # 去除字母有重复的密钥
        _asterisk = len(re.findall(r'\*', _key_str)) - 1
        if not len(set(_key_str)) + _asterisk == len(_key_str):
            continue
        if '*' in _key_str:
            # 未出现的密文字母随机指定对应明文字符
            _key_list = list(_key_str)
            _p_chs = list(set(sub_cipher.LETTERS) - set(_key_str))
            for _i, _m in enumerate(re.finditer(r'\*', _key_str)):
                _key_list[_m.start()] = _p_chs[_i]
            _key_str = ''.join(_key_list)
        keys_rev.append(_key_str)
    keys = [sub_cipher.__rev_key(_k) for _k in keys_rev]

    res = []
    for i, key in enumerate(keys_rev):
        plaintext = sub_cipher.sub_encrypt(ciphertext, ''.join(key))
        res.append({'key': keys[i], 'plaintext': plaintext})
    return res


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
    ]).lower()
    key = list(sub_cipher.LETTERS)
    random.shuffle(key)
    key = ''.join(key)

    print('--- Simple Substitution Cipher Demon ---')
    print('Origin String :', plaintext)
    print('Key           :', key)

    print('\nEncrypting...')
    ciphertext = sub_cipher.sub_encrypt(plaintext, key)
    print('Ciphertext    :', ciphertext)

    print('\nForce Decrypting...')
    res = force_sub_decrypt(ciphertext)
    for info in res:
        if not is_english(info['plaintext'], 1.0, words_file):
            continue
        print('Key {0:<9} : {1}'.format(info['key'], info['plaintext']))


if __name__ == '__main__':
    main()
