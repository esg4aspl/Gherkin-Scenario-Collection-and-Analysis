import {Button, Checkbox, Input} from "antd";
import {DeleteOutlined, EditOutlined} from "@ant-design/icons";

export function getInputColumns(onFieldUpdate, onScenarioClick, onRowDelete) {
    return (
        [
            {
                title: 'id',
                dataIndex: 'id',
                width: '5%',
            },
            {
                title: 'S?',
                dataIndex: 'isStartNode',
                width: '5%',
                render: (item, row, index) => {
                    return <Checkbox checked={item} onChange={(event) => {
                        onFieldUpdate(index, 'isStartNode', event.target.checked);
                    }
                    }/>
                }
            },
            {
                title: 'E?',
                dataIndex: 'isEndNode',
                width: '5%',
                render: (item, row, index) => {
                    return <Checkbox checked={item} onChange={(event) => {
                        onFieldUpdate(index, 'isEndNode', event.target.checked);
                    }
                    }/>
                }
            },
            {
                title: 'startTag',
                dataIndex: 'startTag',
                width: '15%',
                render: (item, record, index) => {
                    return (
                        <Input disabled={record.isStartNode} onChange={event => {
                            onFieldUpdate(index, 'startTag', event.target.value);
                        }} value={item}/>
                    )
                }
            },
            {
                title: 'scenario',
                dataIndex: ['scenario', 'name'],
                width: '15%',
                render: (item, record, index) => {
                    return (
                        <Button block onClick={() => {
                            onScenarioClick(index);
                        }}><EditOutlined/> {item}</Button>
                    );
                }
            },
            {
                title: 'endTag',
                dataIndex: 'endTag',
                width: '15%',
                render: (item, record, index) => {
                    return (
                        <Input disabled={record.isEndNode} onChange={event => {
                            onFieldUpdate(index, 'endTag', event.target.value);
                        }} value={item}/>
                    )
                }
            },
            {
                title: 'delete',
                width: '5%',
                render: (item, record, index) => {
                    return (
                        <Button onClick={() => {
                            onRowDelete(index);
                        }}>
                            <DeleteOutlined className={'center'}/>
                        </Button>
                    )
                }
            },
        ]);
}