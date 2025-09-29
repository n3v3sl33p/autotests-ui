from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.button import Button
from elements.icon import Icon
from elements.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, component_name: str) -> None:
        super().__init__(page)
        self.component_name = component_name

        self.icon = Icon(page, f"{component_name}-drawer-list-item-icon", "icon")
        self.text = Text(page, f"{component_name}-drawer-list-item-title-text", "text")
        self.button = Button(
            page, f"{component_name}-drawer-list-item-button", "button"
        )

    def check_visible(self):
        self.icon.check_visible()

        self.text.check_visible()
        self.text.check_have_text(self.component_name.capitalize())

        self.button.check_visible()

    def click(self):
        self.button.click()
