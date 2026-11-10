class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # DFS
        # preMap = {course: [] for course in range(numCourses)}
        # for course, pre in prerequisites:
        #     preMap[course].append(pre)

        # seen = set()
        # def dfs(course):
        #     if course in seen:
        #         return False
        #     seen.add(course)

        #     for pre in preMap[course]:
        #         if not dfs(pre): return False
            
        #     # Lets save some computation for the others 
        #     preMap[course] = []  # already we know this part doesnt have loops

        #     # allow this node to be seen by someone else without penalty of deth
        #     seen.remove(course)
            
        #     return True

        # for course in range(numCourses):
        #     if not dfs(course): return False
        # return True




        # BFS / Top Sort solution
        if not prerequisites: return True

        required_for = defaultdict(list)
        n_deps = [0] * numCourses

        for course, dependency in prerequisites:
            required_for[dependency].append(course)
            n_deps[course] += 1

        easy_courses = deque(i for i in range(numCourses) if n_deps[i] == 0)

        completed = 0
        while easy_courses:
            curr = easy_courses.popleft()
            completed += 1

            for hard_course in required_for[curr]:
                n_deps[hard_course] -= 1
                if n_deps[hard_course] == 0:
                    easy_courses.append(hard_course)

        return completed == numCourses

