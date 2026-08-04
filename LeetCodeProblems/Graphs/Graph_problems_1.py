''' Count Number of connected components 
You are given an undirected graph with n vertices numbered from 0 to n-1.

Return the number of connected components in the graph.

A connected component is a group of vertices where every vertex is reachable from every other vertex.

Example
n = 7

Edges

0 ----- 1
|       |
2       3


4 ----- 5

6

Adjacency List

adj = [
    [1,2],     # 0
    [0,3],     # 1
    [0],       # 2
    [1],       # 3
    [5],       # 4
    [4],       # 5
    []         # 6
]

Output

3



'''


class Solution:

    def countComponents(self, adj):

        n = len(adj)

        visited = [False] * n
        count = 0

        def dfs(node):

            visited[node] = True

            for neighbour in adj[node]:

                if not visited[neighbour]:
                    dfs(neighbour)

        for i in range(n):

            if not visited[i]:
                count += 1
                dfs(i)

        return count
    
    
''' #2 Number of Provinces (LeetCode 547) 

isConnected = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

obj = Solution()

print(obj.findCircleNum(isConnected))

'''


class Solution:

    def findCircleNum(self, isConnected):

        n = len(isConnected)

        visited = [False] * n
        provinces = 0

        def dfs(city):

            visited[city] = True

            # Scan the entire row
            for neighbour in range(n):

                if isConnected[city][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)

        # Handle disconnected graph
        for city in range(n):

            if not visited[city]:

                provinces += 1
                dfs(city)

        return provinces
    
    
    '''
    Number of Islands

Difficulty: 🟡 Medium

Problem Statement

You are given a 2D grid of '1's (land) and '0's (water).

Count the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically.

Diagonal cells are NOT connected.

Example 1
grid =

1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

Output

1

Because everything is connected.

Example 2
grid =

1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1

Output

3

Visualization

Island 1

1 1
1 1

--------------

Island 2

    1

--------------

Island 3

      1 1
    '''
    class Solution:

    def numIslands(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        islands = 0

        directions = [
            (-1, 0),   # Up
            (1, 0),    # Down
            (0, -1),   # Left
            (0, 1)     # Right
        ]

        def dfs(r, c):

            visited[r][c] = True

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == "1" and
                    not visited[nr][nc]
                ):
                    dfs(nr, nc)

        for r in range(rows):

            for c in range(cols):

                if grid[r][c] == "1" and not visited[r][c]:

                    islands += 1
                    dfs(r, c)

        return islands
    
'''
Flood Fill

Difficulty: 🟢 Easy

Problem Statement

You are given an image represented by a 2D grid.

Each cell contains a color (integer).

You are given:

sr = starting row
sc = starting column
color = new color

Replace the color of the starting pixel and every connected pixel with the same original color using the new color.

Connectivity is only:

Up
Down
Left
Right
Example

Input

image =

1 1 1
1 1 0
1 0 1

sr = 1
sc = 1

newColor = 2

Starting position

1 1 1
1 X 0
1 0 1

Output

2 2 2
2 2 0
2 0 1

Notice the bottom-right 1 is not connected, so it is not changed.

Visualization

Original

1 1 1
1 1 0
1 0 1

Flood Fill starts here

1 1 1
1 X 0
1 0 1

It spreads like water.

2 2 2
2 2 0
2 0 1

'''

class Solution:

    def floodFill(self, image, sr, sc, color):

        rows = len(image)
        cols = len(image[0])

        oldColor = image[sr][sc]

        if oldColor == color:
            return image

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        def dfs(r, c):

            image[r][c] = color

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and image[nr][nc] == oldColor
                ):
                    dfs(nr, nc)

        dfs(sr, sc)

        return image
'''
 
Connected Components
    ↓
Count

Number of Islands
    ↓
Count

Max Area
    ↓
Return Area

Flood Fill
    ↓
Modify Grid

    '''  
    
'''Rotton Orange 


BFS approach is the only solutions
'''

def rottanOrange(grid):
    
    rows=len(grid)
    cols=len(grid[0])
    queue=deque()
    
    directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
    
    for r in range(rows):
        for c in range(cols):
            
            if grid[r][c]==2:
                q.append((r,c))
            elif grid[r][c]==1:
                fresh+=1
    if fresh==0:
        return 0
    minutes = 0
    while queue and fresh > 0:

            size = len(queue)

            for _ in range(size):

                r, c = queue.popleft()

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):

                        grid[nr][nc] = 2
                        fresh -= 1

                        queue.append((nr,nc))

            minutes += 1

        if fresh == 0:
            return minutes

        return -1
    
'''
DFS Problems

Connected Components

↓

Number of Islands

↓

Max Area

↓

Flood Fill


BFS Problems

BFS Traversal

↓

Rotting Oranges ⭐

↓

01 Matrix

↓

Walls and Gates

↓

Shortest Path in Binary Matrix


⭐ Multi-Source BFS Pattern

Whenever you hear:

Spread
Infection
Fire
Virus
Distance from nearest source
Multiple starting points

Immediately think:

Queue = all sources

while queue:

    process one level

    minutes += 1

This is one of the most valuable BFS patterns for interviews.



'''
