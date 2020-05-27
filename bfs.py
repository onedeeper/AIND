def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    import copy

    class Node:
        def __init__(self, state ,action = None, path_cost = None, parent = None, path = None):
            self.state = state
            self.action = action
            self.parent = parent
            if path == None:
                self.path = []
            else:
                self.path = path

        def __repr__(self):
            return ("parent: {},action: {}, state: {}, path : {} ".format(self.parent,self.action, self.state, self.path))


    frontier = util.Queue() #initialize frontier as a FIFO queue
    #initialize the frontier witht he start state
    start_state = problem.getStartState()
    #explored set to store the expanded states
    explored = set()
    frontier.push(Node(start_state))

    while(frontier.isEmpty() == False):
        #while there is something left in the frontier, otherwise it means there is no solution to be found.
        #remove choice from frontier
        current_node = frontier.pop()

        #if the current state is not explored, add to the set.
        state = current_node.state
        if state not in explored:
            explored.add(state)

        #if a goal state is found, return the path
        if problem.isGoalState(state):
            return(current_node.path)

        #make nodes for the next sucessors
        possible_next_nodes = [Node(*i, parent = state)for i in problem.getSuccessors(state)]

        #go through each possible next states and decide what goes on the frontier.
        #unless results(s,a) is in frontier or explored
        #add [path + results(s,a)] to frontier
        for next_node in possible_next_nodes:

            #make a list of all the states in the frontier
            frontier_states = [front.state for front in frontier.list]
            if next_node.state not in explored and next_node.state not in frontier_states:
                #make a copy of the path traversed thus far in the current node
                current_path = copy.copy(current_node.path)
                #update the current path with the next action
                current_path.append(next_node.action)
                #create the next node
                a_node = Node(state = next_node.state,action = next_node.action, parent = current_node.state, path = current_path)
                #append the new node to the frontier
                frontier.push(a_node)
