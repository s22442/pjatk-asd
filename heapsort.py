_heap_size = None


def _heapify_left_index(index: int):
    return 2 * index + 1


def _heapify_right_index(index: int):
    return _heapify_left_index(index) + 1


def _heapify(arr: list, index: int):
    global _heap_size

    left_index = _heapify_left_index(index)
    right_index = _heapify_right_index(index)

    largest_value_index = index

    if left_index < _heap_size and arr[left_index] > arr[index]:
        largest_value_index = left_index

    if right_index < _heap_size and arr[right_index] > arr[largest_value_index]:
        largest_value_index = right_index

    if largest_value_index != index:
        arr[index], arr[largest_value_index] = arr[largest_value_index], arr[index]
        _heapify(arr, largest_value_index)


def _build_max_heap(arr: list):
    global _heap_size

    _heap_size = len(arr)

    for i in range((len(arr) - 1) // 2, -1, -1):
        _heapify(arr, i)


def sort(arr: list):
    global _heap_size

    new_arr = arr[:]

    _build_max_heap(new_arr)

    for i in range((len(new_arr) - 1), 0, -1):
        new_arr[i], new_arr[0] = new_arr[0], new_arr[i]
        _heap_size -= 1
        _heapify(new_arr, 0)

    return new_arr
