def binarize(b):
	bina=[]
	while b:
		bina.append(b%2)
		b = b//2
	bina.reverse()
	return bina

def modular_exponentiation(a, b, n):
	c = 0
	d = 1
	bina = binarize(b)
	k = len(bina)
	for i in range(0, k):
		c = 2 * c
		d = (d * d) % n
		if bina[i] == 1:
			c = c + 1
			d = (d * a) % n
	return d




