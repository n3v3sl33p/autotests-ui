from typing import Literal


from playwright.sync_api import expect

from elements.base_element import BaseElement
import allure

from tools.logger import get_logger

logger = get_logger("BUTTON")


class Button(BaseElement):
    @property
    def type_of(self) -> Literal["button"]:
        return "button"

    def check_disabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is disabled'
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_be_disabled()

    def check_enabled(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is enabled'
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_be_enabled()
