class ParentGroups:
    def __init__ (self, n):
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



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0
        
        R, C = len(grid), len(grid[0])
        groups = ParentGroups(R*C)
        islands = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    islands +=1
                    for dr, dc in [(1,0), (0,1)]:
                        nr, nc = r+dr, c+dc
                        if nr < R and nc < C and grid[nr][nc] == "1":
                            if groups.union( r*C + c, nr*C + nc):
                                islands -=1
        
        return islands

    
        
        return groups.count - num_water_cell


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna