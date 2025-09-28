from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, component_name: str) -> None:
        super().__init__(page)
        self.component_name = component_name

        self.image_empty_view = EmptyViewComponent(page, "create-course-preview")

        self.preview_image = page.get_by_test_id(
            f"{component_name}-image-upload-widget-preview-image"
        )

        self.image_upload_info_icon = page.get_by_test_id(
            f"{component_name}-image-upload-widget-info-icon"
        )
        self.image_upload_info_title = page.get_by_test_id(
            f"{component_name}-image-upload-widget-info-title-text"
        )
        self.image_upload_info_description = page.get_by_test_id(
            f"{component_name}-image-upload-widget-info-description-text"
        )

        self.upload_button = page.get_by_test_id(
            f"{component_name}-image-upload-widget-upload-button"
        ).locator("input")
        self.remove_button = page.get_by_test_id(
            f"{component_name}-image-upload-widget-remove-button"
        )
        self.upload_input = page.get_by_test_id(
            f"{component_name}-image-upload-widget-input"
        )

    def check_visible(self, is_image_uploaded: bool):
        expect(self.image_upload_info_icon).to_be_visible()

        expect(self.image_upload_info_title).to_be_visible()
        expect(self.image_upload_info_title).to_have_text(
            'Tap on "Upload image" button to select file'
        )

        expect(self.image_upload_info_description).to_be_visible()
        expect(self.image_upload_info_description).to_have_text(
            "Recommended file size 540X300"
        )

        expect(self.upload_button).to_be_visible()

        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            expect(self.remove_button).to_be_visible()
            expect(self.preview_image).to_be_visible()

        if not is_image_uploaded:
            # Если картинка не загружена, проверяем наличие компонента EmptyViewComponent
            self.image_empty_view.check_visible(
                title="No image selected",
                description="Preview of selected image will be displayed here",
            )

    def click_remove(self):
        self.remove_button.click()

    def click_upload(self, file: str):
        self.upload_button.set_input_files(file)
