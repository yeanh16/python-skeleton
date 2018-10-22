# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
import sys

##def question05(allowedAllocations, totalValue):
##  amount = [0 for _ in range(totalValue+1)]
##  for amt in range(1, totalValue+1):
##    amount[amt] = sys.maxint
##    temp = sys.maxint
##    for c in range(0, len(allowedAllocations)):
##      if allowedAllocations[c] <= amount:
##        temp_amt = amount[amt-allowedAllocations[c]] + 1
##        if temp_amt < temp:
##          temp = temp_amt
##          amount[amt] = temp
##  return amount[totalValue]

def _get_change_making_matrix(set_of_coins, r):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(r + 1):
        m[0][i] = i
    return m

def question05(coins, n):
    """This function assumes that all coins are available infinitely.
    n is the number to obtain with the fewest coins.
    coins is a list or tuple with the available denominations."""
    m = _get_change_making_matrix(coins, n)
    for c in range(1, len(coins) + 1):
        for r in range(1, n + 1):
            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = 1
            # coins[c - 1] cannot be included.
            # Use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]
            # coins[c - 1] can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] (without
            #      using coins[c - 1]) plus this 1 extra coin.
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
    return m[-1][-1]
