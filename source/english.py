# coding:utf-8
import re
from collections import defaultdict

# with open('words_alpha.txt', 'r', encoding='ascii') as f:
with open('dictionary.txt', 'r', encoding='ascii') as f:
    content = f.read().lower()
    dictionary = set(re.findall('[a-z]+', content))


def is_english(sentence: str, level=0.75):
    """
    判断一串字符串是否是英语句子
    :param sentence: 目标字符串
    :param level: 判断阀值：目标字符串中存在英语单词与所有单词的比例
    :return: 判断结果
    """
    if not isinstance(sentence, str):
        raise TypeError('Param "sentence" must be str')
    if not isinstance(level, float):
        raise TypeError('Param "level" must be float')
    if level > 1 or not sentence:
        return False
    if level <= 0:
        return True

    words = set(re.findall('[a-z]+', sentence.lower()))
    return len(words & dictionary) / len(words) >= level \
        if len(words) else False


def word_pattern(word: str):
    """
    获取英语单词的模式：apple->0.1.1.2.3，pen->0.1.2
    :param word: 英语单词
    :return: 模式，字符串
    """
    if not isinstance(word, str):
        raise TypeError('Param "word" must be str')
    if not word.isalpha():
        raise ValueError('Param "word" must be alpha str')
    _c_list = list()
    for ch in word.lower():
        if ch not in _c_list:
            _c_list.append(ch)
    return '.'.join(map(lambda _c: str(_c_list.index(_c)), word))


pattern_dict = defaultdict(list)
for _word in dictionary:
    pattern_dict[word_pattern(_word)].append(_word)


def pattern_words(p: str):
    """
    获取属于该模式的英语单词
    :param p: 模式，如0.1.1.2.3
    :return: 英语单词列表
    """
    if not isinstance(p, str):
        raise TypeError('Param "p" must be str')
    return pattern_dict[p]


if __name__ == '__main__':
    print(is_english('We are not born with courage,'
                     ' but neither are we born with fear.'))
