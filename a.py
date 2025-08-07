from playwright.sync_api import expect, sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
    )

    login_email_input = page.get_by_test_id("login-form-email-input").locator("input")
    login_password_input = page.get_by_test_id("login-form-password-input").locator(
        "input"
    )
    login_button = page.get_by_test_id("login-page-login-button")
    expect(login_email_input).to_be_visible()
    expect(login_password_input).to_be_visible()
    expect(login_button).to_be_visible()

    registration_link = page.get_by_test_id("login-page-registration-link")
    registration_link.click()
    registration_email_input = page.get_by_test_id(
        "registration-form-email-input"
    ).locator("input")
    registration_password_input = page.get_by_test_id(
        "registration-form-password-input"
    ).locator("input")
    registration_button = page.get_by_test_id("registration-page-registration-button")

    expect(registration_email_input).to_be_visible()

    expect(registration_password_input).to_be_visible()

    expect(registration_button).to_be_visible()
