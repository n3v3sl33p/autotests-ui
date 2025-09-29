from elements.base_element import BaseElement, expect


class Input(BaseElement):
    def get_locator(self, **kwargs):
        locator = self.locator.format(**kwargs)

        return self.page.get_by_test_id(locator).locator("input")

    def fill(self, value: str, **kwargs):
        self.get_locator(**kwargs).fill(value)

    def check_have_value(self, value: str, **kwargs):
        expect(self.get_locator(**kwargs)).to_have_value(value)
