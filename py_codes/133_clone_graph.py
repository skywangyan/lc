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
s = Solution()
node = UndirectedGraphNode(1)
node.neighbors = [UndirectedGraphNode(2)]
print s.cloneGraph(node).label
for i in s.cloneGraph(node).neighbors:
    print i.label
