from _pytest.fixtures import SubRequest
import pytest
from playwright.sync_api import Playwright
from config import settings

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import create_browser_page


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright):
    yield from create_browser_page(playwright=playwright, test_name=request.node.name)


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)

    context = browser.new_context(base_url=settings.base_url)
    page = context.new_page()
    registration_page = RegistrationPage(page)

    registration_page.visit("#/auth/registration")

    registration_page.form.fill(settings.test_user.email, settings.test_user.username, settings.test_user.password)

    registration_page.registration_button.click()

    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture
def chromium_page_with_state(request: SubRequest, playwright: Playwright, initialize_browser_state):
    yield from create_browser_page(
        playwright=playwright, test_name=request.node.name, browser_state=settings.browser_state_file
    )
