from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создание
        self.create_course_title = self.page.get_by_test_id(
            "create-course-toolbar-title-text"
        )
        self.create_course_button = self.page.get_by_test_id(
            "create-course-toolbar-create-course-button"
        )

        # Пустой блок при отсутствии картинки курса
        self.empty_view_icon = self.page.get_by_test_id(
            "create-course-preview-empty-view-icon"
        )
        self.empty_view_title_text = self.page.get_by_test_id(
            "create-course-preview-empty-view-title-text"
        )
        self.empty_view_description_text = self.page.get_by_test_id(
            "create-course-preview-empty-view-description-text"
        )

        # Загрузка картинки курса
        self.upload_image_icon = self.page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-icon"
        )
        self.upload_image_title_text = self.page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-title-text"
        )
        self.upload_image_description_text = self.page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-description-text"
        )
        self.upload_image_button = self.page.get_by_test_id(
            "create-course-preview-image-upload-widget-upload-button"
        )
        self.upload_image_input = self.page.get_by_test_id(
            "create-course-preview-image-upload-widget-input"
        )
        self.remove_image_button = self.page.get_by_test_id(
            "create-course-preview-image-upload-widget-remove-button"
        )

        # Картинка курса
        self.course_image = self.page.get_by_test_id(
            "create-course-preview-image-upload-widget-preview-image"
        )

        # Форма создания курса
        self.course_title_input = self.page.get_by_test_id(
            "create-course-form-title-input"
        ).locator("input")
        self.course_estimated_time_input = self.page.get_by_test_id(
            "create-course-form-estimated-time-input"
        ).locator("input")
        self.course_description_input = (
            self.page.get_by_test_id("create-course-form-description-input")
            .locator("textarea")
            .first
        )
        self.course_max_score_input = self.page.get_by_test_id(
            "create-course-form-max-score-input"
        ).locator("input")
        self.course_min_score_input = self.page.get_by_test_id(
            "create-course-form-min-score-input"
        ).locator("input")

        # Заголовок и кнопка создание упражнения
        self.create_exercise_title = self.page.get_by_test_id(
            "create-course-exercises-box-toolbar-title-text"
        )
        self.create_exercise_button = self.page.get_by_test_id(
            "create-course-exercises-box-toolbar-create-exercise-button"
        )

        # Пустой блок при отсутствии упражнений
        self.exercise_empty_view_icon = self.page.get_by_test_id(
            "create-course-exercises-empty-view-icon"
        )
        self.exercise_empty_view_title_text = self.page.get_by_test_id(
            "create-course-exercises-empty-view-title-text"
        )
        self.exercise_empty_view_description_text = self.page.get_by_test_id(
            "create-course-exercises-empty-view-description-text"
        )

        # Заголовок упражнения и кнопка удаления
        self.exercise_title = self.page.get_by_test_id(
            "create-course-exercise-{}-box-toolbar-subtitle-text"
        )
        self.delete_exercise_button = self.page.get_by_test_id(
            "create-course-exercise-0-box-toolbar-delete-exercise-button"
        )

        self.exercise_title_input = self.page.get_by_test_id(
            "create-course-exercise-form-title-{}-input"
        )
        self.exercise_description_input = self.page.get_by_test_id(
            "create-course-exercise-form-description-{}-input"
        )

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text("Create course")

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_disabled_create_course_button(self):
        expect(self.create_course_button).to_be_disabled()

    def check_visible_image_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()
        expect(self.empty_view_title_text).to_be_visible()
        expect(self.empty_view_title_text).to_have_text("No image selected")
        expect(self.empty_view_description_text).to_be_visible()
        expect(self.empty_view_description_text).to_have_text(
            "Preview of selected image will be displayed here"
        )

    def check_visible_image_upload_view(self, is_image_uploaded: bool):
        expect(self.upload_image_icon).to_be_visible()
        expect(self.upload_image_title_text).to_be_visible()
        expect(self.upload_image_title_text).to_have_text(
            'Tap on "Upload image" button to select file'
        )
        expect(self.upload_image_description_text).to_be_visible()
        expect(self.upload_image_description_text).to_have_text(
            "Recommended file size 540X300"
        )

        expect(self.upload_image_button).to_be_visible()

        if is_image_uploaded:
            expect(self.remove_image_button).to_be_visible()

    def click_remove_image_button(self):
        self.remove_image_button.click()

    def check_visible_course_image(self):
        expect(self.course_image).to_be_visible()

    def upload_image(self, file_path: str):
        self.upload_image_input.set_input_files(file_path)

    def check_visible_exercises_title(self):
        expect(self.create_exercise_title).to_be_visible()
        expect(self.create_exercise_title).to_have_text("Exercises")

    def check_visible_create_course_form(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        expect(self.course_title_input).to_be_visible()
        expect(self.course_title_input).to_have_value(title)

        expect(self.course_estimated_time_input).to_be_visible()
        expect(self.course_estimated_time_input).to_have_value(estimated_time)

        expect(self.course_description_input).to_be_visible()
        expect(self.course_description_input).to_have_value(description)

        expect(self.course_max_score_input).to_be_visible()
        expect(self.course_max_score_input).to_have_value(max_score)

        expect(self.course_min_score_input).to_be_visible()
        expect(self.course_min_score_input).to_have_value(min_score)

    def fill_create_course_form(
        self,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str,
    ):
        self.course_title_input.fill(title)
        expect(self.course_title_input).to_have_value(title)

        self.course_estimated_time_input.fill(estimated_time)
        expect(self.course_estimated_time_input).to_have_value(estimated_time)

        self.course_description_input.fill(description)
        expect(self.course_description_input).to_have_value(description)

        self.course_max_score_input.fill(max_score)
        expect(self.course_max_score_input).to_have_value(max_score)

        self.course_min_score_input.fill(min_score)
        expect(self.course_min_score_input).to_have_value(min_score)

    def check_visible_create_exercise_button(self):
        expect(self.create_exercise_button).to_be_visible()

    def click_create_exercise_button(self):
        self.create_exercise_button.click()

    def check_visible_exercises_empty_view(self):
        expect(self.exercise_empty_view_icon).to_be_visible()
        expect(self.exercise_empty_view_title_text).to_be_visible()
        expect(self.exercise_empty_view_title_text).to_have_text(
            "There is no exercises"
        )
        expect(self.exercise_empty_view_description_text).to_be_visible()
        expect(self.exercise_empty_view_description_text).to_have_text(
            'Click on "Create exercise" button to create new exercise'
        )

    def click_delete_exercise_button(self, index: int):
        self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button"
        ).click()

    def check_visible_create_exercise_form(
        self, index: int, title: str, description: str
    ):
        expect(
            self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        ).to_be_visible()
        expect(
            self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        ).to_have_value(title)

        expect(
            self.page.get_by_test_id(
                f"create-course-exercise-form-description-{index}-input"
            )
        ).to_be_visible()
        expect(
            self.page.get_by_test_id(
                f"create-course-exercise-form-description-{index}-input"
            )
        ).to_have_value(description)

    def fill_create_exercise_form(self, index: int, title: str, description: str):
        self.page.get_by_test_id(
            f"create-course-exercise-form-title-{index}-input"
        ).fill(title)
        self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input"
        ).fill(description)
