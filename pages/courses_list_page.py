from re import S
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_component import (
    CoursesListToolbarComponent,
)
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page


class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.empty_view = EmptyViewComponent(page, "courses-list")
        self.course_view = CourseViewComponent(page)
        self.toolbar = CoursesListToolbarComponent(page)

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            "There is no results",
            "Results from the load test pipeline will be displayed here",
        )
