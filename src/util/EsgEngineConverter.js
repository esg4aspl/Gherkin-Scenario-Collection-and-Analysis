export function convertToEsgEngineFormat(graph) {
    const result = {name: 'exportedEsg', ID: 0}
    result.vertices = graph.nodes.map(node => {
        return {ID: node.id, event: node.label}
    });
    let edgeIdCounter = Number.MAX_SAFE_INTEGER;
    result.edges = graph.edges.map(edge => {
        return {source: edge.from, target: edge.to, ID: edgeIdCounter--}
    })
    return result;
}