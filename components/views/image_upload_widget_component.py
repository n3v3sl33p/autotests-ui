from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, component_name: str) -> None:
        super().__init__(page)
        self.component_name:str = component_name

        self.image_empty_view: EmptyViewComponent = EmptyViewComponent(page, "create-course-preview")

        self.preview_image = Image(
            page, f"{component_name}-image-upload-widget-preview-image", "Preview"
        )

        self.image_upload_info_icon = Icon(
            page, f"{component_name}-image-upload-widget-info-icon", "Image upload info"
        )

        self.image_upload_info_title = Text(
            page,
            f"{component_name}-image-upload-widget-info-title-text",
            "Image upload info",
        )
        self.image_upload_info_description = Text(
            page,
            f"{component_name}-image-upload-widget-info-description-text",
            "Image upload info",
        )

        self.upload_button = Button(
            page, f"{component_name}-image-upload-widget-upload-button", "Upload"
        )
        self.remove_button = Button(
            page, f"{component_name}-image-upload-widget-remove-button", "Remove"
        )
        self.upload_input = FileInput(
            page, f"{component_name}-image-upload-widget-input", "Upload"
        )

    def check_visible(self, is_image_uploaded: bool):
        self.image_upload_info_icon.check_visible()
        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(
            'Tap on "Upload image" button to select file'
        )

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text(
            "Recommended file size 540X300"
        )

        self.upload_button.check_visible()

        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            self.remove_button.check_visible()
            self.preview_image.check_visible()

        if not is_image_uploaded:
            # Если картинка не загружена, проверяем наличие компонента EmptyViewComponent
            self.image_empty_view.check_visible(
                title="No image selected",
                description="Preview of selected image will be displayed here",
            )

    def click_remove(self):
        self.remove_button.click()

    def click_upload(self, file: str):
        self.upload_input.set_input_files(file)
