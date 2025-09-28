from components.charts.charts_view_component import ChartTypes, ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import (
    DashboardToolbarViewComponent,
)
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage
from playwright.sync_api import Page


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.toolbar = DashboardToolbarViewComponent(page)

        self.students_chart = ChartViewComponent(page, "students", ChartTypes.BAR)
        self.activities_chart = ChartViewComponent(page, "activities", ChartTypes.LINE)
        self.courses_chart = ChartViewComponent(page, "courses", ChartTypes.PIE)
        self.scores_chart = ChartViewComponent(page, "scores", ChartTypes.SCATTER)
