import time
import pytest


from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
import allure
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail", "  "),
            ("  ", "password"),
        ],
    )
    @allure.title("User login with wrong email or password")
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title("User login with correct email and password")
    def test_successful_authorization(
        self, registration_page: RegistrationPage, dashboard_page: DashboardPage, login_page: LoginPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.form.fill("aboba@mail.com", "artem", "123")
        registration_page.registration_button.click()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible("artem")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.logout.click()

        login_page.form.fill("aboba@mail.com", "123")
        login_page.click_login_button()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible("artem")
        dashboard_page.sidebar.check_visible()

    @allure.title("Navigation from login page to registration page")
    def test_navigate_from_authorization_to_registration(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()
        registration_page.form.check_visible("", "", "")

def test_firefox_simple(playwright):
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    
    print("Navigating to page...")
    page.goto("https://playwright.dev/", timeout=60000)
    print("Page loaded!")
    
    assert page.title() != ""
    
    browser.close()

