from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page: Page = page
        self.locator: str = locator
        self.name: str = name

    def get_locator(self, nth: int = 0, **kwargs: str) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs:str):
        self.get_locator(nth, **kwargs).click()

    def check_visible(self, nth: int = 0, **kwargs: str):
        expect(self.get_locator(nth, **kwargs)).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs:str):
        expect(self.get_locator(nth, **kwargs)).to_have_text(text)
