import queue
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
    
    def getPathBFS(self, sv, ev):

        #Return an empty list if sv and ev is invalid
        if(sv> (self.nVertices-1)) or (ev> (self.nVertices)):
            return list()

        visited= [False for i in range(self.nVertices)]
        return self.__getPathBFS(sv, ev, visited)

    def __getPathBFS(self,sv,ev,visited):
        map={}
        q=queue.Queue()

        if self.adjMatrix[sv][ev]==1 and sv==ev:
            ans=[]
            ans.append(sv)
            return ans
        
        q.put(sv)
        visited[sv]= True

        while q.empty() is False :
            front=q.get()

            for i in range(self.nVertices):
                if self.adjMatrix[front][i] == 1 and visited[i] is False:
                    map[i]= front
                    q.put(i)

                    visited[i]= True

                    if i == ev :
                        ans=[]
                        ans.append(ev)
                        value=map[ev]

                        while value !=sv:
                            ans.append(value)
                            value=map[value]
                        
                        ans.append(value)
                        return ans
        return []    

g=Graph(4)    
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(2,3)
print(g.getPathBFS(1,3))