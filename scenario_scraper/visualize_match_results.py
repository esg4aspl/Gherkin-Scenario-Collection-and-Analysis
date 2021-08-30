import matplotlib.pyplot as plt


def visualize_results(results):
    match_count = 0
    not_match_count = 0
    for result in results:
        if result['isMatched']:
            match_count += 1
        else:
            not_match_count += 1
    x = [1.1]
    tp = [0]
    fp = [0]
    tn = [not_match_count]
    fn = [match_count]

    for result in results:
        x.append(result['score'])
        if result['isMatched']:
            tp.append(tp[-1] + 1)
            fp.append(fp[-1])
            fn.append(fn[-1] - 1)
            tn.append(tn[-1])
        else:
            tp.append(tp[-1])
            fp.append(fp[-1] + 1)
            fn.append(fn[-1])
            tn.append(tn[-1] - 1)

    x.append(-0.5)
    tp.append(match_count)
    fp.append(not_match_count)
    fn.append(0)
    tn.append(0)

    accuracy = []
    fdr = []
    fomissionr = []
    tpr = []
    for i in range(0, len(x)):
        accuracy.append((tp[i] + tn[i]) / (tp[i] + tn[i] + fp[i] + fn[i]))
        fdr.append(fp[i] / ((fp[i] + tp[i]) if (fp[i] + tp[i] != 0) else 1))
        fomissionr.append(fn[i] / ((fn[i] + tn[i]) if (fn[i] + tn[i] != 0) else 1))
        tpr.append(tp[i] / ((fn[i] + tp[i]) if (fn[i] + tp[i] != 0) else 1))

    normalize = False

    if normalize:
        tn = [x / len(results) for x in tn]
        fn = [x / len(results) for x in fn]
        tp = [x / len(results) for x in tp]
        fp = [x / len(results) for x in fp]
        accuracy_for_stacked = accuracy
    else:
        accuracy_for_stacked = [x * len(results) for x in accuracy]

    accuracy_plot = True
    if accuracy_plot:
        fig, (all_stacked, should_match_stacked, metadata) = plt.subplots(3, sharex=True)
    else:
        fig, (all_stacked, should_match_stacked) = plt.subplots(2)
    fig.suptitle('TODO')
    all_stacked.grid(axis='x', color='0.95')
    all_stacked.stackplot(x, tp, tn, fn, fp, labels=['TP', 'TN', 'FN', 'FP'], step='post')
    all_stacked.step(x, accuracy_for_stacked, where='post', linestyle='dashed', linewidth=7)
    if normalize:
        all_stacked.set_ylabel('Rate')
    else:
        all_stacked.set_ylabel('Clause Pair Count')
    all_stacked.legend(loc='upper left')

    should_match_stacked.grid(axis='x', color='0.95')
    should_match_stacked.stackplot(x, tp, fn, labels=['TP', 'FN'], step='post')
    if normalize:
        should_match_stacked.set_ylabel('Rate')
    else:
        should_match_stacked.set_ylabel('Clause Pair Count')
    should_match_stacked.legend(loc='upper left')

    if accuracy_plot:
        metadata.step(x, accuracy, where='post', label='accuracy', linewidth=4)
        metadata.step(x, fdr, where='post', label='FDR', linewidth=4)
        metadata.step(x, fomissionr, where='post', label='FOR', linewidth=4)
        metadata.step(x, tpr, where='post', label='TPR', linewidth=4)
        metadata.legend(loc='upper left')
        metadata.grid(axis='x', color='0.95')
        metadata.set_ylabel('Rate')
        metadata.set_ylim([-0.1, 1.1])
    plt.xlabel('Threshold')

    plt.show()


if __name__ == '__main__':
    test_results = [
        {'score': 0.8, 'isMatched': True},
        {'score': 0.8, 'isMatched': True},
        {'score': 0.6, 'isMatched': True},
        {'score': 0.4, 'isMatched': False},
        {'score': 0.4, 'isMatched': False},
        {'score': 0.2, 'isMatched': False},
    ]

    visualize_results(test_results)
