import numpy as np
from puzzle_libraries import *
import copy

#------------------------------------------------------------------
# This pyhton script solves the 8 piece puzzle
# It plans the final node from the intial node using BFS(Breadth 
# First Search)
#------------------------------------------------------------------


# Funtion to backtrack the path from the final node
# Input: The visited queue
# Output: The queue with the path
def backtracking (visited):

    path = []
    path.append(visited[-1])
    search_path = visited[::-1]
    current_node = search_path.pop(0)

    while search_path:

        for node in search_path:
            if current_node.parent_node_index == node.node_index:
                path.append(node)
                current_node = search_path.pop(0)
                break
            else:
                search_path.pop(0)
                break

    return path[::-1]
    

# Function for BFS
# Input: Initial and Final node state
# Output: visited node list if exists else -1
def breadth_first_search (inital_node_state, goal_node_state):
    
    # Maintaining a global current node index
    node_index = 0
    
    # Creating the queues
    queue = []
    visited = []
    
    # Goal flag is raised when we found the goal
    goal_reached_flag = False
    
    # Creating a node
    inital_node = Node()
    
    # Update the node
    inital_node.node_state = np.copy(inital_node_state)
    inital_node.update_node(node_index)
    node_index += 1
    inital_node.node_index = node_index
    
    # Appending the first node to the queue
    queue.append(inital_node)
    
    # Changing the current node
    curr_node = Node()
    curr_node = copy.deepcopy(inital_node)
    
    # Creating a temp node
    temp_node = Node()

    # Setting a threshold to stopping infinite loops
    thresh = 0
    
    while not goal_reached_flag:
        
        # Quit if there are no child nodes
        if curr_node.child_nodes == 0:
                print('Nowhere to go!!!')
                goal_reached_flag = True
                break
        
        # For every possible action create a new node and update the queue
        for i in range(len(curr_node.possible_actions)):
            
            temp_node = copy.deepcopy(curr_node)
            
            # Creating the child nodes
            if (curr_node.possible_actions[i]):
                if (i == 0):
                    temp_node.move_up(curr_node.zero_location)
                elif (i == 1):
                    temp_node.move_right(curr_node.zero_location)
                elif (i == 2):
                    temp_node.move_down(curr_node.zero_location)
                elif (i == 3):
                    temp_node.move_left(curr_node.zero_location)
                    
                # Counting child elements and possible actions for this new node
                temp_node.update_node(curr_node.node_index)
                node_index += 1
                temp_node.node_index = node_index
            
                # Adding to the existing queue
                queue.append(temp_node)
            
            if (compare_nodes(temp_node.node_state, goal_node_state)):
                print("\nFound the goal")
                print("==============\n")
                queue[-1].node_index = visited[-1].node_index + 2
                goal_reached_flag = True
                break
            
        visited.append(queue.pop(0))
        if goal_reached_flag:
            visited.append(temp_node)
        curr_node = copy.deepcopy(queue[0])
        curr_node.action_checker()
        
        # Setting an impossible threshold
        thresh += 1
        if thresh > 50000:
            return -1
    return visited


# The main function for the 8 piece puzzle
if __name__ == '__main__':
    
    # Defining the inital node
    inital_node_state = np.array([[1, 4, 7], [5, 8, 0], [2, 3, 6]])
    
    # Defining the goal node
    goal_node_state = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 0]])
    
    # Calling the BFS algorithm for finding the path
    visited = breadth_first_search(inital_node_state, goal_node_state)
    
    if visited == -1:
        print("Impossible to solve")
        print("-------------------")
        print("Files not generated")
    else:
        # Using the visited node list to find the path
        BFS_path = backtracking(visited)
        
        '''
        print("The Art:")
        for every_node in visited:
            print(f'Node index is {every_node.node_index} parent is {every_node.parent_node_index} state is:\n{every_node.node_state}')
        '''
        
        print("The path found to the goal:")
        for every_node in BFS_path:
            print(f'Node index is {every_node.node_index} parent is {every_node.parent_node_index} state is:\n{every_node.node_state}\n')
        
        # Writing the text files
        with open('nodePath.txt', 'w') as txt_file:
            for node in BFS_path:
                to_write = str(np.reshape(node.node_state, (1, 9), order='F')).replace('[', '').replace(']', '').replace(',', '')
                txt_file.write(to_write + '\n')

        with open('Nodes.txt', 'w') as txt_file:
            for node in visited:
                to_write = str(np.reshape(node.node_state, (1, 9), order='F')).replace('[', '').replace(']', '').replace(',', '')
                txt_file.write(to_write + '\n')
        
        with open('NodesInfo.txt', 'w') as txt_file:
            txt_file.write("Node_index   Parent_Node_index   Cost\n")
            for node in visited:
                to_write = str(node.node_index) + ' ' + str(node.parent_node_index) + " 0"
                txt_file.write(to_write + '\n')
        print('Files generated..... :D\n')