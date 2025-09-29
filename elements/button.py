from elements.base_element import BaseElement
from playwright.sync_api import expect


class Button(BaseElement):
    def check_disabled(self, **kwargs):
        expect(self.get_locator(**kwargs)).to_be_disabled()

    def check_enabled(self, **kwargs):
        expect(self.get_locator(**kwargs)).to_be_enabled()
