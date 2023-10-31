#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

_CHO_ = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
_JUNG_ = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
_JONG_ = 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ' # index를 1부터 시작해야 함

# 겹자음 : 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ'
# 겹모음 : 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'

_JAMO2ENGKEY_ = {
 'ㄱ': 'r',
 'ㄲ': 'R',
 'ㄴ': 's',
 'ㄷ': 'e',
 'ㄸ': 'E',
 'ㄹ': 'f',
 'ㅁ': 'a',
 'ㅂ': 'q',
 'ㅃ': 'Q',
 'ㅅ': 't',
 'ㅆ': 'T',
 'ㅇ': 'd',
 'ㅈ': 'w',
 'ㅉ': 'W',
 'ㅊ': 'c',
 'ㅋ': 'z',
 'ㅌ': 'x',
 'ㅍ': 'v',
 'ㅎ': 'g',
 'ㅏ': 'k',
 'ㅐ': 'o',
 'ㅑ': 'i',
 'ㅒ': 'O',
 'ㅓ': 'j',
 'ㅔ': 'p',
 'ㅕ': 'u',
 'ㅖ': 'P',
 'ㅗ': 'h',
 'ㅘ': 'hk',
 'ㅙ': 'ho',
 'ㅚ': 'hl',
 'ㅛ': 'y',
 'ㅜ': 'n',
 'ㅝ': 'nj',
 'ㅞ': 'np',
 'ㅟ': 'nl',
 'ㅠ': 'b',
 'ㅡ': 'm',
 'ㅢ': 'ml',
 'ㅣ': 'l',
 'ㄳ': 'rt',
 'ㄵ': 'sw',
 'ㄶ': 'sg',
 'ㄺ': 'fr',
 'ㄻ': 'fa',
 'ㄼ': 'fq',
 'ㄽ': 'ft',
 'ㄾ': 'fx',
 'ㄿ': 'fv',
 'ㅀ': 'fg',
 'ㅄ': 'qt'
}


###############################################################################
def is_hangeul_syllable(ch):
    '''한글 음절인지 검사
    '''
    if not isinstance(ch, str):
        return False
    elif len(ch) > 1:
        ch = ch[0]
    
    return 0xAC00 <= ord(ch) <= 0xD7A3

###############################################################################
def compose(cho, jung, jong):
    '''초성, 중성, 종성을 한글 음절로 조합
    cho : 초성
    jung : 중성
    jong : 종성
    return value: 음절
    '''
    if not (0 <= cho <= 18 and 0 <= jung <= 20 and 0 <= jong <= 27):
        return None
    code = (((cho * 21) + jung) * 28) + jong + 0xAC00

    return chr(code)

