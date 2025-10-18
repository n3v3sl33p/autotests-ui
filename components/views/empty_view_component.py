from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, component_name: str) -> None:
        super().__init__(page)

        self.component_name: str = component_name

        self.icon: Icon = Icon(page, f"{component_name}-empty-view-icon", "icon")
        self.title: Text = Text(page, f"{component_name}-empty-view-title-text", "text")
        self.description: Text = Text(
            page, f"{component_name}-empty-view-description-text", "text"
        )

    def check_visible(self, title: str, description: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)
