from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        self.get_locator(nth, **kwargs).set_input_files(file)
