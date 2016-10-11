#!/usr/bin/env python3

import chewing

pinyin_pair = '''\
ㄅ b
ㄆ p
ㄇ m
ㄈ f
ㄉ d
ㄊ t
ㄋ n
ㄌ l
ㄍ g
ㄎ k
ㄏ h
ㄐ j
ㄑ q
ㄒ x
ㄓ zh,zhi
ㄔ ch,chi
ㄕ sh,shi
ㄖ r,ri
ㄗ z,zi
ㄘ c,ci
ㄙ s,si
ㄢ an
ㄣ en
ㄤ ang
ㄥ eng
ㄦ er
一 yi,-i
ㄨ wu,-u
ㄩ yu,-ü,-u
ㄚ a
ㄛ o
ㄜ e
ㄝ ê
ㄞ ai
ㄟ ei
ㄠ ao
ㄡ ou
ㄧㄚ ya,-ia
ㄧㄛ yo
ㄧㄝ ye,-ie
ㄧㄞ yai,-iai
ㄧㄠ yao,-iao
ㄧㄡ you,-iu
ㄧㄢ yan,-ian
ㄧㄣ yin,-in
ㄧㄤ yang,-iang
ㄧㄥ ying,-ing
ㄨㄚ wa,-ua
ㄨㄛ wo,-uo
ㄨㄞ wai,-uai
ㄨㄟ wei,-ui
ㄨㄢ wan,-uan
ㄨㄣ wen,-un
ㄨㄤ wang,-uang
ㄨㄥ weng,-ong
ㄩㄝ yue,-üe,-ue
ㄩㄢ yuan,-üan,-uan
ㄩㄣ yun,-ün,-un
ㄩㄥ yong,-iong\
'''.split('\n')

pinyin_pair = list(map(str.split, pinyin_pair))

pinyin_mapping = { i[0]: i[1].split(',') for i in pinyin_pair }

def translate(s):
    s = chewing.translate(s)
    for zhuyin, pinyin in reversed(pinyin_pair):
        s = s.replace(zhuyin, pinyin.split(',')[0])
    return s

while True:
    try:
        data = input()
    except EOFError:
        break

    if not data:
        break

    print(translate(data))
