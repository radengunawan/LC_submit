"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {node: Node(node.val)}
        stack = [node]

        while stack:
            current = stack.pop()
            for neigh in current.neighbors:
                if neigh not in oldToNew:
                    oldToNew[neigh] = Node(neigh.val)
                    stack.append(neigh)
                oldToNew[current].neighbors.append(oldToNew[neigh])
        
        return oldToNew[node]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna