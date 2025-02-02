from pages.amazon_main_page import MainPage
from pages.cart_page import CartPage
from pages.signin_page import SigninPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.amazon_main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.signin_page = SigninPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.product_page = ProductPage(self.driver)

