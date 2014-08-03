els = [2, 3, 1, 4, 10, 28, 18, 1, 15, 9]


def insertionsort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        # Find the right "hole"
        while j >= 0 and arr[j] > val:
            arr[j+1] = arr[j]
            j -= 1

        # Put the value in the "hole"
        arr[j+1] = val

    return arr

print insertionsort(els)
