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
        mergeTagsHelper(taggedEsgSegment, existingTags);
    });
    debugger;
}

function mergeTagsHelper(taggedEsgSegment, existingTags) {
    if (taggedEsgSegment.isTag) {
        const matchingTag = existingTags[taggedEsgSegment.label]
        if (matchingTag) {
            // tag has a match
            matchingTag.next = matchingTag.next.concat(taggedEsgSegment.next);
            taggedEsgSegment.next = [];
        } else {
            existingTags[taggedEsgSegment.label] = taggedEsgSegment;
        }
    }
    if (taggedEsgSegment.next) {
        taggedEsgSegment.next?.forEach(nextSegment => mergeTagsHelper(nextSegment, existingTags));
    }
}
