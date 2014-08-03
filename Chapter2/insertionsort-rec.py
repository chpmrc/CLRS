"""
In insertion sort we select an element and we find its correct
position in the array. Here we do it recursively assuming that
a[0, n-2] is already sorted.
"""
def insertionsortRec(a, n):
    print a[0:n]
    # We avoid "index out of range" by taking 2 as base case
    if (n > 2):
        insertionsortRec(a, n-1)
    # Actual sorting
    pos = n-1
    el = a[pos]
    # We go from the last element before el to the first
    for i in range(n-2, -1, -1):
        if (a[i] > el):
            # Swap the two elements
            tmp = a[i]
            a[i] = el
            a[pos] = tmp
            pos -= 1
    try:
        print (a[0:n], a[n])
    except:
        pass


# a = [5, 2, 3, 1, 10, 4]
# print("Original array: ", a)
# insertionsortRec(a, len(a))
# print("Sorted array: ", a)
