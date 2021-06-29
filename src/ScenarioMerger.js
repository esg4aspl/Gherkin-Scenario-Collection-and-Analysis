export function convertTaggedScenariosToEsgSegments(taggedScenarios) {
    let count = 0;
    return taggedScenarios.map(taggedScenario => {
        const startTag = {label: taggedScenario.startTag, id: count++, isTag: true, type: 'tag'};
        let prev = null;
        const scenarioNodes = [];
        taggedScenario.scenario.steps.forEach(item => {
            const current = {label: item.name, id: count++, type: item.type, next:[]};
            scenarioNodes.push(current);
            prev?.next.push(current);
            prev = current;
        });
        const gherkinBody = {label: taggedScenario.scenario.name, id: count++, scenario: {nodes: scenarioNodes[0], lastNode:prev}, type:'scenario'};
        const endTag = {label: taggedScenario.endTag, id: count++, isTag: true, type: 'tag'};
        startTag.next = [gherkinBody];
        gherkinBody.next = [endTag];
        endTag.next = [];
        return startTag;
    })
}

export function mergeTags(taggedEsgSegments) {
    const existingTags = {};
    taggedEsgSegments.forEach(taggedEsgSegment => {
        mergeTagsHelper(taggedEsgSegment, existingTags, null);
    });
    // removed orphaned tags
    return taggedEsgSegments.filter(esgSegment => !(esgSegment.isTag && esgSegment.next.length === 0));
}

function mergeTagsHelper(taggedEsgSegment, existingTags, previousNode) {
    // save next nodes to use for depth traversal, they may get modified
    const nextNodes = taggedEsgSegment.next;
    if (taggedEsgSegment.isTag) {
        const matchingTag = existingTags[taggedEsgSegment.label];
        if (matchingTag) {
            // tag has a match
            // move current tags postfix to matched tag
            matchingTag.next = matchingTag.next.concat(taggedEsgSegment.next);
            taggedEsgSegment.next = [];
            // if exists, point current tag's parent to matched tag instead
            if (previousNode) {
                previousNode.next = previousNode.next.filter(node => node.id !== taggedEsgSegment.id).concat(matchingTag);
            }
        } else {
            existingTags[taggedEsgSegment.label] = taggedEsgSegment;
        }
    }
    if (nextNodes) {
        nextNodes?.forEach(nextSegment => mergeTagsHelper(nextSegment, existingTags, taggedEsgSegment));
    }
}

export function expandScenarios(mergedEsgs) {
    mergedEsgs.forEach(esgSegment => expandScenarioHelper(esgSegment, null, {}));
    return mergedEsgs;
}

function expandScenarioHelper(esgSegment, prevNode, visitedNodes) {
    if(visitedNodes[esgSegment.id]){
        return;
    }
    visitedNodes[esgSegment.id] = true;
    if (esgSegment.scenario) {
        // insert the scenario between current node and its descendants
        prevNode.next = prevNode.next.filter(node => node.id !== esgSegment.id).concat([esgSegment.scenario.nodes]);
        esgSegment.scenario.lastNode.next = esgSegment.next;
    }
    esgSegment?.next.forEach(nextSegment => expandScenarioHelper(nextSegment, esgSegment, visitedNodes));
}
