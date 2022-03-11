# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import heappush, heappop
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
      """
      Returns the start state for the search problem
      """
      util.raiseNotDefined()

    def isGoalState(self, state):
      """
      state: Search state

      Returns True if and only if the state is a valid goal state
      """
      util.raiseNotDefined()

    def getSuccessors(self, state):
      """
      state: Search state

      For a given state, this should return a list of triples,
      (successor, action, stepCost), where 'successor' is a
      successor to the current state, 'action' is the action
      required to get there, and 'stepCost' is the incremental
      cost of expanding to that successor
      """
      util.raiseNotDefined()

    def getCostOfActions(self, actions):
      """
      actions: A list of actions to take

      This method returns the total cost of a particular sequence of actions.  The sequence must
      be composed of legal moves
      """
      util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

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
    #initialize visited set and the fringe traversing
    start = problem.getStartState()
    fringe = util.Stack()
    visited = []
    fringe.push((start,[]))

    #checks as long as there are still nodes in the fringe
    while not fringe.isEmpty():
      #gets the first and second indexes of the node being where your and the direction
        (currState, direction) = fringe.pop()
        #checks to make sure agent is not at the goal state
        if problem.isGoalState(currState):
            return direction
        #checks to make sure that the agent is not traversing through the same node
        if currState in visited:
          continue
        #adds the traversed node into the visited set
        visited.append(currState)
        #gets the next nodes that are possible from the current one
        successor = problem.getSuccessors(currState)
        #iterates through all of the nodes getting the next coordinates, movement number and cost
        for coordinates, action, cost in successor:
          #checks to make sure that the next coordinate has not been traversed
          if coordinates not in visited:
            #adds the next coordinates into the finge including the direction and the movement number
            directions = direction + [action]
            fringe.push((coordinates,directions))

def breadthFirstSearch(problem):
    #initialize visited set and the fringe traversing
    start = problem.getStartState()
    fringe = util.Queue()
    visited = []
    fringe.push((start,[]))

    #checks as long as there are still nodes in the fringe
    while not fringe.isEmpty():
      #gets the first and second indexes of the node being where your and the direction
        (currState, direction) = fringe.pop()
        #checks to make sure agent is not at the goal state
        if problem.isGoalState(currState):
            return direction
        #checks to make sure that the agent is not traversing through the same node
        if currState in visited:
          continue
        #adds the traversed node into the visited set
        visited.append(currState)
        #gets the next nodes that are possible from the current one
        successor = problem.getSuccessors(currState)
        #iterates through all of the nodes getting the next coordinates, movement number and cost
        for coordinates, action, cost in successor:
          #checks to make sure that the next coordinate has not been traversed
          if coordinates not in visited:
            #adds the next coordinates into the finge including the direction and the movement number
            directions = direction + [action]
            fringe.push((coordinates,directions))

def uniformCostSearch(problem):
    #initialize visited set and the fringe traversing
    start = problem.getStartState()
    fringe = util.PriorityQueue()
    visited = []
    fringe.push((start,[],0),0)

    #checks as long as there are still nodes in the fringe
    while not fringe.isEmpty():
      #gets the first and second indexes of the node being where your and the direction
        (currState, direction, currCost) = fringe.pop()
        #checks to make sure agent is not at the goal state
        if problem.isGoalState(currState):
            return direction
        #checks to make sure that the agent is not traversing through the same node
        if currState in visited:
          continue
        #adds the traversed node into the visited set
        visited.append(currState)
        #gets the next nodes that are possible from the current one
        successor = problem.getSuccessors(currState)
        #iterates through all of the nodes getting the next coordinates, movement number and cost
        for coordinates, action, cost in successor:
          #checks to make sure that the next coordinate has not been traversed
          if coordinates not in visited:
            #adds the next coordinates into the finge including the direction and the movement number
            directions = direction + [action]
            #Calculates the new cost needed to travel with the uniform cost
            newCost = cost+currCost
            fringe.push((coordinates,directions,newCost),newCost)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    #initialize visited set and the fringe traversing
    start = problem.getStartState()
    fringe = util.PriorityQueue()
    visited = []
    fringe.push((start,[],0),0)

    #checks as long as there are still nodes in the fringe
    while not fringe.isEmpty():
      #gets the first and second indexes of the node being where your and the direction
        (currState, direction, currCost) = fringe.pop()
        #checks to make sure agent is not at the goal state
        if problem.isGoalState(currState):
            return direction
        #checks to make sure that the agent is not traversing through the same node
        if currState in visited:
          continue
        #adds the traversed node into the visited set
        visited.append(currState)
        #gets the next nodes that are possible from the current one
        successor = problem.getSuccessors(currState)
        #iterates through all of the nodes getting the next coordinates, movement number and cost
        for coordinates, action, cost in successor:
          #checks to make sure that the next coordinate has not been traversed
          if coordinates not in visited:
            #adds the next coordinates into the finge including the direction and the movement number
            directions = direction + [action]
            #calculates the new cost needed by adding the currentCost and the uniform cost
            newCost = cost+currCost
            #gets the cost needed for the new cost and the heurstic number in mind
            primaryCost = newCost+heuristic(coordinates,problem)
            fringe.push((coordinates,directions,newCost),primaryCost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
