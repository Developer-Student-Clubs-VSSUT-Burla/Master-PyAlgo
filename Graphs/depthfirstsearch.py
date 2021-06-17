class Stack():
    def __init__(self):
        self.size=0
        self.list=[]
    def push(self,a):
        self.list.append(a)
        self.size+=1
    def pop(self):
        try:
            self.size-=1
            return self.list.pop()
        except Exception as error:
            print("{error} is not possible")
    def xprint(self, index):
        print(self.list[index])        


def DFS(graph,root):
    stack = Stack()
    visited_nodes = []
    DFStraversal=[]
    stack.push(root)
   
    curent_node=root

    while stack.size > 0:
        current_node = stack.pop()
       
        if current_node not in visited_nodes:
             DFStraversal.append(current_node)
        
        if current_node in visited_nodes:
            continue
        visited_nodes.append(current_node)    

        adj_nodes = graph[current_node]
        
        for a in adj_nodes:
            if a not in visited_nodes:
                stack.push(a)
                

    return DFStraversal       

if __name__ == "__main__":

    graph = dict()

    graph["A"] = ["B", "G", "D"]
    graph["B"] = ["A", "F", "E"]
    graph["C"] = ["F", "H"]
    graph["D"] = ["F", "A"]
    graph["E"] = ["B", "G"]
    graph["F"] = ["B", "D", "C"]
    graph["G"] = ["A", "E"]
    graph["H"] = ["C"]

    print(DFS(graph, "A"))
         

#OUTPUT
#['A','D','F','C','H','B','E','G']