from mergesort import mergesort
from binarysearch import binarysearch

"""
Find out if an array contains two elements
whose sum is equal to a given value n.
Sort the array (mergesort -> O(n*lg(n)))
For each element in the array:
	Subtract it from n
	Find the remaining value using binarySearch -> O(lg(n))
"""
def containssum(n, a):
	mergesort(a)
	for i in range(len(a)):
		print("Executed {0} times").format(i)
		v = n - a[i]
		found = binarysearch(a, v)
		if found != None and found != i:
			return True
	return False

myA = [3, 6, 18, 1, 2, 50]
print(containssum(53, myA))