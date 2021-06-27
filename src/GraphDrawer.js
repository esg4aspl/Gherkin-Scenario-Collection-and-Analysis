import Graph from "react-graph-vis";
import React from "react";
import convertTaggedScenariosToEsgSegments from "./ScenarioMerger";

function GraphDrawer(props) {

    if (!props.data || props.data.length === 0) {
        return <></>;
    }
    const esgSegments = convertTaggedScenariosToEsgSegments(props.data);
    const graph = {nodes: [], edges: []};
    esgSegments.forEach(esgSegment => travelEsgSegment(esgSegment, graph));

    const options = {
        layout: {
            hierarchical: true
        },
        edges: {
            color: "#000000"
        }
    };

    return (
        <Graph graph={graph} options={options} style={{height: "640px"}}/>
    )
}

function travelEsgSegment(esgSegment, graph) {
    graph.nodes.push({label: esgSegment.label, id: esgSegment.id});
    if (esgSegment.next) {
        esgSegment.next.forEach(destNode => graph.edges.push({from: esgSegment.id, to: destNode.id}));
        esgSegment.next.forEach(destNode => travelEsgSegment(destNode, graph));
    }
}

export default GraphDrawer;