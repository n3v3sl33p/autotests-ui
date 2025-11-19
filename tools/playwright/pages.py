from typing import Any, Generator


from playwright.sync_api._generated import Page
import allure

from playwright.sync_api import Playwright, Page
from pydantic import FilePath
from config import settings


def create_browser_page(
    playwright: Playwright, test_name: str, browser_state: FilePath | None = None
) -> Generator[Page, Any, None]:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.base_url, record_video_dir=settings.videos_dir, storage_state=browser_state
    )
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()
    yield page

    tracing_file_path = settings.tracing_dir.joinpath(f"{test_name}.zip")
    context.tracing.stop(path=tracing_file_path)
    allure.attach.file(source=tracing_file_path, name="trace", extension="zip")
    if page.video is not None:
        allure.attach.file(source=page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)
    browser.close()
