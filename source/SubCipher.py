# !/usr/bin/env python
# coding:utf-8
"""
Created by tzw0745 on 2017/9/2.
"""

SIMPLE_LETTERS = ''.join([chr(x) for x in range(65, 91, 1)])
LETTERS = ''.join([chr(x) for x in range(32, 127, 1)])
dic = None


def sub_encrypt(plain_text, key, letters=None):
    """
    替换加密法加密
    :param plain_text: 明文
    :param key: 密钥，字符集不相等排列组合方式中的一种
    :param letters: 字符集，默认为ascii可见字符集
    :return: 密文
    """
    s = letters if letters else LETTERS
    if len(s) != len(key) or s == key or sorted(s) != sorted(key):
        raise ValueError('key not correct')

    return ''.join(key[s.find(x)] if x in s else x
                   for x in plain_text)


def simple_sub_encrypt(plain_text, key):
    """
    简单替换加密法加密(简单字符集为大写字母)
    :param plain_text: 明文
    :param key: 密钥，简单字符集不相等排列组合方式中的一种
    :return: 密文
    """
    return sub_encrypt(plain_text.upper(), key,
                       letters=SIMPLE_LETTERS)


def get_word_pattern(word):
    """
    获取单词的模式，代表单词字母顺序
    :param word: APPLE模式为12234
    :return: 数字模式
    """
    char_map = {}
    pattern = []
    n = 1
    for ch in word:
        if ch not in char_map:
            char_map[ch] = n
            n += 1
        pattern.append(str(char_map[ch]))

    return '.'.join(pattern)


def main():
    # 因为简单替换加密法的暴力破解对短句子太不友好了
    plain_text = 'Two big mad jocks help fax every quiz. 123'
    key = ''.join(reversed(LETTERS))
    print('The origin string    :', plain_text)
    print('The Sub Cipher Key   :', key)

    print('encrypting...')
    cipher_text = sub_encrypt(plain_text, key)
    print('The Cipher Text      :', cipher_text)


if __name__ == '__main__':
    main()

'''abandoned code
def sub_decrypt(cipher_text, key, letters=None):
    """
    替换加密法解密
    :param cipher_text: 密文
    :param key: 密钥，字符集不相等排列组合方式中的一种
    :param letters: 字符集，默认为ascii可见字符集
    :return: 明文
    """
    s = letters if letters else LETTERS

    return sub_encrypt(cipher_text, s, key)
'''

'''abandoned code
def simple_sub_decrypt(cipher_text, key=None):
    """
    简单替换加密法解密(简单字符集为大写字母)
    :param cipher_text: 密文
    :param key: 密钥，字符集不相等排列组合方式中的一种，无时暴力破解
    :return: 明文
    """
    cipher_text = cipher_text.upper()
    if key:
        return sub_decrypt(cipher_text, key,
                           letters=SIMPLE_LETTERS)

    global dic
    if not dic:
        with open('dictionary.txt', 'r') as f:
            content = f.read().upper()
        dic = set(re.findall('[A-Z]+', content))

    all_pattern = collections.defaultdict(list)
    for word in dic:
        all_pattern[get_word_pattern(word)].append(word)
    text_pattern = collections.defaultdict(list)
    for word in set(re.findall('[A-Z]+', cipher_text)):
        text_pattern[get_word_pattern(word)].append(word)

    maybe_map = {}
    for pattern in text_pattern:
        if pattern not in all_pattern:
            continue
        for cipher_word in text_pattern[pattern]:
            char_to_char = collections.defaultdict(list)
            for dic_word in all_pattern[pattern]:
                for i in range(len(cipher_word)):
                    char_to_char[cipher_word[i]].append(dic_word[i])
            for key in char_to_char:
                char_to_char[key] = set(char_to_char[key])
            maybe_map[cipher_word] = char_to_char

    and_map = {}
    for word in maybe_map:
        for ch in maybe_map[word]:
            if ch not in and_map:
                and_map[ch] = maybe_map[word][ch]
            else:
                and_map[ch] = (and_map[ch] & maybe_map[word][ch])

    char_to_char = collections.defaultdict(list)
    upper_char = [chr(x) for x in range(65, 91, 1)]
    for ch in and_map:
        if len(and_map[ch]) == 1:
            char_to_char[ch] = list(and_map[ch])
            upper_char.remove(ch)
    print(char_to_char)
    for ch in and_map:
        if len(and_map[ch]) > 1:
            char_to_char[ch] = list(and_map[ch] & set(upper_char))
    print(char_to_char)
'''
