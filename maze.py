from search import bfs,dfs,astar

class Maze:
    def __init__(self,filename):
        with open(filename) as f:
            contents = f.read()
    
        lines = [line.rstrip("\r\n") for line in contents.splitlines()]

        self.height = len(lines)
        self.width = max(len(line) for line in lines)
        self.maze = []

        self.start = None
        self.goal = None

        for i, line in enumerate(lines):
            row = []
            for j in range(self.width):
                if j>=len(line):
                    char=" "
                else:
                    char = line[j]

                if char == "A":
                    self.start = (i,j)
                    row.append(" ")
                elif char == "B":
                    self.goal = (i,j)
                    row.append(" ")
                else:
                    row.append(char)
            self.maze.append(row)

    def print_maze(self):
        for i in range(self.height):
            for j in range(self.width):

                if (i,j) == self.start:
                    print("A", end = "")
                elif (i,j) == self.goal:
                    print("B" , end = "")
                elif hasattr(self, 'solution') and (i,j) in self.solution:
                    print ("*",end="") # use * to show path
                else:
                    print(self.maze[i][j],end="")

            print()
        print (len(self.solution))

    def solve(self, method="bfs"):
        
        def is_wall(i,j):
            return self.maze[i][j] == "#"
        
        if method == "bfs":
            path = bfs(self.maze,self.start,self.goal,is_wall)
        elif method =="dfs":
            path = dfs(self.maze,self.start,self.goal,is_wall)
        elif method == "astar":
            path = astar(self.maze,self.start,self.goal,is_wall)
        else:
            raise ValueError("Unknown search method")
        
        if path is None:
            print("No Path found!")
        else:
            self.solution = set(path)

if __name__ == "__main__":
    m = Maze("maze.txt")
    m.solve("astar")
    m.print_maze()