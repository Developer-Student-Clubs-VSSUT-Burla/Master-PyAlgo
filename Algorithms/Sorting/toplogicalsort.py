'''
TOPOLOGICAL SORT

You're given a list of arbitrary jobs that need to be completed. These jobs are in form of distinct integer numbers. You're also given a list of dependencies.A dependency is represented as a pair of job where the first job is a prerequisite of second job i.e. the second job is dependent on first one, it can only be completed once the first job is completed .

Write a function that takes a list of jobs and list of dependencies and return a list containing a valid order in which jobs are completed if no such order exists then function should return an empty array.

Jobs : [1,2,3,4]
deps : [ [1,2] , [1,3] , [3,2] , [4,2] , [4,3] ]
Output [1,4,3,2] or [4,1,3,2]

Space and Time Complexity:
O(j+d)time and O(j+d)space - where j is the numbers of jobs and d is the number of dependencies.


'''
class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False

class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addPrereq(self, job, prereq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(prereq)
        jobNode.prereqs.append(prereqNode)

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

#   O(v + e) time | O(v + e) space
def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)

def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.addPrereq(job, prereq)
    return graph

def getOrderedJobs(graph):
    orderedJobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        containsCycle = depthFirstTraverse(node, orderedJobs)
        if containsCycle:
            return []
    return orderedJobs

def depthFirstTraverse(node, orderedJobs):
    if node.visited:
        return False
    if node.visiting:
        return True
    node.visiting = True
    for prereqNode in node.prereqs:
        containsCycle = depthFirstTraverse(prereqNode, orderedJobs)
        if containsCycle:
            return True
    node.visited = True
    node.visiting = False
    orderedJobs.append(node.job)
    return False

def main():
    print(topologicalSort([1,2,3,4],[[1,2],[1,3],[3,2],[4,2],[4,3]]))
main()
