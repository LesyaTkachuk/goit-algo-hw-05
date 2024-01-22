def binary_search_extended(array, value):
    low = 0
    hight = len(array) - 1
    count = 0

    if value > array[hight]:
        return (count, None)

    while low <= hight:
        middle = (hight + low) // 2
        count += 1

        if array[middle] == value:
            return (count, array[middle])
        if value < array[middle]:
            hight = middle - 1
        if value > array[middle]:
            low = middle + 1

    closest_value = array[middle + 1] if array[middle] < value else array[middle]

    return (count, closest_value)


if __name__ == "__main__":
    # binary search testing
    print(
        binary_search_extended(
            [0.1, 0.2, 0.3, 0.5, 0.8, 1.4, 2.5, 3.7, 4.9, 5.99, 6.5, 7.88], 0.8
        )
    )
    print(
        binary_search_extended(
            [0.1, 0.2, 0.3, 0.5, 0.8, 1.4, 2.5, 3.7, 4.9, 5.99, 6.5, 7.88], 0.4
        )
    )
    print(
        binary_search_extended(
            [0.1, 0.2, 0.3, 0.5, 0.8, 1.4, 2.5, 3.7, 4.9, 5.99, 6.5, 7.88], 10
        )
    )
    print(
        binary_search_extended(
            [0.1, 0.2, 0.3, 0.5, 0.8, 1.4, 2.5, 3.7, 4.9, 5.99, 6.5, 7.88], -0.1
        )
    )
