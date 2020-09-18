 

Welcome To Maze_Solver_project by Ayush
Introduction :
Maze Solver is a program that takes N*N as input matrix and gives the valid path.
First step after opening Python Project.
The Github python project consists of 3 contents.
* README.md
* Maze_solver_project.py
* Maze_solver_project.exe


 My Approach
I have implemented the DFS(Depth First Search) algorithm by taking the oops concept and using backtracking recursive. As there are two approaches to solve this problem using dfs, one if using stack operation(iterative approach) and the other is the recursive approach using the backtracking. This approach goes deep in the cell and tries to fetch the valid path by keeping a note on the visited path, so that it won't trace the same path again.
Code Explanation
The driver function calls the argparse command line through which the input is taken by the user python Maze_solver_project.py -i input.txt -o output.txt.
We take the solution matrix as an input maze and assign it to 0.
Using Maze_solver_dfs function call, retrieve the valid path and return the answer to the solution matrix.
Lastly append all the solveMaze elements in string format.
Technologies Used
Argparse
Pyinstaller
datetime
Conclusion

My final words on this project is I would like to thank our instructor Shubham Sir and Arkesh Sir for guiding us.
References
https://www.geeksforgeeks.com
https://www.tutorialspoints.com/backtracking

