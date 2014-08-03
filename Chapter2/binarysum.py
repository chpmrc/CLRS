def add(a, b):
	# Assuming len(a) = len(b)
	c = []
	for i in range(0, len(a) + 1):
		c.append(0)
	carry = 0

	for i in reversed(range(0, len(a))):
		cIndex = i+1
		c[cIndex] = a[i] + b[i] + carry

		if c[cIndex] == 3:
			c[cIndex] = 1
			carry = 1
		elif c[cIndex] == 2:
			c[cIndex] = 0
			carry = 1
		elif c[cIndex] == 1:
			carry = 0

		c[0] = carry

	return c

b1 = [0, 1, 1, 1, 1, 0]
b2 = [0, 1, 1, 1, 1, 0]
c = add(b1, b2)
print c
