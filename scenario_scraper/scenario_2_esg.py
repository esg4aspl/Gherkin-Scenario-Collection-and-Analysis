import scenario_extractor
from EsgNode import EsgNode


def create_tagged_esg_segments(scenarios):
    segments = []
    for scenario in scenarios:
        entry_node = EsgNode()
        entry_node.label = scenario.step_groups['Given'].get_tag()
        entry_node.isTag = True
        prev_node = entry_node

        given_node = EsgNode()
        given_node.label = scenario.step_groups['Given'].get_steps_as_text()
        prev_node.next.append(given_node)
        prev_node = given_node

        if scenario.step_groups['When'] is not None and len(scenario.step_groups['When'].get_steps_as_text()) > 0:
            when_node = EsgNode()
            when_node.label = scenario.step_groups['When'].get_steps_as_text()
            prev_node.next.append(when_node)
            prev_node = when_node

        then_node = EsgNode()
        then_node.label = scenario.step_groups['Then'].get_steps_as_text()
        prev_node.next.append(then_node)
        prev_node = then_node

        exit_node = EsgNode()
        exit_node.label = scenario.step_groups['Then'].get_tag()
        exit_node.isTag = True
        prev_node.next.append(exit_node)

        segments.append(entry_node)
    return segments


def merge_tags(segments):
    discovered_tags = {}
    for segment in segments:
        match_tags_helper(segment, discovered_tags, None)

    # after tag merging, some of the entry tags will remain in segments with their successors moved to its matching tag
    # remove those segments with len==1
    for segment in segments:
        if len(segment.next) == 0:
            segments.remove(segment)


def match_tags_helper(node, discovered_tags, previous_node):
    # pre-order depth first travel down the segment with prev node tracking to find matching tags
    # if a matching tag is found, move one tag's ancestor and successors to the other tag
    next_nodes = node.next
    if node.isTag:
        if node.label in discovered_tags:
            matching_tag_node = discovered_tags[node.label]
            # move next nodes to found match
            matching_tag_node.next.extend(node.next)
            node.next = []
            if previous_node is not None:
                # point prev node to found match
                # this method counts on node having a single parent (i.e. segment is a tree)
                previous_node.next.remove(node)
                previous_node.next.append(matching_tag_node)
        else:
            discovered_tags[node.label] = node
    for next_node in next_nodes:
        match_tags_helper(next_node, discovered_tags, node)


def remove_complete_tags(segments):
    fill_and_mark_complete_tags(segments)
    mark_nodes_to_be_removed(segments)
    remove_marked_nodes(segments)


def fill_and_mark_complete_tags(segments):
    visited_nodes = set()
    queue = []
    for segment in segments:
        queue.append(segment)

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node in visited_nodes:
            continue
        print(current_node.label)
        visited_nodes.add(current_node)
        for descendent in current_node.next:
            queue.append(descendent)
            if current_node.isTag:
                current_node.add_then_to_tag_node(descendent.label)
            if descendent.isTag:
                descendent.add_given_to_tag_node(current_node.label)


def mark_nodes_to_be_removed(segments):
    visited_nodes = set()
    queue = []
    for segment in segments:
        queue.append(segment)

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node in visited_nodes:
            continue
        print(current_node.label)
        visited_nodes.add(current_node)
        for descendent in current_node.next:
            queue.append(descendent)
            if current_node.is_complete_tag():
                descendent.is_to_be_removed = True
            if descendent.is_complete_tag():
                current_node.is_to_be_removed = True


def remove_marked_nodes(segments):
    visited_nodes = set()
    queue = []
    for segment in segments:
        queue.append(segment)

    while len(queue) > 0:
        current_node = queue.pop(0)
        if current_node in visited_nodes:
            continue
        print(current_node.label)
        visited_nodes.add(current_node)
        copy_of_descendents = current_node.next[:]
        for descendent in copy_of_descendents:
            queue.append(descendent)
            if descendent.is_to_be_removed:
                # remove removed node from current's descendents
                # and move removed node's descendents to current node
                current_node.next.remove(descendent)
                current_node.append_descendents_of(descendent)


if __name__ == '__main__':
    scenarios = scenario_extractor.get_scenarios_from_directory('test_scenarios/tag_testing')
    segments = create_tagged_esg_segments(scenarios)
    merge_tags(segments)
    remove_complete_tags(segments)
    print(segments)
