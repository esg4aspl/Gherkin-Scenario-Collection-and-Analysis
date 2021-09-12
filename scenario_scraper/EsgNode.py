class EsgNode:

    def __init__(self):
        self.label = ''
        self.isTag = False
        self.next = []
        self.aggregatedGiven = ''
        self.aggregatedThen = ''
        self.is_to_be_removed = False

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

