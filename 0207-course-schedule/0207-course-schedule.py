class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courseMap = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            courseMap[course].append(prereq) 
        
        visiting = set()

        def DFS(course):
            if courseMap[course] == []:
                return True
            if course in visiting:
                return False

            visiting.add(course)

            for prereq in courseMap[course]:
                if not DFS(prereq):
                    return False
            
            courseMap[course] = []
            visiting.remove(course)

            return True



        for course in range (numCourses):
            if not DFS(course):
                return False
        
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna