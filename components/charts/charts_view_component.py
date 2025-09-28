from enum import Enum
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class ChartTypes(Enum):
    BAR = "bar"
    LINE = "line"
    PIE = "pie"
    SCATTER = "scatter"


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, component_name: str, chart_type: ChartTypes) -> None:
        super().__init__(page)
        self.component_name = component_name
        self.chart_type = chart_type

        self.title = page.get_by_test_id(f"{component_name}-widget-title-text")
        self.chart = page.get_by_test_id(f"{component_name}-{chart_type}-chart")

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.component_name.capitalize())
        self.chart.is_visible()
