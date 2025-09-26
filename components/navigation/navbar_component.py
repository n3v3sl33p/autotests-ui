from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title = page.get_by_test_id("navigation-navbar-app-title-text")
        self.welcome_text = page.get_by_test_id("navigation-navbar-welcome-title-text")

    def check_visible(self, name: str):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("UI Course")
        expect(self.welcome_text).to_be_visible()
        expect(self.welcome_text).to_have_text(f"Welcome, {name}!")
