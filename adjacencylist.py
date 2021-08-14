# adjacencyList = {}

#                          A                  B
#                            ----------------
#                           |                 \
#                           |                  \
#                           |                    C
#                           |                  /
#                           |                 /
#                           D                 E
#                            ----------------

# vertices = [ 'A', 'B', 'C', 'D', 'E']
# for i in vertices:
#     adjacencyList[i] = []
# adjacencyList['A'].append('B')
# adjacencyList['A'].append('D')
# print(adjacencyList)
class Graph:
    def __init__(self,vertices):
        self.verticesList = vertices
        self.adjacencyList = {}
        for nodes in self.verticesList:
            self.adjacencyList[nodes] =[]
    def print_adjList(self):
        return self.adjacencyList
    def add_Edge(self,fro,to):
        self.adjacencyList[fro].append(to)
        self.adjacencyList[to].append(fro)
    def getNodeDegree(self,node):
        return len(self.adjacencyList[node])

mygraphObject = Graph(['A', 'B','C','D','E'])
mygraphObject.add_Edge('A','B')
mygraphObject.add_Edge('A','D')
mygraphObject.add_Edge('B','C')
mygraphObject.add_Edge('D','E')
mygraphObject.add_Edge('C','E')
mygraphObject.add_Edge('E','A')
print(mygraphObject.print_adjList())
print(mygraphObject.getNodeDegree('E'))
