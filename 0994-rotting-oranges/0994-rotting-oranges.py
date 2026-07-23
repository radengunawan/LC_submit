class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def count_value(val):
            return sum(1 for r in range(ROWS) for c in range (COLS) if grid[r][c] == val)


        fresh = count_value(1)
        time = 0

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             fresh += 1

        

        while fresh > 0:
            flag = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            row, col = r + dr, c + dc
                            if (row in range(ROWS) and
                                col in range(COLS) and
                                grid[row][col] == 1):
                                grid[row][col] = 3
                                fresh -= 1
                                flag = True

            if not flag:
                return -1

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1

        return time



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna