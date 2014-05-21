for i = 1 to n
  // choose the closet vertex u to source s from G judged by the [.d]
  // insert u into S and delete u from G
  // if there exists one vertex that can be directly reached from u and the distance[s -> u -> x] is shorter than that stored in x.d, then change the x.d 
