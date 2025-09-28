from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, component_name: str) -> None:
        super().__init__(page)

        self.component_name = component_name

        self.icon = page.get_by_test_id(f"{component_name}-empty-view-icon")
        self.title = page.get_by_test_id(f"{component_name}-empty-view-title-text")
        self.description = page.get_by_test_id(
            f"{component_name}-empty-view-description-text"
        )

    def check_visible(self, title: str, description: str):
        expect(self.icon).to_be_visible()
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.description).to_be_visible()
        expect(self.description).to_have_text(description)
