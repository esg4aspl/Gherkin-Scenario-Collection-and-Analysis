import Graph from "react-graph-vis";
import React from "react";
import {convertTaggedScenariosToEsgSegments, expandScenarios, mergeTags} from "./ScenarioMerger";
import {Empty, Tabs} from "antd";
import CytoscapeWrapper from "./visualizers/cytoscape/CytoscapeWrapper";

const {TabPane} = Tabs;

function GraphDrawer(props) {

    const nodeColors = {
        tag: '#aaaaaa',
        scenario: '#ffffaa',
        given: '#aaaaff',
        when: '#aaffaa',
        then: '#ffaaaa',
    }

    const travelEsgSegment = (esgSegment, graph, visitedNodes) => {
        if (visitedNodes[esgSegment.id]) {
            // handle possible cyclic paths
            return;
        }
        graph.nodes.push({label: esgSegment.label, id: esgSegment.id, color: nodeColors[esgSegment.type]});
        visitedNodes[esgSegment.id] = true;
        if (esgSegment.next) {
            esgSegment.next.forEach(destNode => graph.edges.push({from: esgSegment.id, to: destNode.id}));
            esgSegment.next.forEach(destNode => travelEsgSegment(destNode, graph, visitedNodes));
        }
    }

    if (!props.data || props.data.length === 0) {
        return <Empty/>;
    }
    let esgSegments = convertTaggedScenariosToEsgSegments(props.data);
    if (props.options.convertLevel > 0) {
        esgSegments = mergeTags(esgSegments);
    }
    if (props.options.convertLevel > 1) {
        esgSegments = expandScenarios(esgSegments);
    }
    const graph = {nodes: [], edges: [], links: []};
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
        <div>
            <Tabs>
                <TabPane tab={'Cytoscape'} key={1}><CytoscapeWrapper graph={graph} style={{height: "640px"}}/></TabPane>
                <TabPane tab={'vis.js'} key={2}><Graph graph={graph} options={options}
                                                       style={{height: "640px"}}/></TabPane>
            </Tabs>

        </div>
    )
}


export default GraphDrawer;