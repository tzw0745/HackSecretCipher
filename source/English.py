# !/usr/bin/env python
# coding:utf-8
"""
Created by tzw0745 on 2016/11/18.
"""
import traceback
import re

dic = None


def isEngSen(sentence, level=0.5):
    global dic
    if not dic:
        with open('dictionary.txt', 'r') as f:
            content = f.read().lower()
        dic = set(re.findall('[a-z]+', content))

    words = set(re.findall('[a-z]+', sentence.lower()))

    return len(words - dic) / len(words) < level


def main():
    print(isEngSen('what do you make of this sentence?'))


if __name__ == '__main__':
    splitLine = '-' * 80
    print(splitLine)
    try:
        main()
        print('\nall done')
    except:
        error = traceback.format_exc()
        print(error)
    finally:
        print(splitLine)
        input()
