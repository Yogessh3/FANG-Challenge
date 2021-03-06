'''DFS in an Undirected Graph
Time-O(V+E) / Space-O(V+E)
Graph
1
 \
  3
   \
    2
   / \
  4   9
 / \
7   6
'''
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def DFS(self,u,visited):
        print(u,end=" ")
        visited[u]=True
        for i in self.graph[u]:
            if(visited[i]==False):
                self.DFS(i,visited)
    def depthFirstSearch(self,vertices):
        visited={}
        for i in vertices:
            visited[i]=False
        for i in self.graph:
            if(visited[i]==False):
                self.DFS(i,visited)
g=Graph(5)
vertices=[1,2,3,4,6,7,9]
edges=[[1,3],[3,2],[2,4],[4,7],[7,9],[2,9],[4,6]]
for i in edges:
    g.addEdge(i[0],i[1])
g.depthFirstSearch(vertices)
