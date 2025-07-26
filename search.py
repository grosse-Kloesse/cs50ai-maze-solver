from collections import deque

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
    
    pass
        

def get_neighbors(position, maze, is_wall):
    i, j = position
    neighbors = []

    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]):
            if not is_wall(ni, nj):
                neighbors.append((ni, nj))

    return neighbors