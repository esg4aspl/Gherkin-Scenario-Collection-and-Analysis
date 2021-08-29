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

    x.append(-0.1)
    tp.append(match_count)
    fp.append(not_match_count)
    fn.append(0)
    tn.append(0)

    accuracy = []
    for i in range(0, len(x)):
        accuracy.append((tp[i] + tn[i]) / (tp[i] + tn[i] + fp[i] + fn[i]))

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
        fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    else:
        fig, (ax1) = plt.subplots(1)
    fig.suptitle('TODO')
    ax1.grid(axis='x', color='0.95')
    ax1.stackplot(x, tp, tn, fn, fp, labels=['TP', 'TN', 'FN', 'FP'], step='post')
    ax1.step(x, accuracy_for_stacked, where='post', linestyle='dashed', linewidth=7)
    if normalize:
        ax1.set_ylabel('Rate')
    else:
        ax1.set_ylabel('Clause Pair Count')
    ax1.legend(loc='upper left')

    if accuracy_plot:
        ax2.step(x, accuracy, where='post', label='accuracy', linewidth=7)
        ax2.legend(loc='upper left')
        ax2.grid(axis='x', color='0.95')
        ax2.set_ylabel('Rate')
    plt.xlabel('Threshold')

    # giving a title to my graph

    # function to show the plot
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