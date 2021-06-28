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
        <div>
            <ScenarioInput handleDrawClick={handleDrawClick}/>
            <GraphDrawer data={data} options={options}/>
        </div>
    );

}

ReactDOM.render(
    <App/>,
    document.getElementById("root")
);