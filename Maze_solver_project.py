

import argparse  # importing the command line python package
import datetime  #importing the date and time 


class Maze:
    def __init__(self, maze):
        self.maze = maze
# conditional boundation and limits of maze solver problem checker Function

    def maze_runner_dfs(self, row, col):
        # condition checking whether the destination element is 0 or not
        if self.maze[n-1][n-1] == 0:
            return False
        # if the final destination reached then
        if (row == n-1) and (col == n-1):
            solution[row][col] = 1
            return True
        if (row >= 0 and col >= 0 and row < n and col < n and
                solution[row][col] == 0 and self.maze[row][col] == 1):
            solution[row][col] = 1  # visiting the cell
            # maze_solver_dfs() call recursively to find the valid path by going deep(dfs)

            if(self.maze_runner_dfs(row+1, col) or
               self.maze_runner_dfs(row-1, col) or
               self.maze_runner_dfs(row, col+1) or 
               self.maze_runner_dfs(row, col-1)):
                return True
            else:

                solution[row][col] = 0  # backtracking

            return False
        else:

            return False

    #               print_path() display the path in string format    #
    # *************************************************************************#

    def print_path(self, sol):
        file2.write("***\n\n" + "the  path followed is " +
                    self.direction(sol) + "reach to the destination: \n\n")
        for i in sol:
            for j in i:
                file2.write(" " + str(j) + " ")
            file2.write('\n')
            # print the output path in matrix form
        time = datetime.datetime.now()
    # call the date time inbuild function that generate the local date time

        file2.write("***\n" + "Time of execution at : " +
                    time.strftime("%d-%m-%Y * %H:%M:%S\n" + "***\n\n"))
        # printing the the path by notaion up down left right notaion


    #direction() function checks the visited path and stores the direction
    # ***********************************************************************#

    def direction(self, solvedMaze):  # call of direction printing function
        n = len(solvedMaze)    # finding the  lenghth of the solved maze
        # make a variable to store in a array cell intial as false
        visited = [[False for _ in range(n)] for _ in range(n)]
        # take blank string variable that store the the direction of movement
        arr = ""
        i = j = 0
        while i != n-1 or j != n-1:
            if j == n-1:
                if solvedMaze[i+1][j] == 1 and visited[i+1][j] is False:
                    visited[i+1][j] = True
                    i = i+1
                    arr += "D=>"
                elif solvedMaze[i][j-1] == 1 and visited[i][j-1] is False:
                    visited[i][j-1] = True
                    j = j-1
                    arr += "L=>"
            elif i == n-1:
                if solvedMaze[i][j+1] == 1 and visited[i][j+1] is False:
                    visited[i][j+1] = True
                    j = j+1
                    arr += "R=>"
                elif solvedMaze[i-1][j] == 1 and visited[i-1][j] is False:
                    visited[i-1][j] = True
                    i = i-1
                    arr += "U=>"
            else:
                if solvedMaze[i+1][j] == 1 and visited[i+1][j] is False:
                    visited[i+1][j] = True
                    i = i+1
                    arr += "D=>"
                elif solvedMaze[i][j+1] == 1 and visited[i][j+1] is False:
                    visited[i][j+1] = True
                    j = j+1
                    arr += "R=>"
                elif solvedMaze[i-1][j] == 1 and visited[i-1][j] is False:
                    visited[i-1][j] = True
                    i = i-1
                    arr += "U=>"
                elif solvedMaze[i][j-1] == 1 and visited[i][j-1] is False:
                    visited[i][j-1] = True
                    j = j-1
                    arr += "L=>"
        return arr


#******Driver Function******   


if __name__ == "__main__":
    maze = []   # appending all cell elemt from the comand line input by user
    maze1 = Maze(maze)     #creating the instance of the class Maze
# TAKING FILE ARGUMENTS FROM COMMAND LINE.  (STEP-1)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input File")
    parser.add_argument("-o", help="Output File")
    args = parser.parse_args()
    file1 = open(args.i, 'r')  # input file
    file2 = open(args.o, 'a')  # output file

    # GENERATING MAZE FROM INPUTS (STEP-2)
    for data in file1:
        [test.strip('\n\r') for test in data]
        maze.append([int(x) for x in data.split()])
    n = len(maze)
    # making a solution matrix and set all cell elemnt to zero initial
    solution = [[0]*n for _ in range(n)]

    # MAZE-RUNNER
    if(maze1.maze_runner_dfs(0, 0)):  # (STEP-3)
        maze1.print_path(solution)
    else:
        file2.write("***\n-1\n")
        file2.write(
            " sorry there is no any path available to reach destination.")
        now = datetime.datetime.now()
        file2.write("\nTime of execution at : " +
                    now.strftime("%d-%m-%Y * %H:%M:%S") + "\n***\n\n\n")

