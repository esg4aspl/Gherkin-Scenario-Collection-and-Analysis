import React, {useState} from "react";
import ScenarioInput from "./ScenarioInput";
import GraphDrawer from "./GraphDrawer";
import ReactDOM from "react-dom";

const App = () => {

    const [data, setData] = useState([])
    return (
        <div>
            <ScenarioInput handleDrawClick={setData}/>
            <GraphDrawer data={data}/>
        </div>
    );

}

ReactDOM.render(
    <App/>,
    document.getElementById("root")
);