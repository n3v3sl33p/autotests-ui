from re import Pattern
from playwright.sync_api import Page, expect
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open the url: {url}")
    def visit(self, url: str):
        self.page.goto(url, wait_until="networkidle")

    @allure.step("Reload current page")
    def reload(self):
        self.page.reload(wait_until="networkidle")

    @allure.step("Check current url")
    def check_current_url(self, expected_url: Pattern[str]):
        expect(self.page).to_have_url(expected_url)
