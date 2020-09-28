'''BFS in an Undirected Graph
Time-O(V+E) / Space-O(V+E)
Graph
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
    def BFS(self,source,visited):
        queue=[]
        queue.append(source)
        visited[source]=True
        while queue:
            currentNode=queue.pop(0)
            print(currentNode,end=" ")
            for node in self.graph[currentNode]:
                if(visited[node]==False):
                    queue.append(node)
                    visited[node]=True
g=Graph(5)
visited={}
vertices=[2,4,6,7,9]
for i in vertices:
    visited[i]=False
edges=[[2,4],[4,7],[7,9],[2,9],[4,6]]
for i in edges:
    g.addEdge(i[0],i[1])
source=2
g.BFS(source,visited)


            
                
                
        
