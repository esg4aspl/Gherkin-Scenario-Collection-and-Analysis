import Graph from "react-graph-vis";
import React from "react";
import {convertTaggedScenariosToEsgSegments, mergeTags} from "./ScenarioMerger";
import {Empty} from "antd";

function GraphDrawer(props) {

    if (!props.data || props.data.length === 0) {
        return <Empty/>;
    }
    let esgSegments = convertTaggedScenariosToEsgSegments(props.data);
    if (props.options.convertLevel > 0) {
        esgSegments = mergeTags(esgSegments);
    }
    const graph = {nodes: [], edges: []};
    esgSegments.forEach(esgSegment => travelEsgSegment(esgSegment, graph, {}));

    const options = {
        layout: {
            hierarchical: props.options.hierarchical,
        },
        edges: {
            color: "#000000"
        }
    };

    return (
        <Graph graph={graph} options={options} style={{height: "640px"}}/>
    )
}

function travelEsgSegment(esgSegment, graph, visitedNodes) {
    if (visitedNodes[esgSegment.id]) {
        // handle possible cyclic paths
        return;
    }
    graph.nodes.push({label: esgSegment.label, id: esgSegment.id});
    visitedNodes[esgSegment.id] = true;
    if (esgSegment.next) {
        esgSegment.next.forEach(destNode => graph.edges.push({from: esgSegment.id, to: destNode.id}));
        esgSegment.next.forEach(destNode => travelEsgSegment(destNode, graph, visitedNodes));
    }
}

export default GraphDrawer;