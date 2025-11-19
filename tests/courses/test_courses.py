import re
from config import settings
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
import pytest
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty course list")
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(AppRoute.COURSES)
        courses_list_page.navbar.check_visible(settings.test_user.username)
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar.check_visible()

        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(AppRoute.CREATE_COURSES)
        create_course_page.course_toolbar.check_visible(is_create_course_disabled=False)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title="", description="", estimated_time="", max_score="0", min_score="0"
        )
        create_course_page.exercises_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.click_upload(settings.test_data.image_png_file)
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
        create_course_page.visit(AppRoute.CREATE_COURSES)
        create_course_page.create_course_form.fill("test1", "1h", "test_description", "100", "10")
        create_course_page.image_upload_widget.click_upload(settings.test_data.image_png_file)
        create_course_page.course_toolbar.button.click()

        courses_list_page.check_current_url(re.compile(".*/#/courses"))
        courses_list_page.course_view.check_visible(0, "test1", "100", "10", "1h")
        courses_list_page.course_view.menu.menu_button.click()
        courses_list_page.course_view.menu.edit_menu_button.click()
        create_course_page.create_course_form.fill("new_title", "2h", "new_description", "200", "20")
        create_course_page.course_toolbar.button.click()
        courses_list_page.course_view.check_visible(0, "new_title", "200", "20", "2h")
