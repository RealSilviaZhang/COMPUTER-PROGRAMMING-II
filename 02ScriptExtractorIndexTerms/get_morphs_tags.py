#!/usr/bin/env python3
# coding: utf-8

import sys

def get_morphs_tags(tagged):
    result = []
    while len(tagged) > 0:
        if '+' in tagged:
            pending_index = tagged.find('+')
            if pending_index != 0:
                pending = tagged[:pending_index]
            else:
                pending = '+/SW'
        else:
            pending = tagged
        if pending =='+/SW':
            tagged = tagged[5:]
            tuple1 = tuple(['+', 'SW'],)
            result.append(tuple1)
        elif pending == '//SP':
            tagged = tagged[5:]
            tuple1 = tuple(['/', 'SP'],)
            result.append(tuple1)
        else:
            elem = pending.split('/')
            tuple1 = tuple(elem,)
            result.append(tuple1)
            tagged = tagged[len(pending)+1:]

    return result
###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1]) as fin:

        for line in fin.readlines():

            # 2 column format
            segments = line.split('\t')

            if len(segments) < 2: 
                continue

            # result : list of tuples
            result = get_morphs_tags(segments[1].rstrip())
        
            for morph, tag in result:
                print(morph, tag, sep='\t')
