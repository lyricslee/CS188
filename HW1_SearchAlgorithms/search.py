# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def sorted_successor(successores, reverse=False):
    nexts = []
    for next_state, next_direction, next_cost in successores:
        nexts.append({
            "state": next_state,
            "direction": next_direction,
            "cost": next_cost,
        })
    nexts = sorted(nexts, key=lambda next: next["cost"], reverse=reverse)
    return nexts

def dfs_imp(problem, container=util.Stack):
    start_actions = []
    start_state = problem.getStartState()
    if problem.isGoalState(start_state): # start is goal
        return start_actions

    visited = []
    nexted = container()
    nexted.push((start_state, start_actions)) # push start state

    while not nexted.isEmpty():
        state, actions = nexted.pop()
        #print('pop state: ', state)

        if state in visited: # not repeat same state
            continue
        else:
            visited.append(state)

        if problem.isGoalState(state): # find goal state
            return actions

        successores = problem.getSuccessors(state)
        successores = sorted_successor(successores) # sort by cost, choose direction with maximum cost

        for succ in successores:
            next_state = succ["state"]
            next_direction = succ["direction"]
            if next_state in visited:
                continue

            #print('push next_state: ', next_state, next_direction)  # push next state
            nexted.push((next_state, actions + [next_direction]))
    util.raiseNotDefined()

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
    #print('======= depthFirstSearch =======')
    return dfs_imp(problem)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #print('======= breadthFirstSearch =======')
    return dfs_imp(problem, container=util.Queue)

def uniform_cost_serach_imp(problem, container=util.PriorityQueue, heuristic=None):
    start_actions = []
    start_state = problem.getStartState()
    start_cost= 0
    if problem.isGoalState(start_state): # start is goal
        return start_actions

    visited = []
    nexted = container()
    # we use PriorityQueue in uniform_cost_search, cost == priority
    # Here, PriorityQueue is based minimum heap.
    nexted.push((start_state, start_actions, start_cost), start_cost) # push start state

    while not nexted.isEmpty():
        state, actions, cost = nexted.pop()
        #print('pop state: ', state, cost)

        if state in visited: # not repeat same state
            continue
        else:
            visited.append(state)

        if problem.isGoalState(state): # find goal state
            return actions

        successores = problem.getSuccessors(state)
        for next_state, next_direction, next_cost in successores:
            accumulate_cost = float(cost) + float(next_cost)
            if next_state in visited:
                continue

            priority_vaule = accumulate_cost # uniform cost search
            if heuristic: # A start algorithm
                priority_vaule += heuristic(next_state, problem)

            nexted.push((next_state, actions + [next_direction], accumulate_cost), priority_vaule)
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return uniform_cost_serach_imp(problem)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #print('heuristic: ', heuristic)
    return uniform_cost_serach_imp(problem, heuristic=heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
