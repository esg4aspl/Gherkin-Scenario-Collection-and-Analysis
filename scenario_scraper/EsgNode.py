class EsgNode:

    instance_counter = 0

    def __init__(self):
        self.label = ''
        self.isTag = False
        self.next = []
        self.aggregatedGiven = ''
        self.aggregatedThen = ''
        self.is_to_be_removed = False
        self.isIncomplete = False
        self.isReachable = False
        self.canReachToFinal = False
        self.uid = EsgNode.instance_counter
        EsgNode.instance_counter = EsgNode.instance_counter + 1

    def is_complete_tag(self):
        return len(self.aggregatedGiven) > 0 and len(self.aggregatedThen) > 0

    def add_given_to_tag_node(self, text):
        self.aggregatedGiven += '|' + text

    def add_then_to_tag_node(self, text):
        self.aggregatedThen += '|' + text

    def is_descendent_complete_tag(self):
        for descendent in self.next:
            if descendent.is_complete_tag():
                return True
        return False

    def append_descendents_of(self, other_node):
        for descendent in other_node.next:
            if descendent not in self.next:
                self.next.append(descendent)

    def get_label(self):
        if not self.is_complete_tag():
            return self.label
        else:
            return self.label + self.aggregatedThen + self.aggregatedGiven

    def is_initial_node(self):
        return self.isTag and self.label == '['

    def is_final_node(self):
        return self.isTag and self.label == ']'

    def is_incomplete(self):
        return (not self.isReachable) or (not self.canReachToFinal)
