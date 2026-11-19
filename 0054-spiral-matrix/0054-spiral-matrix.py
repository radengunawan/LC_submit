class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        steps = [len(matrix[0]), len(matrix) - 1]

        r, c, d = 0, -1, 0
        while steps[d & 1]:
            for i in range(steps[d & 1]):
                r += directions[d][0]
                c += directions[d][1]
                res.append(matrix[r][c])
            steps[d & 1] -= 1
            d += 1
            d %= 4
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna