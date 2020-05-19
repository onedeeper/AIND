def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Agent
    import itertools
    print ("Start:", problem.getStartState())
    print ("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print ("Start's successors:", problem.getSuccessors(problem.getStartState()))

    #A function to unpack a list of lists to get the final directions
    def walk(e):
        if type(e) == list:
            for v2 in e:
                for v3 in walk(v2):
                    yield v3
        else:
            yield e

    class Node:
        def __init__(self, state ,action = None, path_cost = None, parent = None, current_path = None):
            self.state = state
            self.action = action
            self.parent = parent

        def __repr__(self):
            return ("parent: {},action: {}, state: {} ".format(self.parent,self.action, self.state))


    frontier = util.Stack() #initialize frontier as a LIFO queue
    #initialize the frontier witht he start state
    start_state = problem.getStartState()
    #explored set to store the expanded states
    explored = set()
    frontier.push(Node(start_state))

    while(frontier.isEmpty() == False):
        #if frontier is empty: return fail
        #remove choice from frontier
        current_node = frontier.pop()

        if isinstance(current_node,list):
            state = current_node[-1].state
            explored.add(state)
            possible_next_nodes = [Node(*i, state)for i in problem.getSuccessors(current_node[-1].state)]

        else:
            state = current_node.state
            explored.add(state)
            possible_next_nodes = [Node(*i, current_node.state)for i in problem.getSuccessors(current_node.state)]

        if problem.isGoalState(state):
            solved_path = []
            for link_node in walk(current_node):
                solved_path.append(link_node.action)
            return(solved_path[1:])

        #go through each possible next states and decide what goes on the frontier.
        for next_node in possible_next_nodes:
            #unless results(s,a) is in frontier or explored
            #add [path + results(s,a)] to frontier
            if next_node.state not in explored and next_node not in frontier.list:
                frontier.push([current_node, next_node])
