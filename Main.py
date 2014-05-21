#!/usr/bin/python 
# Filename: Main.py 

import Dijkstra 

inf = float('inf') 
G = [] 
n = 5 
for i in range(0, n): 
  G.append([]) 
  for j in range(0, n): 
    G[i].append(Dijkstra.vertex(i, j)) 

G[0][1].value = 10 
G[1][2].value = 50 
G[0][3].value = 30 
G[0][4].value = 100 
G[2][4].value = 10 
G[3][2].value = 20 
G[3][4].value = 60 

print 'The Available Routes Are List As Follows: '
for i in range(0, n): 
  for j in range(0, n): 
    if G[i][j].value < inf: 
      print '\t[', i + 1, ',', j + 1, '] ==> The Direct Distance is', G[i][j].value 
print 

for i in range(0, n): 
  S = [] 
  Dijkstra.Dijkstra(S, G, n, i) 
  print 'When The Source Vertex is', i + 1, '\n', '*' * 20 
  isEmpty = True
  for j in range(1, n): 
    if S[j].distance < inf: 
      isEmpty = False
  if isEmpty == True: 
    print '\tThis Vertex Cannot Be The Source\n', '*' * 20, '\n'
    break
  for j in range(1, n): 
    if S[j].distance < inf: 
      print '\t[', i + 1, ',', S[j].end + 1, '] ==> The Shortest Distance is', S[j].distance 
  print '*' * 20, '\n'
