# Python program to print topological sorting of a DAG 
from collections import defaultdict 

# Class to represent a graph 


class Graph: 
	def __init__(self, vertices): 
		self.graph = defaultdict(list) # dictionary containing adjacency List 
		self.V = vertices # No. of vertices 

	# function to add an edge to graph 
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	# A recursive function used by topologicalSort 
	def topologicalSortUtil(self, v, visited, stack): 
		print(stack)
		print(visited)
		# Mark the current node as visited. 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.topologicalSortUtil(i, visited, stack) 

		# Push current vertex to stack which stores result 
		stack.append(v) 

	# The function to do Topological Sort. It uses recursive 
	# topologicalSortUtil() 
	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack = [] 

		# Call the recursive helper function to store Topological 
		# Sort starting from all vertices one by one 
		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i, visited, stack) 

		# Print contents of the stack 
		for i in range(9,-1,-1):print(stack[i],end="") # return list in reverse order 
f=open("/home/vedant/program files/Project-Euler/79/text.txt", "r")
g = Graph(10) 
for i in range(50):
    inp=f.readline()
    g.addEdge(int(inp[0]),int(inp[1]))
    g.addEdge(int(inp[1]),int(inp[2]))
# Driver Code 



print ("Following is a Topological Sort of the given graph")

# Function Call 
g.topologicalSort() 

# This code is contributed by Neelam Yadav
