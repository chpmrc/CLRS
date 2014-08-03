def selectionsort(arr):
    """ At each step i find the smallest element and exchange with the one in position i """
    for i in range(len(arr) - 1):
        mini = i # Assume the current element is the smallest
        j = i + 1
        while j < len(arr): # Search for the actual minimum
            if arr[j] < arr[mini]:
                mini = j
            j += 1
        # Exchange the values
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    return arr

myArr = [-1, 20, 14, 1, 50]
print selectionsort(myArr)