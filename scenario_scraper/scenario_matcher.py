import scenario_extractor
import semantic_similarity_nltk


def match_scenarios_in_directory(directory):
    scenarios = scenario_extractor.get_scenarios_from_directory(directory)
    # semantic_similarity_nltk.cosine_sim(scenarios[0].get_step_as_text('Given'), scenarios[1].get_step_as_text('Given'), verbose=True)
    # semantic_similarity_nltk.cosine_sim(scenarios[1].get_step_as_text('Given'), scenarios[2].get_step_as_text('Given'), verbose=True)
    # semantic_similarity_nltk.cosine_sim(scenarios[2].get_step_as_text('Given'), scenarios[0].get_step_as_text('Given'), verbose=True)

    corpus = []
    for scenario in scenarios:
        corpus.append(scenario.get_steps_as_text('Given'))
    for scenario in scenarios:
        corpus.append(scenario.get_steps_as_text('Then'))

    pw = semantic_similarity_nltk.get_pairwise_similarity_form_corpus(corpus)
    print(pw)
    results = []
    for x in range(0, int(len(corpus))):
        for y in range(0, x):
            results.append({'score': pw[x][y], 'x': get_readable_result(scenarios, x), 'y': get_readable_result(scenarios, y)})

    def compare_attr_getter(item):
        if 'score' not in item:
            return -float('inf')
        else:
            return item['score']

    results.sort(key=lambda x: compare_attr_getter(x), reverse=True)
    for item in results:
        print(item)


def get_readable_result(scenarios, x):
    size = len(scenarios)
    if x < size:
        type = 'Given'
    else:
        x = x - size
        type = 'Then'
    return type + ' of Scenario:' + scenarios[int(x)].scenario_name



if __name__ == '__main__':
    match_scenarios_in_directory('test_scenarios/tag_testing')
    # match_scenarios_in_directory('test_scenarios/tuglular_v1')
