class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def get_state(self):
        return self.state

    def get_parent(self):
        return self.parent

from enum import Enum
import copy

class MovementType(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class NodeUtil:
    @staticmethod
    def get_successors(state):
        successors = []

        index = state.index('0')
        if index in [0, 1, 2]:
            if index != 0:
                successors.append(NodeUtil._swap(state, index, index - 1))  # Move left
            if index != 2:
                successors.append(NodeUtil._swap(state, index, index + 1))  # Move right
            successors.append(NodeUtil._swap(state, index, index + 3))  # Move down
        elif index in [3, 4, 5]:
            if index != 3:
                successors.append(NodeUtil._swap(state, index, index - 1))  # Move left
            if index != 5:
                successors.append(NodeUtil._swap(state, index, index + 1))  # Move right
            successors.append(NodeUtil._swap(state, index, index + 3))  # Move down
            successors.append(NodeUtil._swap(state, index, index - 3))  # Move up
        else:  # index in [6, 7, 8]
            if index != 6:
                successors.append(NodeUtil._swap(state, index, index - 1))  # Move left
            if index != 8:
                successors.append(NodeUtil._swap(state, index, index + 1))  # Move right
            successors.append(NodeUtil._swap(state, index, index - 3))  # Move up

        return successors

    @staticmethod
    def _swap(state, i, j):
        state_list = list(state)
        state_list[i], state_list[j] = state_list[j], state_list[i]
        return ''.join(state_list)

    @staticmethod
    def print_solution(goal_node, visited_nodes, root, time):
        total_cost = 0
        solution_stack = []
        solution_stack.append(goal_node)

        while goal_node.get_state() != root.get_state():
            solution_stack.append(goal_node.get_parent())
            goal_node = goal_node.get_parent()

        solution_stack = solution_stack[::-1]  # Reverse the list to get the order from root to goal
        source_state = root.get_state()
        destination_state = None
        cost = 0

        for node in solution_stack:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            destination_state = node.get_state()
            if source_state != destination_state:
                print(f"Move {destination_state[source_state.index('0')]} {NodeUtil.find_transition(source_state, destination_state)}")
                cost = int(destination_state[source_state.index('0')])
                total_cost += cost

            source_state = destination_state
            print(f"Cost of the movement: {cost}")
            print("*******")
            print(f"* {node.get_state()[:3]} *")
            print(f"* {node.get_state()[3:6]} *")
            print(f"* {node.get_state()[6:]} *")
            print("*******")

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(f"** Number of transitions to get to the goal state from the initial state:  {len(solution_stack) - 1}")
        print(f"** Number of visited states:  {len(visited_nodes)}")
        print(f"** Total cost for this solution: {total_cost}")
        print(f"** Number of Nodes popped out of the queue: {time}")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    @staticmethod
    def find_transition(source, destination):
        zero_position_difference = destination.index('0') - source.index('0')
        if zero_position_difference == -3:
            return MovementType.DOWN
        elif zero_position_difference == 3:
            return MovementType.UP
        elif zero_position_difference == 1:
            return MovementType.LEFT
        elif zero_position_difference == -1:
            return MovementType.RIGHT
        return None
