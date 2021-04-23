""" Created by debjitpal5040

    Dijsktra's Shortest Path Algorithm

    Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph.
    For a given source node in the graph, the algorithm finds the shortest path between that node and every other.

    The alogorithm can be informally described as performing the following steps:

    Let the node at which we are starting be called the initial node. 
    Let the distance of node Y be the distance from the initial node to Y. 
    Dijkstra's algorithm will assign some initial distance values and will try to improve them step by step.

        1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
        2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. 
           Set the initial node as current.
        3. For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the current node. 
           Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
           Otherwise, the current value will be kept.
        4. When we are done considering all of the unvisited neighbours of the current node, 
           mark the current node as visited and remove it from the unvisited set. 
           A visited node will never be checked again.
        5. If the destination node has been marked visited (when planning a route between two specific nodes)
           or if the smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal;
           occurs when there is no connection between the initial node and remaining unvisited nodes), 
           then stop. The algorithm has finished.
        6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, 
           set it as the new "current node", and go back to step 3
"""
Infinity=100000
Max=100
def dijkstra(G,n,startnode):
    cost=[[0 for x in range(Max)] for y in range(Max)]
    distance=[0 for x in range(Max)]
    pred=[0 for x in range(Max)]
    visited=[0 for x in range(Max)]
    for i in range(n):
        for j in range(n):
            if G[i][j]==0:
                cost[i][j]=Infinity
            else:
                cost[i][j]=G[i][j]
    for i in range(n):
        distance[i]=cost[startnode][i]
        pred[i]=startnode
        visited[i]=0
    distance[startnode]=0
    visited[startnode]=1
    count=1
    while count<n-1:
        mindistance=Infinity
        for i in range(n):
            if distance[i]<mindistance and not visited[i]:
                mindistance=distance[i]
                nextnode=i
        visited[nextnode]=1
        for i in range(n):
            if not visited[i]:
                if mindistance+cost[nextnode][i]<distance[i]:
                    distance[i]=mindistance+cost[nextnode][i]
                    pred[i]=nextnode
        count+=1
    for i in range(n):
        if i!=startnode:
            print("Shortest distance between node "+ str(i)+ " and starting node = "+ str(distance[i]))
            print("Path = "+str(i),end="")
            j=i
            while True:
                j=pred[j]
                print("->"+str(j),end="")
                if j==startnode:
                    print()
                    break
n=5                
print("Total number of vertices :",n)
G=[ [0,2,3,0,0],
    [2,0,15,2,0],
    [3,15,0,0,13],
    [0,2,0,0,9],
    [0,0,13,9,0] ]
u=2
print("The starting node :",u)
dijkstra(G,n,u)

"""
Output

Total number of vertices : 5
The starting node : 2
Shortest distance between node 0 and starting node = 3
Path = 0->2
Shortest distance between node 1 and starting node = 5
Path = 1->0->2
Shortest distance between node 3 and starting node = 7
Path = 3->1->0->2
Shortest distance between node 4 and starting node = 13
Path = 4->2

"""