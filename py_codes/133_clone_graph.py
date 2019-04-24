'''
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. 
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Example:

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},
{"$id":"3","neighbors":[{"$ref":"2"},
{"$id":"4","neighbors":[{"$ref":"3"},
{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor
 too.
You must return the copy of the given node as a reference to the cloned graph.
'''

#Definition for a undirected graph node
from collections import deque
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        nodeMap = {}
        visited = []
        if not node:
            return None
        def bfs(startNode):
            queue = deque([startNode])
            while queue:
                curr = queue.popleft()
                if curr.label not in visited:
                    visited.append(curr.label)
                else:
                    continue
                if curr.label not in nodeMap:
                    nodeMap[curr.label] = UndirectedGraphNode(curr.label)
                for neighbor in curr.neighbors:
                    if neighbor.label not in nodeMap:
                        nodeMap[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    if neighbor.label not in visited:
                        queue.append(neighbor)
                    nodeMap[curr.label].neighbors.append(nodeMap[neighbor.label])
        bfs(node)
        return nodeMap[node.label]
    
    def cloneGraph2(self, node):
        nodemap = {}
        
        def dfs(startNode):
            stack = [node]
            while stack:
                currNode = stack.pop()
                if currNode not in nodemap:
                    nodemap[currNode] = UndirectedGraphNode(currNode.label)
                
                for neighbor in currNode.neighbors:
                    if neighbor not in nodemap:
                        nodemap[neighbor] = UndirectedGraphNode(neighbor.label)
                        stack.append(neighbor)
                    nodemap[currNode].neighbors.append(nodemap[neighbor])
        dfs(node)
        return nodemap[node]
            
s = Solution()
node = UndirectedGraphNode(1)
node.neighbors = [UndirectedGraphNode(2)]
print s.cloneGraph2(node).label
for i in s.cloneGraph2(node).neighbors:
    print i.label
