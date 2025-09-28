from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        self.page = page

        self.title = self.page.get_by_test_id("create-course-toolbar-title-text")
        self.button = self.page.get_by_test_id(
            "create-course-toolbar-create-course-button"
        )

    def check_visible(self, is_create_course_disabled: bool):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text("Create course")
        if is_create_course_disabled:
            expect(self.button).to_be_visible()
            expect(self.button).to_be_enabled()
        else:
            expect(self.button).to_be_visible()
            expect(self.button).to_be_disabled()

    def click_button(self):
        self.button.click()
