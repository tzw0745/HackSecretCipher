# coding:utf-8
import re
from collections import defaultdict
from functools import reduce

_filename_cache = None
words_set = None
pattern_map = None
_word_pattern_cache = {}


def _read_words(filename, encoding='ascii'):
    global _filename_cache, words_set, pattern_map
    if _filename_cache == filename and words_set and pattern_map:
        return

    with open(filename, 'r', encoding=encoding) as f:
        content = f.read().lower()
    words_set = set(re.findall(r'[a-z]+', content))
    pattern_map = defaultdict(set)
    for _word in words_set:
        pattern_map[word_pattern(_word)].add(_word)
    _filename_cache = filename


def is_english(sentence: str, level=0.75, words_file='words_45k.txt'):
    """
    判断一串字符串是否是英语句子
    :param sentence: 目标字符串
    :param level: 判断阀值：目标字符串中存在英语单词与所有单词的比例
    :param words_file: 单词来源文件
    :return: 判断结果
    """
    if not isinstance(sentence, str) or not isinstance(words_file, str):
        raise TypeError('Param "sentence" and "words_file" must be str')
    if not isinstance(level, float):
        raise TypeError('Param "level" must be float')
    if level > 1 or not sentence:
        return False
    if level <= 0:
        return True

    _read_words(words_file)
    global words_set

    _words = set(re.findall('[a-z]+', sentence.lower()))
    return len(_words & words_set) / len(_words) >= level \
        if len(_words) else False


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

    word = word.lower()
    global _word_pattern_cache
    if word in _word_pattern_cache:
        return _word_pattern_cache[word]

    chs = sorted(set(word), key=word.index)
    pattern = '.'.join(str(chs.index(ch)) for ch in word)

    _word_pattern_cache[word] = pattern
    return pattern


def pattern_words(p: str, words_file='words_45k.txt'):
    """
    获取属于该模式的英语单词
    :param p: 模式，如0.1.1.2.3
    :param words_file: 单词来源文件
    :return: 英语单词列表
    """
    if not isinstance(p, str) or not isinstance(words_file, str):
        raise TypeError('Param "p" and "words_file" must be str')

    _read_words(words_file)
    global pattern_map

    return pattern_map[p]


if __name__ == '__main__':
    print(is_english('We are not born with courage,'
                     ' but neither are we born with fear.'))
