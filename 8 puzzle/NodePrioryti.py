class NodePriorityComparator:
    def __call__(self, x, y):
        if x.get_total_cost() < y.get_total_cost():
            return -1
        if x.get_total_cost() > y.get_total_cost():
            return 1
        return 0
