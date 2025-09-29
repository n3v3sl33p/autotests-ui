from playwright.sync_api import Page, expect
from components.courses.create_course_exercise_form_component import (
    CreateCourseExerciseFormComponent,
)
from components.courses.create_course_exercises_toolbar_component import (
    CreateCourseExercisesToolbarComponent,
)
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import (
    CreateCourseToolbarViewComponent,
)
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercise_empty_view = EmptyViewComponent(page, "create-course-exercises")
        self.image_upload_widget = ImageUploadWidgetComponent(
            page, "create-course-preview"
        )

        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

        self.navbar = NavbarComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.exercises_toolbar = CreateCourseExercisesToolbarComponent(page)
        self.course_toolbar = CreateCourseToolbarViewComponent(page)

    def check_visible_exercises_empty_view(self):
        self.exercise_empty_view.check_visible(
            "There is no exercises",
            'Click on "Create exercise" button to create new exercise',
        )
