import pytest
from playwright.sync_api import Page, expect


def test_webkit_browser(page: Page):
    """Простой тест для проверки работы WebKit браузера"""
    # Переход на страницу
    page.goto("https://playwright.dev/")

    # Проверка что страница загрузилась
    assert page.url == "https://playwright.dev/"
