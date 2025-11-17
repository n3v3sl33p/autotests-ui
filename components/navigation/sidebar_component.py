from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SidebarListItemComponent
import allure


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.dashboard = SidebarListItemComponent(page, "dashboard")
        self.courses = SidebarListItemComponent(page, "courses")
        self.logout = SidebarListItemComponent(page, "logout")

    @allure.step("Check visible sidebar")
    def check_visible(self):
        self.dashboard.check_visible()
        self.courses.check_visible()
        self.logout.check_visible()
