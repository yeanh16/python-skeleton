# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
import sys

## input: [3,1,[[0,7,4],[7,0,2],[4,2,0]] output: 6
## number of servers and target server



def question06(numServers, targetServer, times):
  Q = [i for i in range(numServers)]
  dist = [sys.maxint for _ in range(numServers)]
  prev = [-1 for _ in range(numServers)]

  dist[0] = 0

  while Q:
    minNode = findMinNode(Q,dist) #minNode is the index of the server that has min distance
    if minNode == targetServer:
      return dist[minNode]
    
    Q.remove(minNode)

    for index, time in enumerate(times[minNode]):
      if index in Q:
        alt = dist[minNode] + time
        if alt < dist[index]:
          dist[index] = alt
          prev[index] = minNode
    
  return dist

def findMinNode(Q,dist):
  minNode = -1
  minDistance = sys.maxint
  for q in Q:
    if dist[q] < minDistance:
      minDistance = dist[q]
      minNode = q
  return minNode
                  
##  # modify and then return the variable below
##  for time in times[0]:
##    v = (0,time)    
##  Q = [v] + [(0,sys.maxint) for _ in range(numServers-1)]
##  dict(Q)
##  visited = List()
##  
##  
##  while Q:
##    minnode = min(Q, key = Q.get)
##
##    if minnode == targetServer:
##      return Q.get(minnode)
##    
##    del Q[u]
####    visited.append(u[0])
##    
##    
##    for index, connection in enumerate(times[u[0]]):
##      alt = u[1] + connection
##      if alt < Q


  
