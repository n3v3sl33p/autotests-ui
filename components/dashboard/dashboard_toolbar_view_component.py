from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title = Text(page, "dashboard-toolbar-title-text", "App title")

    def check_visible(self):
        self.title.check_visible()
