_MIN_MERGE = 32


def _find_minrun(n: int):
    r = 0
    while n >= _MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


def _insertion_sort(arr: list, start_index: int, end_index: int):
    for i in range(start_index + 1, end_index + 1):
        j = i
        while j > start_index and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def _merge(arr: list, left_index: int, mid_index: int, right_index: int):
    left_arr = arr[left_index:mid_index]
    right_arr = arr[mid_index : right_index + 1]
    left_arr_len, right_arr_len = len(left_arr), len(right_arr)

    left_arr_iterator, right_arr_iterator, arr_iterator = 0, 0, left_index

    while left_arr_iterator < left_arr_len and right_arr_iterator < right_arr_len:
        if left_arr[left_arr_iterator] <= right_arr[right_arr_iterator]:
            arr[arr_iterator] = left_arr[left_arr_iterator]
            left_arr_iterator += 1
        else:
            arr[arr_iterator] = right_arr[right_arr_iterator]
            right_arr_iterator += 1

        arr_iterator += 1

    arr += left_arr[left_arr_iterator:] + right_arr[right_arr_iterator:]


def sort(arr: list):
    new_arr = arr[:]
    arr_len = len(arr)
    minrun = _find_minrun(arr_len)

    for start_index in range(0, arr_len, minrun):
        end_index = min(start_index + minrun - 1, arr_len - 1)
        _insertion_sort(new_arr, start_index, end_index)

    size = minrun
    while size < arr_len:
        for left_index in range(0, arr_len, size * 2):
            mid_index = min(arr_len - 1, left_index + size - 1) + 1
            right_index = min((left_index + 2 * size - 1), (arr_len - 1))
            _merge(new_arr, left_index, mid_index, right_index)

        size *= 2

    return new_arr
