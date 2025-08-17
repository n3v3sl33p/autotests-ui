import pytest
from playwright.sync_api import expect, sync_playwright
from playwright.sync_api._generated import Page


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    courses_title = chromium_page_with_state.get_by_test_id(
        "courses-list-toolbar-title-text"
    )
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    results_title = chromium_page_with_state.get_by_test_id(
        "courses-list-empty-view-title-text"
    )
    expect(results_title).to_be_visible()
    expect(results_title).to_have_text("There is no results")
