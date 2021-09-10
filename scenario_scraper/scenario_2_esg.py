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
        prev_node.next = given_node
        prev_node = given_node

        if scenario.step_groups['When'] is not None and len(scenario.step_groups['When'].get_steps_as_text()) > 0:
            when_node = EsgNode()
            when_node.label = scenario.step_groups['When'].get_steps_as_text()
            prev_node.next = when_node
            prev_node = when_node

        then_node = EsgNode()
        then_node.label = scenario.step_groups['Then'].get_steps_as_text()
        prev_node.next = then_node
        prev_node = then_node

        exit_node = EsgNode()
        exit_node.label = scenario.step_groups['Then'].get_tag()
        exit_node.isTag = True
        prev_node.next = exit_node

        segments.append(entry_node)
    print(segments)

if __name__ == '__main__':
    scenarios = scenario_extractor.get_scenarios_from_directory('test_scenarios/tag_testing')
    create_tagged_esg_segments(scenarios)
