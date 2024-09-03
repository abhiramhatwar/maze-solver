def is_valid_move(maze, visited, x, y):
    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if maze[x][y] == 1 or visited[x][y]:
        return False
    return True

def dfs(maze, x, y, visited, path):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        path.append((x, y))
        return True

    if is_valid_move(maze, visited, x, y):
        visited[x][y] = True
        path.append((x, y))

        if dfs(maze, x + 1, y, visited, path):
            return True
        if dfs(maze, x, y + 1, visited, path):
            return True
        if dfs(maze, x - 1, y, visited, path):
            return True
        if dfs(maze, x, y - 1, visited, path):
            return True

        path.pop()
        visited[x][y] = False

    return False

def solve_maze(maze):
    start_x, start_y = 0, 0
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = []

    if dfs(maze, start_x, start_y, visited, path):
        return path
    else:
        return "No path found"

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

solution_path = solve_maze(maze)
print("Path to solve the maze:", solution_path)
