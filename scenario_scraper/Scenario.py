from StepGroup import StepGroup


class Scenario:

    def __init__(self):
        self.scenario_name = ''
        self.feature_name = ''
        self.file_name = ''
        self.step_groups = {'Given': StepGroup('Given'), 'When': StepGroup('When'), 'Then': StepGroup('Then')}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self) -> str:
        return self.__str__()

