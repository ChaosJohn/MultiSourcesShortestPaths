#!/usr/bin/python 
# Filename: Main_With_Input.py 

import Dijkstra 

def InputG(G): 
  cmd = raw_input("Please Enter The Directly Connected Routes('Enter' For Input, 'n' for Exit): ") 
  while cmd != 'n': 
    start = int(raw_input("\tStart Point: ")) - 1
    end = int(raw_input("\tEnd Point: ")) - 1
    if start == end: 
      print '!' * 20, '\nThe End Point Cannot Be The Same As The Start Point!!!!\n', '!' * 20 
      continue
    value = int(raw_input("\tThe Direct Distance is: ")) 
    G[start][end].value = value 
    cmd = raw_input("Is There Any Routes Available?('Enter' For Input, 'n' for Exit): ")

inf = float('inf') 
G = [] 
n = int(raw_input("Please Enter The Number Of The Vertexs: "))  
for i in range(0, n): 
  G.append([]) 
  for j in range(0, n): 
    G[i].append(Dijkstra.vertex(i, j)) 

InputG(G) 

print '\nThe Available Routes Are List As Follows: '
for i in range(0, n): 
  for j in range(0, n): 
    if G[i][j].value < inf: 
      print '\t[', i + 1, ',', j + 1, '] ==> The Direct Distance is', G[i][j].value 
print 

for i in range(0, n): 
  S = [] 
  Dijkstra.Dijkstra(S, G, n, i) 
  print '## When The Source Vertex is', i + 1, '\n', '*' * 20 
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
