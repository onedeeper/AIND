explored = []
print(dir(problem))
print(problem.walls)
while(True):
    #if the frontier is empty, return failiure
    if frontier.isEmpty():
        return ("No solution")

    #choose a leaf node and remove it from the frontier
    current_node = frontier.pop()

    #if node contains a goal state, then return the corresponding solution
    #check if the initial state is a goal state.
    if len(current_node) == 2:

        if problem.isGoalState(current_node):
            explored.append(current_node)
            return_list = [n[1] for n in explored]

            return(return_list)

    #for checking all other states
    if len(current_node) != 2:
        if problem.isGoalState(current_node[0]):
            #print(current_node)
            explored.append(current_node)
            return_list = [n if len(n) == 2 else n[1] for n in explored]
            print(return_list)
            return(return_list[1:])
            #return(True)
    #add the node to the explored set
    explored.append(current_node)
    #expand the chosen node, add the resulting nodes to the frontier
    #the initial state has no path or cost so of different shape
    if len(current_node) == 2:
        #print(len(current_node))
        current_node_successors = problem.getSuccessors(current_node)
        print('c.n successor: ',current_node_successors)
    #for all states past the initial, need the state which is the first
    #in the triple
    if len(current_node) != 2 :
        #print(len(current_node))
        current_node_successors = problem.getSuccessors(current_node[0])
        print('c.n successor: ',current_node_successors)

    for n in current_node_successors:
        frontier_states = [ l[0] for l in frontier.list]
        explored_states = [ s if (len(s) == 2) else s[0] for s in explored]

        if n[0] not in explored_states and n[0] not in frontier_states:
            frontier.push(n)
