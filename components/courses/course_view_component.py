from components.base_component import BaseComponent
from playwright.sync_api import Page

from components.courses.course_view_menu_component import CourseViewMenuComponent
from elements.image import Image
from elements.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = Text(page, "course-widget-title-text", "Title")
        self.image = Image(page, "course-preview-image", "Preview")
        self.max_score = Text(page, "course-max-score-info-row-view-text", "Max score")
        self.min_score = Text(page, "course-min-score-info-row-view-text", "Min score")
        self.estimated_time = Text(
            page, "course-estimated-time-info-row-view-text", "Estimated time"
        )

    def check_visible(
        self,
        index: int,
        title: str,
        max_score: str,
        min_score: str,
        estimated_time: str,
    ):
        self.image.check_visible(index)

        self.title.check_visible(index)
        self.title.check_have_text(title, index)

        self.max_score.check_visible(index)
        self.max_score.check_have_text(f"Max score: {max_score}", index)

        self.min_score.check_visible(index)
        self.min_score.check_have_text(f"Min score: {min_score}", index)

        self.estimated_time.check_visible(index)
        self.estimated_time.check_have_text(f"Estimated time: {estimated_time}", index)
