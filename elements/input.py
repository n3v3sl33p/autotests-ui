import allure
from elements.base_element import BaseElement, expect
from tools.logger import get_logger

logger = get_logger("INPUT")


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator("input")

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
