import {useState} from "react";
import {Button, Checkbox, Col, Drawer, Input, Row, Steps} from 'antd';
import 'antd/dist/antd.css'
import {ColorPicker, useColor} from "react-color-palette";
import "react-color-palette/lib/css/styles.css";
import {EditOutlined} from '@ant-design/icons';

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

    return (
        <div style={{border: '1px solid', marginLeft: '40px', marginRight: '40px', marginTop: '40px'}}>
            <Row justify={'space-between'}>
                <Col span={1}>id</Col>
                <Col span={6}>startTag</Col>
                <Col span={6}>Scenario</Col>
                <Col span={6}>endTag</Col>
                <Col span={1}/>
            </Row>
            {dataStateCopy.map((row, id) => {
                return (
                    <>
                        <Row justify={'space-between'} key={id}
                             className='mb-2'>
                            <Col span={1}>{id}</Col>
                            <Col span={6}>
                                <Input onChange={event => {
                                    dataStateCopy[id].startTag = event.target.value;
                                    setDataState(dataStateCopy)
                                }} value={row.startTag}/>
                            </Col>
                            <Col span={6}>
                                <Button block onClick={() => {
                                    setEditingScenarioId(id);
                                    setDrawerVisible(true)
                                }}><EditOutlined/> {row.scenario.name}</Button>
                            </Col>
                            <Col span={6}>
                                <Input onChange={event => {
                                    dataStateCopy[id].endTag = event.target.value;
                                    setDataState(dataStateCopy)
                                }} value={row.endTag}/>
                            </Col>
                            <Col span={1}>
                                <Button onClick={() => {
                                    dataStateCopy.splice(id, 1);
                                    setDataState(dataStateCopy);
                                }}>-</Button>
                            </Col>
                        </Row>
                    </>
                )
            })}

            <Row justify={'space-between'} gutter={[0, 8]}>
                <Col span={24}>
                    <Button block onClick={() => {
                        dataStateCopy.push({
                            startTag: `#startTag-${uniqueRowCounter}`,
                            scenario: {
                                name: `#scenario-${uniqueRowCounter}`,
                                steps: [
                                    {name: 'temp1', type: 'given'},
                                    {name: 'temp2', type: 'when'},
                                    {name: 'temp3', type: 'when'},
                                    {name: 'temp4', type: 'then'},
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
            <Row>
                <ColorPicker width={456} height={228} color={color} onChange={setColor} hideHSV/>
            </Row>
            <Drawer visible={drawerVisible} width={720} onClose={() => {
                setDrawerVisible(false)
            }}>
                <div>
                {
                    types.map((currentType) => {
                        return(
                        dataState[editingScenarioId]?.scenario.steps.filter((step) => step.type === currentType)
                            .map((step, id) => {
                                return (<Input addonBefore={id === 0 ? step.type : 'and'} value={step.name}/>);
                            })
                        )
                    })
                }
                </div>
            </Drawer>
        </div>
    )
}

export default ScenarioInput;