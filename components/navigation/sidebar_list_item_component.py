from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, component_name: str) -> None:
        super().__init__(page)
        self.component_name = component_name
        self.icon = page.get_by_test_id(f"{component_name}-drawer-list-item-icon")
        self.text = page.get_by_test_id(f"{component_name}-drawer-list-item-title-text")
        self.button = page.get_by_test_id(f"{component_name}-drawer-list-item-button")

    def check_visible(self):
        expect(self.icon).to_be_visible()

        expect(self.text).to_be_visible()
        expect(self.text).to_have_text(self.component_name.capitalize())

        expect(self.button).to_be_visible()

    def click(self):
        self.button.click()
