from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        self.page = page

        self.create_exercise_title = Text(
            page, "create-course-exercises-box-toolbar-title-text", "Exercises"
        )
        self.create_exercise_button = Button(
            page,
            "create-course-exercises-box-toolbar-create-exercise-button",
            "Create exercise",
        )
        

    def check_visible(self):
        self.create_exercise_title.check_visible()
        self.create_exercise_title.check_have_text("Exercises")
        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()
