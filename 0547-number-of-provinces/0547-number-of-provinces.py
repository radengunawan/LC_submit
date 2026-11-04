class ParentGroups:
    def __init__ (self,n):
        self.n = n
        self.count = n
        self.parent = list(range(n))
    
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False
        
        self.parent[root_b] = root_a
        self.count -=1
        return True


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        groups = ParentGroups(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    groups.union(i,j)
        
        return groups.count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna