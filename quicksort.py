def _partition(arr: list, start_index: int, end_index: int):
    partition_index = start_index - 1

    for i in range(start_index, end_index):
        if arr[i] <= arr[end_index]:
            partition_index += 1
            arr[partition_index], arr[i] = arr[i], arr[partition_index]

    arr[partition_index + 1], arr[end_index] = arr[end_index], arr[partition_index + 1]

    return partition_index + 1


def _qsort(arr: list, start_index: int, end_index: int):
    if start_index < end_index:
        i = _partition(arr, start_index, end_index)
        _qsort(arr, start_index, i - 1)
        _qsort(arr, i + 1, end_index)


def sort(arr: list):
    new_arr = arr[:]
    _qsort(new_arr, 0, len(new_arr) - 1)
    return new_arr
