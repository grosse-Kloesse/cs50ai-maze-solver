from collections import deque
import heapq

def bfs(maze, start, goal, is_wall):
    """
    Breadth_First Search to find the shortest path in the maze.

    Parameters:
        maze: 2D list of characters
        start: (row, col) tuple
        goal: (row, col) tuple
        is_wall: function(i, j) -> bool

    Returns:
        path: list of (row, col) tuples from start to goal
            or None if no path found    
    """

    frontier = deque()
    frontier.append(start)

    came_from = {start:None}
    visited = set()

    while frontier:
        current = frontier.popleft()

        if current == goal:
            # return patn
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        visited.add(current)

        for neighbor in get_neighbors(current, maze, is_wall):
            if neighbor not in visited and neighbor not in frontier:
                came_from[neighbor] = current
                frontier.append(neighbor)

    return None  # no path

def dfs(maze, start, goal, is_wall):
    
    frontier = [start]

    came_from = {start:None}
    visited = set()

    while frontier:
        current = frontier.pop()

        if current == goal:
            # return patn
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        visited.add(current)

        for neighbor in get_neighbors(current, maze, is_wall):
            if neighbor not in visited and neighbor not in frontier:
                came_from[neighbor] = current
                frontier.append(neighbor)

    return None  # no path
        

def astar(maze,start,goal,is_wall):
    def heuristic (a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
    
    frontier = []
    heapq.heappush(frontier,(0,start))

    came_from={start:None}
    cost_so_far = {start:0}


    while frontier:
        _,current = heapq.heappop(frontier)

        if current == goal:
            return reconstruct_path(came_from,goal)
        
        for neighbor in get_neighbors(current,maze,is_wall):
            new_cost = cost_so_far[current] +1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                property = new_cost + heuristic(neighbor,goal)
                heapq.heappush(frontier,(property,neighbor))
                came_from[neighbor] = current
    return None

def get_neighbors(position, maze, is_wall):
    i, j = position
    neighbors = []

    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]):
            if not is_wall(ni, nj):
                neighbors.append((ni, nj))

    return neighbors

def reconstruct_path(came_from,goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path