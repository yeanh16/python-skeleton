# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  maxeval = 0
  n = len(portfolios)
  for i in range(n):
    for j in range(i+1,n):
      curvalue = portfolios[i] ^ portfolios[j]
      if curvalue > maxeval:
        maxeval = curvalue
    
  return maxeval
