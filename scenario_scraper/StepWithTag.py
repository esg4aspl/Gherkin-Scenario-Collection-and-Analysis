
class StepWithTag:

    def __init__(self, text, connector_keyword):
        split_text = text.split('#')
        if len(split_text) == 1:
            self.text = text
            self.tag = None
        else:
            last_element_index = len(split_text) - 1
            self.text = '#'.join(split_text[:last_element_index])
            self.tag = split_text[last_element_index].strip()

        self.connector_keyword = connector_keyword

    def get_step_as_text(self):
        return self.connector_keyword + ' ' + self.text
