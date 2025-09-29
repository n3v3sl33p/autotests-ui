from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_input_files(self, file: str, **kwargs):
        self.get_locator(**kwargs).set_input_files(file)

    