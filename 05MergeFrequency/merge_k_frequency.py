#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 복수의 빈도 파일을 병합하는 프로그램

import sys
import heapq

###############################################################################
def merge_k_sorted_freq(input_files):
    '''
    input_files : list of input filenames (frequency files; 2 column format)
    '''
    fins = []
    k = len(input_files)
    heap = []
    lish = []
    finished = [False for _ in range(k)] # [False] * k
    for file in range(k):
        with open(sys.argv[(k+1)]) as fs:
            for line in fs.readline():
                t = line.split('\t')
                t = tuple(t)
                fins.append(t)

    heapq.heapify(fins)
    for i in fins:
        pendding = heapq.heappop(fins)
        lish.append(pendding)
    for i in lish:
        if i+1 != range(len(lish)):
            if i[0] == lish[(i+1)][0]:
                lish[(i+1)][1] += i[1]
            else:
                heap.append(i)
        else:
            if i[0] == lish[(i+1)][0]:
                i[1] += lish[(i+1)][1]
                heap.append(i)
                break
            else:
                heap.append(lish[(i+1)])
                break

    for terms, freq in heap:
        print( "%s\t%d" %(terms, freq))

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    merge_k_sorted_freq( sys.argv[1:])
