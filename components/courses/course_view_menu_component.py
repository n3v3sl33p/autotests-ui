from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.button import Button


class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.menu_button = Button(page, "course-view-menu-button", "Menu")
        self.edit_menu_button = Button(page, "course-view-edit-menu-item", "Edit")
        self.delete_menu_button = Button(page, "course-view-delete-menu-item", "Delete")

    def click_edit(self, index: int):
        self.menu_button.click(index)
        self.edit_menu_button.check_visible(index)
        self.edit_menu_button.click(index)

    def click_delete(self, index: int):
        self.menu_button.click(index)
        self.delete_menu_button.check_visible(index)
        self.delete_menu_button.click(index)
