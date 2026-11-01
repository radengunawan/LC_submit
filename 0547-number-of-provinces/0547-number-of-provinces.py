class NaiveGroups:
    def __init__ (self,n):
        self.n = n
        self.count = n
        self.labels = list(range(n))
    
    def connected(self, a, b):
        return self.labels[a] == self.labels[b]
    
    def union(self, a, b):
        label_a = self.labels[a]
        label_b = self.labels[b]

        if label_a == label_b:
            return False
        
        for i in range(self.n):
            if self.labels[i] == label_b:
                self.labels[i] = label_a
        
        self.count -=1

        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        groups = NaiveGroups(n)
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j] == 1:
                    groups.union(i,j)
        
        return groups.count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna