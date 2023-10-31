#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import get_morphs_tags as mf
import get_index_terms as term

###############################################################################
def word_count_by_year(word_count, filename, index, size):
    '''
    word_count: dictionary (key: word, value: frequency list)
    filename : 형태소 분석 파일
    index : 연도 인덱스 2000->0, 2001->1, ...
    size : 연도의 총 수
    '''

    with open(filename) as fin:

        mt_freq = {}
        wordlist = []

        for line in fin.readlines():

            segments = line.split('\t')

            if len(segments) < 2:
                continue

            result = mf.get_morphs_tags(segments[1].rstrip())

            a = term.get_index_terms(result)

            for i in a:
                wordlist.append(i)

    for word in wordlist:
        if word not in word_count:
            word_count[word] = [0] * (index + 1)

        if len(word_count[word]) != (index + 1):
            word_count.setdefault(word, []).append(0)

        word_count[word][index] += 1


###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    word_count = {}

    for i, filename in enumerate(sys.argv[1:]):
        word_count_by_year( word_count, filename, i, len(sys.argv[1:]))

    while True:
        query = input('검색할 단어를 입력하세요(type "exit" to exit): ')

        if query == "exit":
            break
        
        if query in word_count:
            print(word_count[query])
        else:
            print("결과가 없습니다.")
    