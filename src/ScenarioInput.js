import {useState} from "react";
import {Button, Checkbox, Col, Drawer, Input, Row, Steps, Table} from 'antd';
import 'antd/dist/antd.css'
import {useColor} from "react-color-palette";
import "react-color-palette/lib/css/styles.css";
import {MinusCircleOutlined, PlusCircleOutlined} from '@ant-design/icons';
import {getInputColumns} from "./ScenarioInputHelper";

const _ = require('lodash');

const {Step} = Steps;

function ScenarioInput(props) {

    const [dataState, setDataStateProtected] = useState([]);
    const setDataState = (dataState) => {
        setDataStateProtected(dataState);
        if (autoDrawEnabled) {
            props.handleDrawClick(_.cloneDeep(dataState), {...drawOptions});
        }
    }

    const [autoDrawEnabled, setAutoDrawEnabled] = useState(false);
    const [uniqueRowCounter, setUniqueRowCounter] = useState(0);
    const [drawOptions, setDrawOptionsProtected] = useState({convertLevel: 0, hierarchical: false})
    const setDataOptions = (drawOptions) => {
        setDrawOptionsProtected(drawOptions);
        if (autoDrawEnabled) {
            props.handleDrawClick(_.cloneDeep(dataState), {...drawOptions});
        }
    }
    const [color, setColor] = useColor("hex", "#121212");
    const dataStateCopy = [...dataState];
    const [drawerVisible, setDrawerVisible] = useState(false);
    const [editingScenarioId, setEditingScenarioId] = useState();
    const types = ['given', 'when', 'then'];

    const handleScenarioEdit = (event, step) => {
        step.name = event.target.value;
        setDataState(dataStateCopy);
    }

    const handleScenarioStepDelete = (steps, stepToDelete) => {
        const deleteIndex = steps.findIndex(aStep => aStep === stepToDelete);
        steps.splice(deleteIndex, 1);
        setDataState(dataStateCopy);
    };

    const handleScenarioStepAdd = (steps, type) => {
        debugger
        // find last index matching
        let insertAfterIndex = -1;
        steps.forEach((aStep, index) => (aStep.type === type) && (insertAfterIndex = index));
        steps.splice(insertAfterIndex + 1, 0, {name: '', type});
        setDataState(dataStateCopy);
    };

    const drawTypeGroup = (steps, currentType) => {
        return (
            <div>
                {steps.filter((step) => step.type === currentType)
                    .map((step, id, orgArray) => {
                        return (
                            <div>
                                <Row>
                                    <Col span={20}>
                                        <Input
                                            addonBefore={id === 0 ? step.type : 'and'}
                                            value={step.name}
                                            onChange={(event => {
                                                handleScenarioEdit(event, step)
                                            })}/>
                                    </Col>
                                    <Col span={4}>
                                        {orgArray.length > 1 && <MinusCircleOutlined onClick={() =>
                                            handleScenarioStepDelete(steps, step)
                                        }/>}
                                    </Col>
                                </Row>
                            </div>
                        );
                    })}
                <Button onClick={() => handleScenarioStepAdd(steps, currentType)}><PlusCircleOutlined/>{currentType}
                </Button>
            </div>
        );
    };

    const handleFieldUpdate = (index, fieldName, value) => {
        if (fieldName === 'isStartNode' || fieldName === 'isEndNode') {
            handleStartOrEndTagUpdate(index, fieldName === 'isStartNode', value);
        }
        dataStateCopy[index][fieldName] = value;
        setDataState(dataStateCopy)
    }

    const handleStartOrEndTagUpdate = (index, isStart, value) => {
        // convert tag to '[' or ']' if value is set
        // o.w. convert tag to placeholder
        if (value) {
            if (isStart) {
                dataStateCopy[index].startTag = '[';
            } else {
                dataStateCopy[index].endTag = ']';
            }
        } else {
            if (isStart) {
                dataStateCopy[index].startTag = `#startTag-${dataStateCopy[index].id}`;
            } else {
                dataStateCopy[index].endTag = `#endTag-${dataStateCopy[index].id}`;
            }
        }
    }

    const handleScenarioClick = (index) => {
        setEditingScenarioId(index);
        setDrawerVisible(true);
    }

    const handleRowDelete = (index) => {
        dataStateCopy.splice(index, 1);
        setDataState(dataStateCopy);
    }

    return (
        <div>
            <Table columns={getInputColumns(handleFieldUpdate, handleScenarioClick, handleRowDelete)}
                   dataSource={dataStateCopy}/>

            <Row justify={'space-between'} gutter={[0, 8]}>
                <Col span={24}>
                    <Button block onClick={() => {
                        dataStateCopy.push({
                            id: uniqueRowCounter,
                            startTag: `#startTag-${uniqueRowCounter}`,
                            scenario: {
                                name: `#scenario-${uniqueRowCounter}`,
                                steps: [
                                    {name: 'a given', type: 'given'},
                                    {name: 'a when', type: 'when'},
                                    {name: 'a then', type: 'then'},
                                ]
                            },
                            endTag: `#endTag-${uniqueRowCounter}`
                        });
                        setDataState(dataStateCopy);
                        setUniqueRowCounter(uniqueRowCounter + 1);
                    }}>Add Row</Button>
                </Col>
                <Col span={24}>
                    <Steps current={drawOptions.convertLevel}
                           onChange={(chosen) => {
                               setDataOptions({...drawOptions, convertLevel: chosen})
                           }}>
                        <Step title="Tagged Scenarios"/>
                        <Step title="Merge Tags"/>
                        <Step title="Expand Scenarios"/>
                        <Step disabled title="Remove Tags"/>
                    </Steps>
                </Col>
                <Col span={3}>
                    <Checkbox
                        checked={autoDrawEnabled}
                        onClick={() => {
                            setAutoDrawEnabled(!autoDrawEnabled)
                        }}
                    >Autodraw</Checkbox>
                </Col>
                <Col span={3}>
                    <Checkbox
                        checked={drawOptions.hierarchical}
                        onClick={() => {
                            setDataOptions({...drawOptions, hierarchical: !drawOptions.hierarchical})
                        }}
                    >Hierarchical</Checkbox>
                </Col>
                <Col span={18}>
                    <Button block onClick={() => {
                        props.handleDrawClick(dataState, drawOptions);
                    }}>Draw</Button>
                </Col>
            </Row>
            {/*<Row>*/}
            {/*    <ColorPicker width={456} height={228} color={color} onChange={setColor} hideHSV/>*/}
            {/*</Row>*/}
            <Drawer visible={drawerVisible} width={720} onClose={() => {
                setDrawerVisible(false)
            }}>
                {drawerVisible && (<div>
                    {
                        types.map((currentType) => {
                            return (drawTypeGroup(dataStateCopy[editingScenarioId].scenario.steps, currentType));
                        })
                    }
                </div>)
                }
            </Drawer>
        </div>
    )
}

export default ScenarioInput;