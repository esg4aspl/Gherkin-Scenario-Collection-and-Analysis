import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


class EsgVisualizerNetworkX:

    def temp(self, esg_segments):
        edge_from = []
        edge_to = []
        uids = []
        colors = []
        labels = {}

        visited_nodes = set()
        for esg_segment in esg_segments:
            queue = [esg_segment]
            while len(queue) != 0:
                current_node = queue.pop(0)
                if current_node.uid in visited_nodes:
                    continue
                visited_nodes.add(current_node.uid)
                uids.append(current_node.uid)
                color = 'skyblue'
                if not current_node.isReachable:
                    color = 'orange'
                if not current_node.canReachToFinal:
                    color = 'yellow'
                if not current_node.canReachToFinal and not current_node.isReachable:
                    color = 'red'
                colors.append(color)
                # if current_node.is_incomplete() and current_node.isTag:
                #     colors.append('yellow')
                # elif current_node.is_incomplete() and not current_node.isTag:
                #     colors.append('red')
                # else:
                #     colors.append('skyblue')
                labels[current_node.uid] = current_node.get_label()
                for neighbor in current_node.next:
                    edge_from.append(current_node.uid)
                    edge_to.append(neighbor.uid)
                    queue.append(neighbor)

        # Build a dataframe with your connections
        # df = pd.DataFrame({'from': ['A', 'B', 'C', 'A'], 'to': ['D', 'A', 'E', 'C']})
        df = pd.DataFrame({'from': edge_from, 'to': edge_to})

        # And a data frame with characteristics for your nodes
        # carac = pd.DataFrame(
        #     {'ID': ['A', 'B', 'C', 'D', 'E'], 'myvalue': ['skyblue', 'red', 'green', 'yellow', 'blue']})
        carac = pd.DataFrame(
            {'ID': uids, 'myvalue': colors})

        # Build your graph
        # G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())
        G = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())

        # The order of the node for networkX is the following order:
        G.nodes()
        # Thus, we cannot give directly the 'myvalue' column to netowrkX, we need to arrange the order!

        # Here is the tricky part: I need to reorder carac to assign the good color to each node
        carac = carac.set_index('ID')
        carac = carac.reindex(G.nodes())

        # And I need to transform my categorical column in a numerical value: group1->1, group2->2...
        # carac['myvalue'] = pd.Categorical(carac['myvalue'])
        # carac['myvalue'].cat.codes

        # Custom the nodes:
        # nx.draw(G, with_labels=True, node_color=carac['myvalue'].cat.codes, cmap=plt.cm.Set1, node_size=1500)
        nx.draw(G, labels=labels, node_color=carac['myvalue'], node_size=1500)
        # nx.draw(G, with_labels=True, node_color=carac['myvalue'], node_size=1500)
        plt.show()
        plt.savefig('asdf.png')


if __name__ == '__main__':
    vis = EsgVisualizer()
    vis.temp()
