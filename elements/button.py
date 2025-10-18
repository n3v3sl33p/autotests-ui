from playwright.sync_api import expect

from elements.base_element import BaseElement


class Button(BaseElement):
    def check_disabled(self, nth: int = 0, **kwargs):
        expect(self.get_locator(nth, **kwargs)).to_be_disabled()

    def check_enabled(self, nth: int = 0, **kwargs):
        expect(self.get_locator(nth, **kwargs)).to_be_enabled()
