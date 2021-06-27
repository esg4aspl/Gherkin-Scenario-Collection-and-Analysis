function convertTaggedScenariosToEsgSegments(taggedScenarios) {
    let count = 0;
    return taggedScenarios.map(taggedScenario => {
        const startTag = {label: taggedScenario.startTag, id:count++};
        const gherkinBody = {label: taggedScenario.scenario, id:count++};
        const endTag = {label: taggedScenario.endTag, id:count++};
        startTag.next = [gherkinBody];
        gherkinBody.next = [endTag];
        return startTag;
    })
}

export default convertTaggedScenariosToEsgSegments;