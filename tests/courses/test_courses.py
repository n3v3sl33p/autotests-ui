import re
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import pytest


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar.check_visible("username")
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar.check_visible()

        courses_list_page.check_visible_empty_view()

    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.course_toolbar.check_visible(is_create_course_disabled=False)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", description="", estimated_time="", max_score="0", min_score="0"
        )
        create_course_page.exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.click_upload("./testdata/files/image.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10",
        )
        create_course_page.course_toolbar.click_button()

        courses_list_page.toolbar.check_visible()

        courses_list_page.course_view.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks",
        )

    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_form.fill("test1", "1h", "test_description", "100", "10")
        create_course_page.image_upload_widget.click_upload("testdata/files/image.png")
        create_course_page.course_toolbar.button.click()

        courses_list_page.check_current_url(re.compile(".*/#/courses"))
        courses_list_page.course_view.check_visible(0, "test1", "100", "10", "1h")
        courses_list_page.course_view.menu.menu_button.click()
        courses_list_page.course_view.menu.edit_menu_button.click()
        create_course_page.create_course_form.fill("new_title", "2h", "new_description", "200", "20")
        create_course_page.course_toolbar.button.click()
        courses_list_page.course_view.check_visible(0, "new_title", "200", "20", "2h")
