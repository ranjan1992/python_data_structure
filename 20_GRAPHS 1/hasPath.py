import queue

class Graph:
    def __init__(self, nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def removeEdge(self):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
    
    def containsEdge(self, v1, v2):
        if self.adjMatrix[v1][v2]>0:
            return True
        else:
            return False
    
    def __str__(self):
        return str(self.adjMatrix)
    
    def hasPath(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPath(sv, ev, visited)
    
    def __hasPath(self, sv, ev, visited):
        if sv==ev:
            return True
        
        q= queue.Queue()
        q.put(sv)
        visited[sv]= True

        while q.empty() is False:
            u=q.get()

            for i in range(self.nVertices):
                if self.adjMatrix[u][i]==1 and visited[i] is False:
                    if i==ev:
                        return True
                    
                    q.put(i)
                    visited[i]= True
        return False
                

g= Graph(4)

g.addEdge(0,1)
g.addEdge(1,2)

print(g.hasPath(0,3))