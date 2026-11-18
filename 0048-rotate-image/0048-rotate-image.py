class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna