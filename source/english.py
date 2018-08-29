# !/usr/bin/env python
# coding:utf-8
"""
Created by tzw0745 on 2016/11/18.
"""
import re

dictionary = None


def is_english(sentence, level=0.5):
    global dictionary
    if not dictionary:
        with open('dictionary.txt', 'r', encoding='ascii') as f:
            content = f.read().lower()
        dictionary = set(re.findall('[a-z]+', content))

    words = set(re.findall('[a-z]+', sentence.lower()))

    return len(words - dictionary) / len(words) < level\
        if len(words) else False


if __name__ == '__main__':
    print(is_english('We are not born with courage,'
                     ' but neither are we born with fear.'))
