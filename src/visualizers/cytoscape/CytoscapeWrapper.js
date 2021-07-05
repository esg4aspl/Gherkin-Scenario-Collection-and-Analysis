import cytoscape from 'cytoscape';
import {useEffect, useState} from "react";
import {convertToCytoscapeInput} from "./cytoscapeHelper";

function CytoscapeWrapper(props){
    let cyStyle = {
        height: '400px',
        width: '90%',
        display: 'block',
        border: '1px solid black'
    };

    let elements= [ ]

    let conf = {
        boxSelectionEnabled: false,
        autounselectify: true,
        zoomingEnabled: true,
        style: [
            {
                selector: 'node',
                style: {
                    // shape: 'hexagon',
                    // 'background-color': 'red',
                    label: 'data(label)'
                },
                //
            },
            {
                selector: 'edge',
                style: {
                    // 'curve-style': 'unbundled-bezier',
                    'curve-style': 'bezier',
                    // 'curve-style': 'straight',
                    'width': 3,
                    'line-color': '#ccc000',
                    'target-arrow-color': '#ffffff',
                    'source-arrow-color': '#ffffff',
                    'target-arrow-shape': 'triangle', // there are far more options for this property here: http://js.cytoscape.org/#style/edge-arrow
                    'mid-target-arrow-shape': 'triangle', // there are far more options for this property here: http://js.cytoscape.org/#style/edge-arrow
                    'source-arrow-shape': 'diamond' // there are far more options for this property here: http://js.cytoscape.org/#style/edge-arrow
                }
            }
        ],
        layout: {
            name: 'cose',
            // name: 'breadthfirst',
            // name: 'concentric',
            animate: false
        }
    };

    const [cy, setCy] = useState();
    const [cyRef, setCyRef] = useState();

    useEffect(()=>{
        conf.container = cyRef;
        conf.elements = elements;
        setCy( cytoscape(conf));
    },[cyRef])

    useEffect(()=>{
        console.log('a');
        debugger;
        if(cy){
            // cy.destroy();
        }
        conf.container = cyRef;
        conf.elements = convertToCytoscapeInput(props.graph);
        setCy( cytoscape(conf));
    },[props.graph]);

    return <div style={cyStyle} ref={(cyRef) => {
        setCyRef(cyRef);
    }}/>
}

export default CytoscapeWrapper;