from random import randint
from typing import List


def bubble_sort(series: List[int]):
    for i, number_a in enumerate(series[:-1]):

        # print(i, end=' ')
        if series[i] > series[i+1]:
            n = series[i]
            series[i] = series[i+1]
            series[i+1] = n

        for j, number_b in enumerate(series[:-1]):
            if series[-j] < series[-j-1]:
                n = series[-j]
                series[-j] = series[-j-1]
                series[-j-1] = n

    return series


if __name__ == "__main__":
    limit = 99
    number_series = [randint(0, limit) for i in range(limit)]

    for i in number_series:
        print(i, end=' ')

    sorted_number_series = bubble_sort(number_series)

    print('\n====================\n')
    for i in sorted_number_series:
        print(i, end=' ')
