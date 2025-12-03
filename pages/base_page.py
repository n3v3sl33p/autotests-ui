from re import Pattern
from playwright.sync_api import Page, expect
import allure

from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Open the url: {url}")
    def visit(self, url: str):
        logger.info(f"Open the url: {url}")
        self.page.goto(url, wait_until="networkidle")

    @allure.step("Reload current page")
    def reload(self):
        logger.info("Reload current page")
        self.page.reload(wait_until="networkidle")

    @allure.step("Check current url")
    def check_current_url(self, expected_url: Pattern[str]):
        logger.info("Check current url")
        expect(self.page).to_have_url(expected_url)
