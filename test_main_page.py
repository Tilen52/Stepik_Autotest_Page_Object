from .pages.main_page import MainPage
from .pages.locators import LinkUrl
from .pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, LinkUrl.LINK)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()