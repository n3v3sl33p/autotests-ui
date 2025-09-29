from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title = Text(page, "navigation-navbar-app-title-text", "App title")
        self.welcome_text = Text(
            page, "navigation-navbar-welcome-title-text", "Welcome text"
        )

    def check_visible(self, name: str):
        self.title.check_visible()
        self.title.check_have_text("UI Course")

        self.welcome_text.check_visible()
        self.welcome_text.check_have_text(f"Welcome, {name}!")
