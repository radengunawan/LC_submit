class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # N = len(s)
        highestIndex = {}

        for i, c in enumerate(s):
            highestIndex[c] = i
        
        res = []
        the_size = 0
        the_end = 0

        for i,c in enumerate(s):
            the_size += 1
            the_end = max(the_end, highestIndex[c])

            if the_end == i:
                res.append(the_size)
                the_size = 0
        
        return res





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna