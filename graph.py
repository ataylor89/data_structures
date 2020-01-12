from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor, visited, recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                return True

    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V

        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False

g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.isCyclic() == True: 
    print "Graph has a cycle"
else: 
    print "Graph has no cycle"

# Thanks to Divyanshu Mehta for contributing this code 
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
