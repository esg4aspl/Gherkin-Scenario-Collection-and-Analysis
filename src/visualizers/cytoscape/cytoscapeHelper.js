export function convertToCytoscapeInput(graph) {
    const convertedGraph = [];
    graph.nodes.forEach(node => convertedGraph.push({data: {id: node.id, label: node.label}}));
    graph.edges.forEach(edge => convertedGraph.push({data: {source: edge.from, target: edge.to}}));
    return convertedGraph;
}