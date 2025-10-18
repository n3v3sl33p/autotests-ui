import time
import pytest


from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail", "  "),
            ("  ", "password"),
        ],
    )
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    def test_successful_authorization(
        self, registration_page: RegistrationPage, dashboard_page: DashboardPage, login_page: LoginPage
    ):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_page.form.fill("aboba@mail.com", "artem", "123")
        registration_page.click_registration_button()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible("artem")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.logout.click()

        login_page.form.fill("aboba@mail.com", "123")
        login_page.click_login_button()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible("artem")
        dashboard_page.sidebar.check_visible()

    def test_navigate_from_authorization_to_registration(
        self, login_page: LoginPage, registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()
        registration_page.form.check_visible("", "", "")
