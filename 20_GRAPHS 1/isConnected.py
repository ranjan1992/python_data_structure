import queue
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(nVertices)] for j in range(nVertices)]
    
    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1
    
    def removeEdge(self):
        if self.containsEdge(v1, v2) is False :
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2] > 0:
            return True
        else: 
            return False
        
    def __str__(self):
        return str(self.adjMatrix)
    
    def isConnected(self, sv):
        visited = [False for i in range(self.nVertices)]
        self.__isConnected(sv, visited)
        for i in range(self.nVertices):
            if visited[i] is False:
                return False
        return True
    
    def __isConnected(self,sv, visited):
        if sv==self.nVertices:
            return
        visited[sv]= True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i] and visited[i] is False:
                self.__isConnected(i, visited)

g=Graph(4)
g.addEdge(0,1)
g.addEdge(0,3)


print(g.isConnected(0))

