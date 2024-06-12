# Course Schedule

# numCourses = 0, 1, 2, 3
# prerequs = [[1, 0]]
# could use an adjecency matrix, and also use caching or a dynamic programming approach 
# to store the number of prereqs for

# i thought about this wrong, sort of... basically you are trying to detect cycles
# but you are of course still able to cache and not revisit and redo work you have done when processing nodes.

class Solution(object):
    def courseSchedule(self, numCourses, prereqs):
        graph = {}
        for c, p in prereqs:
            if c not in graph.keys():
                graph[c] = [p]
            else:
                graph[c].append(p)

sol, numCourses, prereqs = Solution(), 4, [[1, 0], [2, 0], [3, 0], [4, 0]]
print(sol.courseSchedule(4, prereqs))