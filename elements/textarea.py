from playwright.sync_api import Locator, expect
from elements.base_element import BaseElement


class Textarea(BaseElement):
    def get_locator(self, **kwargs) -> Locator:
        return super().get_locator(**kwargs).locator("textarea").first

    def fill(self, value: str, **kwargs):
        self.get_locator(**kwargs).fill(value)

    def check_have_value(self, value: str, **kwargs):
        expect(self.get_locator(**kwargs)).to_have_value(value)
