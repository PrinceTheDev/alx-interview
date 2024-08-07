#!/usr/bin/python3
"""
This project contains a prime game which helps in technical interviews
"""


def isWinner(x, nums):
    """Function to determine the winner of the prime game"""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for p in range(2, int(max_num ** 0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, max_num + 1, p):
                primes[multiple] = False

    winners = [False] * (max_num + 1)

    for i in range(2, max_num + 1):
        for p in range(2, i + 1):
            if primes[p] and not winners[i - p]:
                winners[i] = True
                break

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if winners[num]:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
