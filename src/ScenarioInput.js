// import {Button, ButtonToggle, Input} from 'reactstrap';
import {useState} from "react";
import {Button, Checkbox, Col, Input, Row} from 'antd';
import 'antd/dist/antd.css'

function ScenarioInput(props) {

    const [dataState, setDataStateProtected] = useState([]);
    const setDataState = (dataState) => {
        setDataStateProtected(dataState);
        if (autoDrawEnabled) {
            props.handleDrawClick(dataState);
        }
    }

    const [autoDrawEnabled, setAutoDrawEnabled] = useState(false);

    const dataStateCopy = [...dataState];

    return (
        <div style={{marginLeft: '40px'}}>
            <Row justify={'space-between'} style={{width: '1000px'}}>
                <Col span={1}>id</Col>
                <Col span={6}>startTag</Col>
                <Col span={6}>Scenario</Col>
                <Col span={6}>endTag</Col>
                <Col span={1}/>
            </Row>
            {dataStateCopy.map((row, id) => {
                return (
                    <>
                        <Row justify={'space-between'} style={{width: '1000px'}} key={id}
                             className='mb-2'>
                            <Col span={1}>{id}</Col>
                            <Col span={6}>
                                <Input onChange={event => {
                                    dataStateCopy[id].startTag = event.target.value;
                                    setDataState(dataStateCopy)
                                }} value={row.startTag}/>
                            </Col>
                            <Col span={6}>
                                <Input onChange={event => {
                                    dataStateCopy[id].scenario = event.target.value;
                                    setDataState(dataStateCopy)
                                }} value={row.scenario}/>
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
            <Row justify={'space-between'} style={{width: '1000px'}} gutter={[0, 8]}>
                <Col span={24}>
                    <Button block onClick={() => {
                        dataStateCopy.push({});
                        setDataState(dataStateCopy);
                    }}>Add Row</Button>
                </Col>
                <Col span={3}>
                    <Checkbox
                        checked={autoDrawEnabled}
                        onClick={() => {
                            setAutoDrawEnabled(!autoDrawEnabled)
                        }}
                    >Autodraw</Checkbox>
                </Col>
                <Col span={21}>
                    <Button block onClick={() => {
                        props.handleDrawClick(dataState);
                    }}>Draw</Button>
                </Col>
            </Row>
        </div>
    )
}

export default ScenarioInput;