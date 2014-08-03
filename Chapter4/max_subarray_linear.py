"""Here we compute shit"""


def find_max_first_subarray(vals, low, high):
    """
    Find the subarray in the form A[0..i]
    """
    summation = 0
    max_summation = None
    max_index = low
    step = 1 if low <= high else -1
    for i in range(low, high, step):
        summation += vals[i]
        if summation > max_summation:
            max_summation = summation
            max_index = i
    return (low, max_index, max_summation)


def find_max_subarray_linear(vals, low, high):
    """Find the maximum subarray in linear time"""
    i = low
    j = high
    first_result = find_max_first_subarray(vals, i, j)
    j = first_result[1]
    second_result = find_max_first_subarray(vals, j+1, i)
    if first_result[2] > second_result[2]:
        return first_result
    else:
        return second_result


MY_VALUES = [0, 5, -1, -2, 7, -1, -5, 7]
# print find_max_first_subarray(MY_VALUES, 0, len(MY_VALUES))
print find_max_subarray_linear(MY_VALUES, 0, len(MY_VALUES))
