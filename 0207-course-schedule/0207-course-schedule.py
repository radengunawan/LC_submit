class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        howManyNeedMe = [0]*numCourses

        courseMap = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
            howManyNeedMe[prereq]+=1
        
        q = deque()

        for i in range(len(howManyNeedMe)):
            if howManyNeedMe[i] == 0:
                q.append(i)
        
        finished_courses = 0
        while q:
            current_course = q.popleft()
            finished_courses +=1

            for prereq in courseMap[current_course]:
                howManyNeedMe[prereq] -=1
                if howManyNeedMe[prereq] == 0:
                    q.append(prereq)
        
        return finished_courses == numCourses
        

        

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna