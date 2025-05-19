class Node:
    def __init__(self, state):
        self.visited = False
        self.state = state
        self.children = []
        self.parent = None
        self.cost = 0
        self.estimated_cost_to_goal = 0
        self.total_cost = 0
        self.depth = 0

    def get_depth(self):
        return self.depth

    def set_depth(self, depth):
        self.depth = depth

    def is_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited

    def get_total_cost(self):
        return self.total_cost

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    def set_total_cost_with_estimation(self, cost, estimated_cost):
        self.total_cost = cost + estimated_cost

    def get_estimated_cost_to_goal(self):
        return self.estimated_cost_to_goal

    def set_estimated_cost_to_goal(self, estimated_cost_to_goal):
        self.estimated_cost_to_goal = estimated_cost_to_goal

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost

    def set_state(self, state):
        self.state = state

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_state(self):
        return self.state

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)
