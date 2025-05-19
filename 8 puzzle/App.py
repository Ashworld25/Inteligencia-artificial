import time
from enum import Enum
from queue import PriorityQueue

EASY = "134862705"
MEDIUM = "281043765"
HARD = "567408321"
GOAL_STATE = "123804765"

class MovementType(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.total_cost = 0

    def add_child(self, child):
        self.children.append(child)

    def get_state(self):
        return self.state

    def get_total_cost(self):
        return self.total_cost

    def set_total_cost(self, cost):
        self.total_cost = cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost

class SearchTree:
    def __init__(self, root, goal_state):
        self.root = root
        self.goal_state = goal_state
        self.state_sets = set()

    def best_first_search(self):
        queue = PriorityQueue()
        queue.put((0, self.root))
        time_spent = 0

        while not queue.empty():
            _, current_node = queue.get()
            current_state = current_node.get_state()

            if current_state == self.goal_state:
                NodeUtil.print_solution(current_node, self.state_sets, self.root, time_spent)
                return

            self.state_sets.add(current_state)
            for successor in NodeUtil.get_successors(current_state):
                if successor not in self.state_sets:
                    child_node = Node(successor)
                    child_node.set_total_cost(NodeUtil.calculate_heuristic(successor))
                    current_node.add_child(child_node)
                    child_node.parent = current_node
                    queue.put((child_node.get_total_cost(), child_node))

            time_spent += 1

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
    def print_solution(goal_node, visited_nodes, root, time_spent):
        total_cost = 0
        solution_stack = []
        while goal_node:
            solution_stack.append(goal_node)
            goal_node = goal_node.parent

        solution_stack.reverse()
        source_state = root.get_state()
        for node in solution_stack:
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            destination_state = node.get_state()
            if source_state != destination_state:
                move_cost = int(destination_state[source_state.index('0')])
                transition = NodeUtil.find_transition(source_state, destination_state)
                print(f"Move {destination_state[source_state.index('0')]} {transition}")
                print(f"Cost of the movement: {move_cost}")
                total_cost += move_cost
            else:
                move_cost = 0  # Initialize move_cost to avoid uninitialized usage
            source_state = destination_state
            print("*******")
            print(f"* {node.get_state()[:3]} *")
            print(f"* {node.get_state()[3:6]} *")
            print(f"* {node.get_state()[6:]} *")
            print("*******")

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(f"** Number of transitions to get to the goal state from the initial state:  {len(solution_stack) - 1}")
        print(f"** Number of visited states:  {len(visited_nodes)}")
        print(f"** Total cost for this solution: {total_cost}")
        print(f"** Number of Nodes popped out of the queue: {time_spent}")
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

    @staticmethod
    def calculate_heuristic(state):
        # Dummy heuristic function
        return 0

if __name__ == "__main__":
    root_state = MEDIUM
    start_time = time.time()

    search= SearchTree(Node(root_state), GOAL_STATE)
    search.best_first_search()
    ##search.DepthSearch()
    ##search.heuristic_four()

    finish_time = time.time()
    total_time = finish_time - start_time
    print(f"Time: {total_time:.2f} seconds")
