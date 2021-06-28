export function convertTaggedScenariosToEsgSegments(taggedScenarios) {
    let count = 0;
    return taggedScenarios.map(taggedScenario => {
        const startTag = {label: taggedScenario.startTag, id: count++, isTag: true};
        const gherkinBody = {label: taggedScenario.scenario, id: count++};
        const endTag = {label: taggedScenario.endTag, id: count++, isTag: true};
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
        debugger;
        if (matchingTag) {
            debugger;
            // tag has a match
            // move current tags postfix to matched tag
            matchingTag.next = matchingTag.next.concat(taggedEsgSegment.next);
            taggedEsgSegment.next = [];
            // if exists, point current tag's parent to matched tag instead
            if(previousNode){
                debugger;
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
