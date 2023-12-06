#!/usr/bin/python3
"""
Prime Game
Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
"""

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        return [i for i in range(2, n + 1) if is_prime(i)]

    def play_round(n):
        primes = get_primes_up_to_n(n)
        player = "Maria"

        while n > 1:
            move = primes[0]
            n -= move

            if player == "Maria":
                player = "Ben"
            else:
                player = "Maria"

            primes = [p for p in primes if p > move or (move % p != 0)]

        return player

    maria_wins = 0
    ben_wins = 0

    for round_num, n in enumerate(nums):
        winner = play_round(n)

        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
