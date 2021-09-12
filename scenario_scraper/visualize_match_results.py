import matplotlib.pyplot as plt


class MatchResultVisualizer:

    def __init__(self):
        self.results_list = []

    def insert_match_to_match_order(self, match_orders, uid, step_def_name, result):
        if uid not in match_orders:
            match_orders[uid] = {'matchRank': 1, 'correctMatch': result['isMatched'], 'stepDefName': step_def_name}
        else:
            existing_entry = match_orders[uid]
            if existing_entry['correctMatch']:
                return
            existing_entry['matchRank'] = existing_entry['matchRank'] + 1
            existing_entry['correctMatch'] = result['isMatched']

    def get_cumulative_match_order(self, match_orders, normalizeX, normalizeY):
        match_counts_at_rank = [0] * (len(match_orders) + 1)
        for match_order in match_orders.values():
            if match_order['correctMatch']:
                match_counts_at_rank[match_order['matchRank']] += 1

        total_count = 0
        cumulative_match_orders = []
        for count in match_counts_at_rank:
            total_count += count
            cumulative_match_orders.append(total_count)

        if normalizeX:
            coeff = 100 / cumulative_match_orders[-1]
            for i in range(0, len(cumulative_match_orders)):
                cumulative_match_orders[i] *= coeff

        xdata = range(0, len(cumulative_match_orders))
        xdata = list(xdata)
        if normalizeY:
            coeff = 100 / xdata[-1]
            for i in range(0, len(xdata)):
                xdata[i] *= coeff
        return xdata, cumulative_match_orders

    def plot_match_order(self, results, header, delay_plot_show=False, normalizeX=False, normalizeY=False):
        xdata, cumulative_match_order = self.get_match_order_data(normalizeX, normalizeY, results)
        plt.plot(xdata, cumulative_match_order)
        plt.title(header['dataset'] + '\n' + 'Alg:' + header['algName'])
        plt.xlabel('Match Depth')
        plt.ylabel('# of Matches')
        if not delay_plot_show:
            plt.show()

    def get_match_order_data(self, normalizeX, normalizeY, results):
        match_orders = {}
        for result in results:
            self.insert_match_to_match_order(match_orders, result['x_uid'], result['x'], result)
            self.insert_match_to_match_order(match_orders, result['y_uid'], result['y'], result)
        for key in list(match_orders.keys()):
            if not match_orders[key]['correctMatch']:
                del match_orders[key]
        xdata, cumulative_match_order = self.get_cumulative_match_order(match_orders, normalizeX, normalizeY)
        return xdata, cumulative_match_order

    def visualize_results(self, results, header):
        self.results_list.append({'results': results, 'header': header})
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
        fig.suptitle(header['dataset'] + '\n' + 'Alg:' + header['algName'])
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
        self.plot_match_order(results, header)

    def plot_overall_graph(self):
        print_ready = True
        counter = 0
        for result in self.results_list:
            counter += 1
            xdata, cumulative_orders = self.get_match_order_data(True, True, result['results'])
            plt.plot(xdata, cumulative_orders, linewidth=7,
                     label='TD' + str(counter) if print_ready else result['header']['dataset'])
            print('TD', result['header']['dataset'], ',', ','.join(map(str, cumulative_orders)))
        plt.legend(loc='lower right')
        plt.title('Match Rate vs. Checking Depth')
        plt.xlabel('% of checked tags')
        plt.ylabel('% of matched tags')
        plt.savefig('all.svg')
        plt.savefig('all.png')
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
