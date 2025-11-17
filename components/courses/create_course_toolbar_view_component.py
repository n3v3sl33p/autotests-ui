import allure
from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        self.page = page

        self.title = Text(page, "create-course-toolbar-title-text", "Create course")
        self.button = Button(page, "create-course-toolbar-create-course-button", "Create course")

    @allure.step('Checking that "Create course toolbar view" is visible')
    def check_visible(self, is_create_course_disabled: bool):
        self.title.check_visible()
        self.title.check_have_text("Create course")

        if is_create_course_disabled:
            self.button.check_visible()
            self.button.check_enabled()
        else:
            self.button.check_visible()
            self.button.check_disabled()

    def click_button(self):
        self.button.click()
