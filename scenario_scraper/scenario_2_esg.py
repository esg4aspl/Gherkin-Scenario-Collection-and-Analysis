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
        if segment.get_depth() == 1:
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


if __name__ == '__main__':
    scenarios = scenario_extractor.get_scenarios_from_directory('test_scenarios/tag_testing')
    segments = create_tagged_esg_segments(scenarios)
    merge_tags(segments)
    print(segments)

