from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self.page = page
        self.locator = locator
        self.name = name

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)

        return self.page.get_by_test_id(locator)

    def click(self, **kwargs):
        self.get_locator(**kwargs).click()

    def check_visible(self, **kwargs):
        expect(self.get_locator(**kwargs)).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        expect(self.get_locator(**kwargs)).to_have_text(text)
