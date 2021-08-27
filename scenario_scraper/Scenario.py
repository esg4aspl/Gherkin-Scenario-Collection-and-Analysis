class Scenario:

    def __init__(self):
        self.scenario_name = ''
        self.feature_name = ''
        self.file_name = ''
        self.steps = {'Given': [], 'When': [], 'Then': []}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()

    def get_step_as_text(self, step_name):
        step = self.steps[step_name]
        text = ''
        for statement in step:
            text += statement['keyword'] + ' ' + statement['text']
        return text
