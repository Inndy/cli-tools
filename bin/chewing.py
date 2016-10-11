#!/usr/bin/env python3

__all__ = [ 'translate', 'translation_table' ]

chewing_map_0  = '1	q	a	z	2	w	s	x	'
chewing_map_1  = 'ㄅ	ㄆ	ㄇ	ㄈ	ㄉ	ㄊ	ㄋ	ㄌ	'
chewing_map_0 += '3	e	d	c	4	r	f	v	'
chewing_map_1 += 'ˇ	ㄍ	ㄎ	ㄏ	ˋ	ㄐ	ㄑ	ㄒ	'
chewing_map_0 += '5	t	g	b	6	y	h	n	'
chewing_map_1 += 'ㄓ	ㄔ	ㄕ	ㄖ	ˊ	ㄗ	ㄘ	ㄙ	'
chewing_map_0 += '7	u	j	m	8	i	k	,	'
chewing_map_1 += '˙	一	ㄨ	ㄩ	ㄚ	ㄛ	ㄜ	ㄝ	'
chewing_map_0 += '9	o	l	.	0	p	;	/	'
chewing_map_1 += 'ㄞ	ㄟ	ㄠ	ㄡ	ㄢ	ㄣ	ㄤ	ㄥ	'
chewing_map_0 += '-'
chewing_map_1 += 'ㄦ'
chewing_map_0 = chewing_map_0.replace('\t', '')
chewing_map_1 = chewing_map_1.replace('\t', '')

translation_table = str.maketrans(chewing_map_0, chewing_map_1)

def translate(s):
    return s.translate(translation_table)

if __name__ == '__main__':
    while True:
        try:
            data = input()
        except EOFError:
            break
        print(data.translate(translation_table))
