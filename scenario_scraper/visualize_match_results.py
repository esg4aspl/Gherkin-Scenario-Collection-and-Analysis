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
        accuracy.append((tp[i] + tn[i]) / len(results))

    # plotting the points
    plt.stackplot(x, tp, tn, fn, fp, labels=['TP', 'TN', 'FN', 'FP'], step='post')
    plt.plot(x, accuracy)
    # plt.stackplot(x, tp)
    # plt.stackplot(x, fp)
    # plt.plot(x, tp)
    # plt.plot(x, fp)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')
    plt.legend(loc='upper left')

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
