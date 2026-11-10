class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True

        from collections import defaultdict

        required_for = defaultdict(list)
        n_deps = defaultdict(int)
        easy_courses = set(range(0, numCourses))

        for course, dependency in prerequisites:
            required_for[dependency].append(course)
            n_deps[course] += 1
            if course in easy_courses: easy_courses.remove(course)

        hard_courses = set(range(0, numCourses))
        easy_courses = list(easy_courses)

        while easy_courses:
            curr = easy_courses.pop(0)
            hard_courses.remove(curr)
            for hard_course in required_for[curr]:
                n_deps[hard_course] -= 1
                if n_deps[hard_course] == 0:
                    # becomes easy
                    easy_courses.append(hard_course)
            
        return len(hard_courses) == 0

