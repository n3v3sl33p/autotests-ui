from playwright.sync_api import Locator, expect
from elements.base_element import BaseElement
from tools.logger import get_logger
import allure

logger = get_logger("TEXTAREA")


class Textarea(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator("textarea").first

    def fill(self, value: str, nth: int = 0, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        with allure.step(step):
            logger.info(step)
            self.get_locator(nth, **kwargs).fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        with allure.step(step):
            logger.info(step)
            expect(self.get_locator(nth, **kwargs)).to_have_value(value)
