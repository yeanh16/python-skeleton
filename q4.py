# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
import sys

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  # modify and then return the variable below
  fixed = False
  mintime = sys.maxint
  for row in rows:
    for machine in row:
      pair = countBrokenSum(row)
      if pair[0] == numberMachines:
        if pair[1] < mintime:
          mintime = pair[1]
          fixed = True

  if fixed:
    return mintime
  else:
    return 0

##returns a pair (nbroken, sumoffix)
def countBrokenSum(row):
  count = 0;
  fixtime = 0;
  for machine in row:
    if machine != 'X':
      count = count + 1
      fixtime = fixtime + int(machine)
      
  return (count,fixtime)
