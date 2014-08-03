"""
Assume the array is sorted.
At each step we can exclude half of the (sub)array
in which, for sure, we won't find the element we are looking for.
"""
def binarysearchaux(a, e, p, q):
    # print (a, e, p, q)
    if (q < p):
        return None
    halfInd = (p + q) / 2
    halfEl = a[halfInd]
    if halfEl == e:
        return halfInd
    elif e > halfEl:
        return binarysearchaux(a, e, halfInd + 1, q)
    else:
        return binarysearchaux(a, e, p, halfInd - 1)


def binarysearch(a, e):
    return binarysearchaux(a, e, 0, len(a) - 1)

# a = [1, 3, 5, 7, 9]
el = binarysearch(a, 9, 0, len(a) - 1)
# print el
