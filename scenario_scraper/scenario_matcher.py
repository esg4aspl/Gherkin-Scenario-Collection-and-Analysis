import scenario_extractor
import semantic_similarity_nltk
import visualize_match_results


def match_scenarios_in_directory(directory):
    scenarios = scenario_extractor.get_scenarios_from_directory(directory)

    corpus = []
    scenarios_in_corpus = []
    scenario_steps_in_corpus = []
    for scenario in scenarios:
        corpus.append(scenario.step_groups['Given'].get_steps_as_text())
        scenarios_in_corpus.append(scenario)
        scenario_steps_in_corpus.append(scenario.step_groups['Given'])
    for scenario in scenarios:
        corpus.append(scenario.step_groups['Then'].get_steps_as_text())
        scenarios_in_corpus.append(scenario)
        scenario_steps_in_corpus.append(scenario.step_groups['Then'])

    pw = semantic_similarity_nltk.get_pairwise_similarity_form_corpus(corpus)
    print(pw)
    results = []
    for x in range(0, int(len(corpus))):
        for y in range(0, x):
            results.append({'score': pw[x][y],
                            'x': (scenario_steps_in_corpus[x].keyword + ' of ' + scenarios_in_corpus[x].scenario_name),
                            'y': (scenario_steps_in_corpus[y].keyword + ' of ' + scenarios_in_corpus[y].scenario_name),
                            'isMatched': scenario_steps_in_corpus[x].does_match(scenario_steps_in_corpus[y])})

    results.sort(key=lambda x: x['score'], reverse=True)
    for item in results:
        print(item)

    visualize_match_results.visualize_results(results)


if __name__ == '__main__':
    match_scenarios_in_directory('test_scenarios/tag_testing')
    # match_scenarios_in_directory('test_scenarios/tuglular_v1')
