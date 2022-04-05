from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    DEPARTMENT = (By.CSS_SELECTOR, "#nav-subnav[data-category='{DEPARTMENT_CATEGORY}']")

    def _get_department_locator(self, department: str):
        return[self.DEPARTMENT[0], self.DEPARTMENT[1].replace('{DEPARTMENT_CATEGORY}', department)]

    def verify_correct_department(self, department):
        department_locator = self._get_department_locator(department)
        self.wait_for_element_appear(*department_locator)
