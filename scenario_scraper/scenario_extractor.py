import os
import gherkin_parse_util
from Scenario import Scenario
from StepWithTag import StepWithTag


def get_scenarios_from_directory(directory):
    features = find_features_in_directory(directory)
    converted_scenarios = []
    for feature in features:
        file_path = directory + '/' + feature
        parsed_feature = get_feature_from_file(file_path)
        scenarios_from_file = extract_scenarios_from_feature(parsed_feature)
        for scenario in scenarios_from_file:
            scenario.file_name = file_path
        converted_scenarios.extend(scenarios_from_file)
    return converted_scenarios


def find_features_in_directory(directory):
    files = os.listdir(directory)
    feature_files = []
    for file in files:
        if file.endswith('.feature'):
            feature_files.append(file)
    return feature_files


def extract_scenarios_from_feature(parsed_feature):
    scenarios = []
    background = None
    blocks = parsed_feature['feature']['children']
    for block in blocks:
        if 'scenario' in block:
            scenarios.append(convert_parsed_scenario(block['scenario']))
        elif 'background' in block:
            background = extract_background(block['background'])
    for scenario in scenarios:
        scenario.feature_name = parsed_feature['feature']['name']
        if background is not None:
            scenario.steps['Given'] = background + scenario.steps['Given']
    return scenarios


def extract_background(parsed_background):
    steps = []
    for step in parsed_background['steps']:
        keyword = step['keyword'].strip()
        if keyword == 'Given':
            keyword = 'And'
        steps.append({'keyword': keyword, 'text': step['text']})
    return steps


def convert_parsed_scenario(parsed_scenario):
    segment_keywords = {'Given', 'When', 'Then'}
    inter_segment_keywords = {'And', 'But'}
    scenario = Scenario()
    scenario.scenario_name = parsed_scenario['name']
    last_seen_segment_keyword = 'Given'
    for step in parsed_scenario['steps']:
        keyword = step['keyword'].strip()
        if keyword in inter_segment_keywords:
            scenario.step_groups[last_seen_segment_keyword].append(StepWithTag(step['text'], keyword))
        elif keyword in segment_keywords:
            last_seen_segment_keyword = keyword
            scenario.step_groups[last_seen_segment_keyword].append(StepWithTag(step['text'], 'And'))
    return scenario


def get_feature_from_file(filename):
    f = open(filename, 'r')
    filecontent = f.read()
    feature = gherkin_parse_util.parse_text(filecontent)
    return feature


if __name__ == '__main__':
    t = get_scenarios_from_directory('scenarios')
    print(t)
