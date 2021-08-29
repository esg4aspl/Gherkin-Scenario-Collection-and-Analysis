class StepGroup:
    def __init__(self, keyword) -> None:
        self.steps = []
        self.keyword = keyword

    def get_steps_as_text(self):
        text = ''
        for step in self.steps:
            text += step.get_step_as_text() + ' '
        return text.strip()

    def append(self, step):
        self.steps.append(step)

    def does_match(self, rhs):
        own_tags = set()
        for step in self.steps:
            if step.tag is not None:
                own_tags.add(step.tag)

        for step in rhs.steps:
            if step.tag is not None and step.tag in own_tags:
                return True

        return False

