import React, {useState} from "react";
import ScenarioInput from "./ScenarioInput";
import GraphDrawer from "./GraphDrawer";
import ReactDOM from "react-dom";

const App = () => {

    const [data, setData] = useState([])
    const [options, setOptions] = useState([])
    const handleDrawClick = (data, options) => {
        setData(data);
        setOptions(options);
    }
    return (
        <div style={{padding: '40px'}}>
            <div style={{border: '1px solid', margin: '40px'}}>
                <ScenarioInput handleDrawClick={handleDrawClick}/>
            </div>
            <div style={{border: '1px solid', margin: '40px'}}>
                <GraphDrawer data={data} options={options}/>
            </div>
        </div>
    );

}

ReactDOM.render(
    <App/>,
    document.getElementById("root")
);