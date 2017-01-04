from math import log
from operator import mod

def repeat_square(a, b):
    c = 0
    d = 1
    bk = bin(b)[2:]
    i = len(bk) - 1
    while i >= 0:
        c = 2 * c
        d = d * d
        if bk[i] == '1':
            c += 1
            d = d * a
        i -= 1
    return d

def modular_exponentiation(a,b,n):
	''' raising to powers with repeated squaring and get modular_exponentiation'''
	c = 0
	d = 1
	bk = bin(b)[2:]
	i = len(bk) - 1
	while i >= 0:
		c = 2*c
		d = mod((d*d), n)
		if bk[i] == 1:
			c += 1
			d = mod((d * a), n)
		i -= 1
	return d




