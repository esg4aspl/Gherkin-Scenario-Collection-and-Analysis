import {Button, Col, Container, Input, Row} from 'reactstrap';
import {useState} from "react";

function ScenarioInput(props) {

    const [dataState, setDataState] = useState([]);

    const dataStateCopy = [...dataState];
    return (
        <Container>
            <Row><Col xs={1}>id</Col><Col>startTag</Col><Col>Scenario</Col><Col>endTag</Col><Col xs={1}/></Row>
            {dataStateCopy.map((row, id) => {
                return (
                    <Row key={id} className='mb-2' >
                        <Col xs={1}>{id}</Col>
                        <Col>
                            <Input onChange={event => {
                                dataStateCopy[id].startTag = event.target.value;
                                setDataState(dataStateCopy)
                            }} value={row.startTag}/>
                        </Col>
                        <Col>
                            <Input onChange={event => {
                                dataStateCopy[id].scenario = event.target.value;
                                setDataState(dataStateCopy)
                            }} value={row.scenario}/>
                        </Col>
                        <Col>
                            <Input onChange={event => {
                                dataStateCopy[id].endTag = event.target.value;
                                setDataState(dataStateCopy)
                            }} value={row.endTag}/>
                        </Col>
                        <Col xs={1}>
                            <Button onClick={()=>{
                                dataStateCopy.splice(id, 1);
                                setDataState(dataStateCopy);
                            }}>-</Button>
                        </Col>
                    </Row>
                )
            })}

            <Button block onClick={() => {
                dataStateCopy.push({});
                setDataState(dataStateCopy);
            }}>Add Row</Button>
            <Button block onClick={() => {
               props.handleDrawClick(dataState);
            }}>Draw</Button>
        </Container>
    )
}

export default ScenarioInput;