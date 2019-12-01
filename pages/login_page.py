from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators, LinkUrl
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        time.sleep(1)
        url = self.browser.current_url
        time.sleep(1)
        assert "login" in url, 'Login URL is not matching'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "There is no register form"

class LoginPageLocators():
    LOGIN_FORM = (By .CSS_SELECTOR, "[name='login-username']")

    REGISTRATION_FORM = (By .CSS_SELECTOR, "[name = 'registration-email']")
