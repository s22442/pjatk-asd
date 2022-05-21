def sort(arr: list):
    if len(arr) <= 1:
        return arr

    split_index = len(arr) // 2

    right_arr = sort(arr[split_index:])
    left_arr = sort(arr[:split_index])

    new_arr = []

    while len(right_arr) > 0 and len(left_arr) > 0:
        if right_arr[0] < left_arr[0]:
            new_arr.append(right_arr.pop(0))
        else:
            new_arr.append(left_arr.pop(0))

    if len(right_arr):
        new_arr += right_arr
    else:
        new_arr += left_arr

    return new_arr
