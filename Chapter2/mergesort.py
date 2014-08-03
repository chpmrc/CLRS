# import random

"""
Split the given array a into l = a[p, k-1], r = a[k, q]
Scan the two arrays and at each iteration pick the lower value
Append this value to the original array starting from a[0]
If one of the arrays has been scanned completely just copy the
remaining elements in the other one
"""
def merge(a, p, k, q):
	# print("Calling merge with (%d, %d, %d)") % (p, k, q)
	# print("Original array: ", a[p:q+1])
	l = []
	r = []
	lpos = 0
	rpos = 0
	for i in range(p, q+1):
		if (i <= k):
			l.append(a[i])
		else :
			r.append(a[i])

	for i in range(p, q+1):
		if (lpos >= len(l)):
			while (rpos < len(r)):
				a[i] = r[rpos]
				rpos += 1
				i += 1
		elif (rpos >= len(r)):
			while (lpos < len(l)):
				a[i] = l[lpos]
				lpos += 1
				i += 1
		# Generic case
		else:
			if (l[lpos] < r[rpos]):
				a[i] = l[lpos]
				lpos += 1
			else:
				a[i] = r[rpos]
				rpos += 1

	# print("Merged array: ", a[p:q+1])


def mergesortaux(a, p, q):
	# print("Calling mergesort with (%d, %d)") % (p, q)
	half = (p + q) / 2
	if (p < q):
		mergesortaux(a, p, int(half))
		mergesortaux(a, int(half) + 1, q)
	merge(a, p, half, q)

def mergesort(a):
	mergesortaux(a, 0, len(a) - 1)


# tosort = []
# for i in range(10):
# 	tosort.append(random.randint(1, 100))
# print tosort
# mergesort(tosort, 0, len(tosort) - 1)
# print tosort
