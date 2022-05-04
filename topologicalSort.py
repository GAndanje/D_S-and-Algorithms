def topSort(jobs,dependencies):
    JobGraph = createJobGraph(jobs,dependencies)
    return OrderedListfunction(JobGraph)

def createJobGraph(jobs,dependencies):
    graph= JobGraph(jobs)
    for job,prereq in dependencies:
        JobGraph.addPrereq(job,prereq)

class JobGraph:
    def __init__(self,jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addPrereq(self,job,prereq):
        jobNode = JobGraph.getNode(job)
        prereqNode = JobGraph.getNode(prereq)
        jobNode.prereq.append(prereqNode)

    def addNode(self,job):
        self.graph[job]=jobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self,job):
        return self.graph[job]

class jobNode:
    def __init__(self,job):
        self.job = job
        self.prereq = []
        self.visited = False
        self.visiting = False

def OrderedListfunction(JobGraph):
    OrderedList=[]
    nodes = JobGraph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle=depthFirstSearch(node,OrderedList)
        if containsCycle:
            return []
    return OrderedList

def depthFirstSearch(node,OrderedList):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereqNode in node.prereq:
        containsCycle=depthFirstSearch(prereq,OrderedList)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    return False

