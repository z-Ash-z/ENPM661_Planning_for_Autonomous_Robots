Run the puzzle_8_project_V2.py to get the text files

- change the initial and goal nodes (in line number 129 and 132 of the code) for generating a different node path

- Libraries used:
	- copy: to make deepcopy of the matrices
	- numpy: for numpy operations

- Prints the node path if found and generates nodePath.txt, Nodes.txt and NodesInfo.txt
	- nodePath.txt - contains the state of each node from initial to the goal. The 3x3 matrix is converted to a 1x9 row vector read column-wise
	- Nodes.txt - contains the list of all the visited nodes. The 3x3 matrix is converted to a 1x9 row vector read column-wise
	- NodesInfo.txt - Contains the node index and it's parent's node index along with the cost to come

After running puzzle_8_project_V2.py, run plot_path.py

- It reads the generated nodePath.txt file and gives a graphical view of the nodes generated