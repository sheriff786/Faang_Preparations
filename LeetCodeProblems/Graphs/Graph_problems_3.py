'''
course schedule -1

'''

from collections import deque

class Solution:

    def canFinish(self, numCourses, prerequisites):

        # Build graph
        adj = [[] for _ in range(numCourses)]

        indegree = [0] * numCourses

        for course, prereq in prerequisites:

            adj[prereq].append(course)

            indegree[course] += 1

        queue = deque()

        # Push indegree 0 courses
        for i in range(numCourses):

            if indegree[i] == 0:
                queue.append(i)

        processed = 0

        while queue:

            node = queue.popleft()

            processed += 1

            for neighbour in adj[node]:

                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return processed == numCourses
    
numCourses = 4

prerequisites = [
    [1,0],
    [2,0],
    [3,1],
    [3,2]
]

'''
course-schedule 2  just need to return the topological order for that we can use same bfs kahn topological order algorithm

'''


from collections import deque

class Solution:

    def findOrder(self, numCourses, prerequisites):

        # Build graph
        adj = [[] for _ in range(numCourses)]

        indegree = [0] * numCourses

        for course, prereq in prerequisites:

            adj[prereq].append(course)

            indegree[course] += 1

        queue = deque()

        # Add all courses with indegree 0
        for i in range(numCourses):

            if indegree[i] == 0:
                queue.append(i)

        order = []

        while queue:

            node = queue.popleft()

            order.append(node)

            for neighbour in adj[node]:

                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(order) == numCourses:
            return order

        return []
numCourses = 4

prerequisites = [
    [1,0],
    [2,0],
    [3,1],
    [3,2]
]

'''

Course Schedule I	Course Schedule II

Return True/False	    Return course order
Count processed nodes	Store processed nodes
processed == numCourses	 len(order) == numCourses
Detect cycle	         Produce  topological order 
diffrenece in them 

-----------------------------------

Course Schedule I

processed += 1

return processed == numCourses
------------------------------------------
Course Schedule II

order.append(node)

if len(order) == numCourses:
    return order

return []

Everything else is identical.
'''

#Alien dictionary

'''
Problem Statement

Suppose an alien language uses English letters but in a different alphabetical order.

You are given a list of words already sorted according to the alien language.

Find one possible order of the characters.

Example
words =

wrt
wrf
er
ett
rftt

Output

wertf


This problem has two phases:

Input Words
        ↓
Build Graph
        ↓
Topological Sort
        ↓
Answer

Many candidates know Topological Sort but struggle because they don't realize the first challenge is constructing the graph correctly.
'''


from collections import deque

class Solution:

    def alienOrder(self, words):

        # Step 1: Create graph with every character
        graph = {char: set() for word in words for char in word}

        indegree = {char: 0 for char in graph}

        # Step 2: Build graph
        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]

            # Invalid case
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            for c1, c2 in zip(word1, word2):

                if c1 != c2:

                    if c2 not in graph[c1]:

                        graph[c1].add(c2)
                        indegree[c2] += 1

                    break

        # Step 3: Push indegree 0 characters
        queue = deque()

        for char in indegree:

            if indegree[char] == 0:
                queue.append(char)

        order = []

        # Step 4: Topological Sort
        while queue:

            char = queue.popleft()

            order.append(char)

            for neighbour in graph[char]:

                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        # Step 5: Check cycle
        if len(order) == len(graph):
            return "".join(order)

        return ""


