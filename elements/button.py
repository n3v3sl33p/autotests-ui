from typing import Literal


from playwright.sync_api import expect

from elements.base_element import BaseElement
import allure


class Button(BaseElement):

    @property
    def type_of(self) -> Literal["button"]:
        return "button"

    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is disabled'):
            expect(self.get_locator(nth, **kwargs)).to_be_disabled()

    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is enabled'):
            expect(self.get_locator(nth, **kwargs)).to_be_enabled()
