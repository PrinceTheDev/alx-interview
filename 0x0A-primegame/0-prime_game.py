#!/usr/bin/python3
"""
This project contains a prime game which helps in technical interviews
"""

def isWinner(x, nums):
    # Helper function to find all primes up to max_num using Sieve of Eratosthenes
    def sieve(max_num):
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
        p = 2
        while (p * p <= max_num):
            if (is_prime[p] == True):
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        primes = [p for p, prime in enumerate(is_prime) if prime]
        return primes, is_prime

    # Maximum possible value of n
    max_n = max(nums) if nums else 0

    # Generate all primes up to the maximum number in nums
    primes, is_prime = sieve(max_n)

    # Initialize win counters
    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        # If n is 1, Ben wins because Maria can't make a move
        if n == 1:
            ben_wins += 1
            continue
        
        # Set of remaining numbers
        remaining = set(range(1, n + 1))
        
        # Simulate the game
        turn = 0  # 0 for Maria's turn, 1 for Ben's turn
        while True:
            # Find the smallest prime in the remaining set
            move_made = False
            for prime in primes:
                if prime > n:
                    break
                if prime in remaining:
                    move_made = True
                    # Remove the prime and its multiples from the set
                    for multiple in range(prime, n + 1, prime):
                        if multiple in remaining:
                            remaining.remove(multiple)
                    break

            if not move_made:
                # No more moves can be made
                if turn == 0:
                    ben_wins += 1  # Maria's turn, but she cannot move
                else:
                    maria_wins += 1  # Ben's turn, but he cannot move
                break
            
            # Switch turn
            turn = 1 - turn

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
