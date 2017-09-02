# !/usr/bin/env python
# coding:utf-8
"""
Created by tzw0745 on 2016/11/18.
"""
import re

dic = None


def is_english(sentence, level=0.5):
    global dic
    if not dic:
        with open('dictionary.txt', 'r') as f:
            content = f.read().lower()
        dic = set(re.findall('[a-z]+', content))

    words = set(re.findall('[a-z]+', sentence.lower()))

    return len(words - dic) / len(words) < level


if __name__ == '__main__':
    print(is_english('We are not born with courage,'
                     ' but neither are we born with fear.'))
