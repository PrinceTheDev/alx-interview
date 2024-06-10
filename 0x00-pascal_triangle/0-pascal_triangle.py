#!/usr/bin/python3


def pascal_traingle(n):
    """ Returns a list of integers representing the
        Pascal Triangle
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            c = k[i - 1]
            temp.append(k[i -1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k
