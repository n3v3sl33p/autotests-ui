from typing import Literal
from abc import ABC, abstractmethod

from playwright.sync_api import Page, Locator, expect
import allure


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page: Page = page
        self.locator: str = locator
        self.name: str = name

    @property
    @abstractmethod
    def type_of(self) -> str: ...

    def get_locator(self, nth: int = 0, **kwargs: str) -> Locator:
        locator = self.locator.format(**kwargs)
        with allure.step(f'Getting locator with "data-testid={locator}" at index "{nth}"'):
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs: str):
        with allure.step(f'Clicking {self.type_of} "{self.name}"'):
            self.get_locator(nth, **kwargs).click()

    def check_visible(self, nth: int = 0, **kwargs: str):
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            expect(self.get_locator(nth, **kwargs)).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs: str):
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{text}"'):
            expect(self.get_locator(nth, **kwargs)).to_have_text(text)
