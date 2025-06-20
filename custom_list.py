
class CustomList:
    """
    Custom list with recursive sum method.
    """
    def __init__(self, items=None):
        self.items = items if items else []

    def add(self, item):
        self.items.append(item)

    def recursive_sum(self, idx=0):
        if idx >= len(self.items):
            return 0
        return self.items[idx] + self.recursive_sum(idx + 1)