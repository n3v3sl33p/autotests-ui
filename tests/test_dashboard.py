import pytest

from pages.dashboard_page import DashboardPage


@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"
    )

    dashboard_page_with_state.navbar.check_visible("username")
    dashboard_page_with_state.sidebar.check_visible()

    dashboard_page_with_state.toolbar.check_visible()
    dashboard_page_with_state.scores_chart.check_visible()
    dashboard_page_with_state.courses_chart.check_visible()
    dashboard_page_with_state.students_chart.check_visible()
    dashboard_page_with_state.activities_chart.check_visible()