###############################################################################
# input: 음절
# return: 초, 중, 종성
def decompose(syll):
    '''한글 음절을 초성, 중성, 종성으로 분해
    syll : 한글 음절
    return value : tuple of integers (초성, 중성, 종성)
    '''
    if not is_hangeul_syllable(syll):
        return (None, None, None)
    
    uindex = ord(syll) - 0xAC00
    
    jong = uindex % 28
    jung = ((uindex - jong) // 28) % 21
    cho = ((uindex - jong) // 28) // 21

    return (cho, jung, jong)

###############################################################################
def str2jamo(str):
    '''문자열을 자모 문자열로 변환
    '''
    jamo = []
    for ch in str:
        if is_hangeul_syllable(ch):
            cho, jung, jong = decompose(ch)
            jamo.append( _CHO_[cho])
            jamo.append( _JUNG_[jung])
            if jong != 0:
                jamo.append( _JONG_[jong-1])
        else:
            jamo.append(ch)
    return ''.join(jamo)

###############################################################################
def jamo2engkey(str):
    engkey = []
    for ch in str:
        if is_hangeul_syllable(ch):
            engkey.append(_JAMO2ENGKEY_[ch])
        else:
            engkey.append(ch)
    return ''.join(engkey)

###############################################################################
def engkey2jamo(str):
    _ENGKEY2JAMO_ = {v: k for k, v in _JAMO2ENGKEY_.items()}
    jamo = []
    for ch in str:
        if is_hangeul_syllable(ch):
            jamo.append(_ENGKEY2JAMO_[ch])
        else:
            jamo.append(ch)
    return ''.join(jamo)

###############################################################################
def chang_p(str):
    comb={'ㅗㅏ': 'ㅘ','ㅗㅐ': 'ㅙ','ㅗㅣ': 'ㅚ','ㅜㅓ': 'ㅝ','ㅜㅔ': 'ㅞ','ㅜㅣ': 'ㅟ','ㅡㅣ': 'ㅢ','ㄱㅅ': 'ㄳ','ㄴㅈ': 'ㄵ','ㄴㅎ': 'ㄶ','ㄹㄱ': 'ㄺ','ㄹㅁ': 'ㄻ','ㄹㅂ': 'ㄼ','ㄹㅅ': 'ㄽ','ㄹㅌ': 'ㄾ','ㄹㅍ': 'ㄿ','ㄹㅎ': 'ㅀ','ㅂㅅ': 'ㅄ'}
    typejamo =''
    wordl =[]
    for ch in str:
        if ch in _CHO_:
            typejamo += 'c'
        elif ch in _JUNG_:
            typejamo += 'u'
        else:
            typejamo += 'X'
        # The only 'c' before any 'u' should be the 초성!!!
        # For a word, as least there will be 'cu' or 'cuu' in it.
    typejamo = typejamo.replace('cu', 'SCU').replace('cuu', 'SCUU')
    tword = typejamo.split('S')
    for i in tword:
        a = tword.index(i)
        b = len(i)
        wordi = str[a:(a + b + 1)]
        wordl.append(wordi)

    for i in range(len(tword)):
        choi = wordl[i][0]
        if 'UU' in tword[i]:
            jungi = comb[wordl[i][1:3]]
            if 'cc' in tword[i]:
                jongi = comb[wordl[i][3:]]
            else:
                jongi = wordl[i][3:]
        if 'UU' not in tword[i] and 'U' in tword[i]:
            jungi = wordl[i][1]
            if 'cc' in tword[i]:
                jongi = comb[wordl[i][2:]]
            else:
                jongi = wordl[i][2:]
        t = (choi, jungi, jongi)
        wordl[i] = decompose(t)

    return ''.join(wordl)

###############################################################################
def jamo2syllable(str):
    syll = []
    list_p = []
    pendding = ''
    for ch in str:
        if is_hangeul_syllable(ch):
            pendding += ch
        else:
            if pendding == '':
                list_p.append(ch)
            else:
                list_p.append(pendding)
                pendding = ''

    for i in list_p:
        if len(i) == 1:
            syll.append(i)
        else:
            pendded = chang_p(i)
            syll.append(pendded)

    return ''.join(syll)

###############################################################################
if __name__ == "__main__":
    
    i = 0
    line = sys.stdin.readline()

    while line:
        line = line.rstrip()
        i += 1
        print('[%06d:0]\t%s' %(i, line)) # 원문
    
        # 문자열을 자모 문자열로 변환 ('닭고기' -> 'ㄷㅏㄺㄱㅗㄱㅣ')
        jamo_str = str2jamo(line)
        print('[%06d:1]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 키입력 문자열로 변환 ('ㄷㅏㄺㄱㅗㄱㅣ' -> 'ekfrrhrl')
        key_str = jamo2engkey(jamo_str)
        print('[%06d:2]\t%s' %(i, key_str)) # 키입력 문자열
        
        # 키입력 문자열을 자모 문자열로 변환 ('ekfrrhrl' -> 'ㄷㅏㄹㄱㄱㅗㄱㅣ')
        jamo_str = engkey2jamo(key_str)
        print('[%06d:3]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 음절열로 변환 ('ㄷㅏㄹㄱㄱㅗㄱㅣ' -> '닭고기')
        syllables = jamo2syllable(jamo_str)
        print('[%06d:4]\t%s' %(i, syllables)) # 음절열

        line = sys.stdin.readline()
