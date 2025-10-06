from elements.base_element import BaseElement, expect


class Input(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator("input")

    def fill(self, value: str, nth: int = 0, **kwargs):
        self.get_locator(nth, **kwargs).fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        expect(self.get_locator(nth, **kwargs)).to_have_value(value)
