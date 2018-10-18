# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
import sys

def question05(allowedAllocations, totalValue):
  amount = [0 for _ in range(totalValue+1)]
  for amt in range(1, totalValue+1):
    amount[amt] = sys.maxint
    temp = sys.maxint
    for c in range(0, len(allowedAllocations)):
      if allowedAllocations[c] <= amount:
        temp_amt = amount[amt-allowedAllocations[c]] + 1
        if temp_amt < temp:
          temp = temp_amt
          amount[amt] = temp
  return amount[totalValue]
