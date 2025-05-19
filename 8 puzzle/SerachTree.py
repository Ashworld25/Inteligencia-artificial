import heapq
from collections import deque
import math

class Node:
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.children = []
        self.cost = 0
        self.depth = 0

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def set_depth(self, depth):
        self.depth = depth

    def get_depth(self):
        return self.depth

class NodeUtil:
    @staticmethod
    def get_successors(state):
        # Implement the logic to get successors of the given state
        # This function should return a list of successor states
        return []

    @staticmethod
    def print_solution(current_node, state_sets, root, time):
        # Implement the logic to print the solution path
        pass

class SearchTree:
    def __init__(self, root, goal_state):
        self.root = root
        self.goal_state = goal_state

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def get_goal_state(self):
        return self.goal_state

    def set_goal_state(self, goal_state):
        self.goal_state = goal_state

    def breadth_first_search(self):
        state_sets = set()
        total_cost = 0
        time = 0
        node = Node(self.root.get_state())
        queue = deque([node])
        current_node = node

        while current_node.get_state() != self.goal_state:
            state_sets.add(current_node.get_state())
            node_successors = NodeUtil.get_successors(current_node.get_state())
            for n in node_successors:
                if n in state_sets:
                    continue
                state_sets.add(n)
                child = Node(n)
                current_node.add_child(child)
                child.set_parent(current_node)
                queue.append(child)

            current_node = queue.popleft()
            time += 1

        NodeUtil.print_solution(current_node, state_sets, self.root, time)

    def depth_first_search(self):
        state_sets = set()
        total_cost = 0
        time = 0
        node = Node(self.root.get_state())
        main_queue = deque([node])
        current_node = node

        while current_node.get_state() != self.goal_state:
            state_sets.add(current_node.get_state())
            node_successors = NodeUtil.get_successors(current_node.get_state())
            for n in node_successors:
                if n in state_sets:
                    continue
                state_sets.add(n)
                child = Node(n)
                current_node.add_child(child)
                child.set_parent(current_node)
                main_queue.appendleft(child)

            current_node = main_queue.popleft()
            time += 1

        NodeUtil.print_solution(current_node, state_sets, self.root, time)

    def uniform_cost_search(self):
        state_sets = set()
        total_cost = 0
        time = 0
        node = Node(self.root.get_state())
        node.set_cost(0)
        node_priority_queue = []
        heapq.heappush(node_priority_queue, (node.get_cost(), node))
        current_node = node

        while current_node.get_state() != self.goal_state:
            state_sets.add(current_node.get_state())
            node_successors = NodeUtil.get_successors(current_node.get_state())
            for n in node_successors:
                if n in state_sets:
                    continue
                state_sets.add(n)
                child = Node(n)
                current_node.add_child(child)
                child.set_parent(current_node)
                child.set_cost(current_node.get_cost() + 1)  # Assuming each step cost is 1
                heapq.heappush(node_priority_queue, (child.get_cost(), child))

            current_node = heapq.heappop(node_priority_queue)[1]
            time += 1

        NodeUtil.print_solution(current_node, state_sets, self.root, time)

    def best_first_search(self):
        state_sets = set()
        total_cost = 0
        time = 0
        node = Node(self.root.get_state())
        node.set_cost(0)
        node_priority_queue = []
        heapq.heappush(node_priority_queue, (0, node))
        current_node = node

        while current_node.get_state() != self.goal_state:
            state_sets.add(current_node.get_state())
            node_successors = NodeUtil.get_successors(current_node.get_state())
            for n in node_successors:
                if n in state_sets:
                    continue
                state_sets.add(n)
                child = Node(n)
                current_node.add_child(child)
                child.set_parent(current_node)
                heuristic_cost = self.heuristic_one(child.get_state(), self.goal_state)
                child.set_cost(heuristic_cost)
                heapq.heappush(node_priority_queue, (child.get_cost(), child))

            current_node = heapq.heappop(node_priority_queue)[1]
            time += 1

        NodeUtil.print_solution(current_node, state_sets, self.root, time)

    def a_star(self, heuristic):
        state_sets = set()
        time = 0
        node = Node(self.root.get_state())
        node.set_cost(0)
        node_priority_queue = []
        heapq.heappush(node_priority_queue, (node.get_cost(), node))
        current_node = node

        while current_node.get_state() != self.goal_state:
            state_sets.add(current_node.get_state())
            node_successors = NodeUtil.get_successors(current_node.get_state())
            for n in node_successors:
                if n in state_sets:
                    continue
                state_sets.add(n)
                child = Node(n)
                current_node.add_child(child)
                child.set_parent(current_node)

                if heuristic == 'H_ONE':
                    heuristic_cost = self.heuristic_one(child.get_state(), self.goal_state)
                elif heuristic == 'H_TWO':
                    heuristic_cost = self.heuristic_two(child.get_state(), self.goal_state)
                elif heuristic == 'H_THREE':
                    heuristic_cost = self.heuristic_three(child.get_state(), self.goal_state)
                elif heuristic == 'H_FOUR':
                    heuristic_cost = self.heuristic_four(child.get_state(), self.goal_state)

                total_cost = current_node.get_cost() + 1 + heuristic_cost  # Assuming each step cost is 1
                child.set_cost(total_cost)
                heapq.heappush(node_priority_queue, (child.get_cost(), child))

            current_node = heapq.heappop(node_priority_queue)[1]
            time += 1

        NodeUtil.print_solution(current_node, state_sets, self.root, time)

    def iterative_deepening(self, depth_limit):
        solution_found = False
        state_sets = set()
        total_visited_states = set()
        time = 0

        for max_depth in range(1, depth_limit):
            state_sets.clear()
            main_queue = deque([Node(self.root.get_state())])
            current_node = main_queue[0]

            while main_queue:
                current_node = main_queue.popleft()
                time += 1
                if current_node.get_state() == self.goal_state:
                    solution_found = True
                    break
                if current_node.get_depth() < max_depth:
                    node_successors = NodeUtil.get_successors(current_node.get_state())
                    for n in node_successors:
                        if n in state_sets:
                            continue
                        state_sets.add(n)
                        child = Node(n)
                        current_node.add_child(child)
                        child.set_parent(current_node)
                        child.set_depth(current_node.get_depth() + 1)
                        main_queue.appendleft(child)

            if solution_found:
                break
            total_visited_states.update(state_sets)

        if not solution_found:
            print("No solution Found!")
        else:
            NodeUtil.print_solution(current_node, total_visited_states, self.root, time)

    def heuristic_one(self, current_state, goal_state):
        # Simple misplaced tiles heuristic
        return sum(1 for i, char in enumerate(current_state) if char != goal_state[i] and char != '0')

    def heuristic_two(self, current_state, goal_state):
        # Manhattan distance heuristic
        difference = 0
        for i, char in enumerate(current_state):
            if char != '0':
                goal_index = goal_state.index(char)
                current_x, current_y = divmod(i, 3)
                goal_x, goal_y = divmod(goal_index, 3)
                difference += abs(current_x - goal_x) + abs(current_y - goal_y)
        return difference

    def heuristic_three(self, current_state, goal_state):
        # Weighted Manhattan distance heuristic
        difference = 0
        for i, char in enumerate(current_state):
            if char != '0':
                goal_index = goal_state.index(char)
                current_x, current_y = divmod(i, 3)
                goal_x, goal_y = divmod(goal_index, 3)
                manhattan_distance = abs(current_x - goal_x) + abs(current_y - goal_y)
                difference += 2 * manhattan_distance - 1
        return difference
    
    def heuristic_four(self, current_state, goal_state):
        difference = 0
        for i in range(len(current_state)):
            if current_state[i] != '0':  # Ignorar el espacio vacío
                goal_index = goal_state.index(current_state[i])
                current_x, current_y = divmod(i, 3)
                goal_x, goal_y = divmod(goal_index, 3)
                difference += math.sqrt((current_x - goal_x) ** 2 + (current_y - goal_y) ** 2)
        return difference