import Graph from "react-graph-vis";
import React from "react";

function GraphDrawer(props) {

    if(!props.data || props.data.length === 0){
        return <></>;
    }
    const graph = {
        nodes: [
            {id: 1, label: "Node 1", color: "#e04141"},
            {id: 2, label: "Node 2", color: "#e09c41"},
            {id: 3, label: "Node 3", color: "#e0df41"},
            {id: 4, label: "Node 4", color: "#7be041"},
            {id: 5, label: "Node 5", color: "#41e0c9"},
            {id: 6, label: "Node 5", color: "#41e0c9"},
            {id: 7, label: "Node 5", color: "#41e0c9"},
            {id: 8, label: "Node 5", color: "#41e0c9"},
            {id: 9, label: "Node 5", color: "#41e0c9"},
        ],
            edges: [
            {from: 1, to: 2},
            {from: 1, to: 3},
            {from: 2, to: 4},
            {from: 2, to: 6},
            {from: 2, to: 7},
            {from: 2, to: 8},
            {from: 2, to: 9},
            {from: 5, to: 9},
            {from: 8, to: 9}
        ]
    };

    const options = {
        layout: {
            hierarchical: false
        },
        edges: {
            color: "#000000"
        }
    };

    return (
        <Graph graph={graph} options={options} style={{height: "640px"}}/>
    )
}

export default GraphDrawer;