class EsgNode:

    def __init__(self):
        self.label = ''
        self.isTag = False
        self.next = []

    def get_depth(self):
        depth = 1
        for node in self.next:
            depth = max(depth, node.get_depth() + 1)
        return depth
