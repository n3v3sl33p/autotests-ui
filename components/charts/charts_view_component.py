from enum import Enum
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartTypes(Enum):
    BAR = "bar"
    LINE = "line"
    PIE = "pie"
    SCATTER = "scatter"

    def __str__(self) -> str:
        return self.value


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, component_name: str, chart_type: ChartTypes) -> None:
        super().__init__(page)
        self.component_name = component_name
        self.chart_type = chart_type

        self.title = Text(page, f"{component_name}-widget-title-text", "Title")
        self.chart = Image(page, f"{component_name}-{chart_type}-chart", "Chart")

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text(self.component_name.capitalize())
        self.chart.check_visible()
