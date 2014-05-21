#!/usr/bin/python 
# Filename: Dijkstra.py 

inf = float('inf') 

class vertex: 
  def __init__(self, start, end, value = inf , distance = inf, isTaken = False): 
    self.start = start 
    self.end = end 
    self.value = value 
    self.distance = distance
    self.isTaken = isTaken 

def Dijkstra(S, G, n, source): 
  G[source][source].distance = 0 
  for i in range(0, n): 
    for j in range(0, n): 
      if G[source][j].isTaken == False: 
        index = j
        break
    for j in range(0, n): 
      if G[source][j].distance < G[source][index].distance and G[source][j].isTaken == False: 
        index = j 
    G[source][index].isTaken = True   # delete vertex[index] from G 
    S.append(G[source][index])        # insert vertex[index] into S 
    for j in range(0, n): 
      if G[source][j].isTaken == False and G[index][j].value < inf:
        availableDistance = G[source][index].distance + G[index][j].value 
        originalDistance = G[source][j].distance 
        G[source][j].distance = availableDistance if availableDistance < originalDistance else originalDistance 

