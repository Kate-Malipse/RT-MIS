from src.base.Base import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    locator_dictionary = {
        "demo_mode_header": (By.CLASS_NAME, "demo"),
        "demo_mode_on_button": (By.CSS_SELECTOR, "a[href='/user/demo_login'"),
        "user_profile": (By.CSS_SELECTOR, "a[href= '/user/profile']"),
    }

    def to_demo_page(self):
        demo_mode_header = self.find_element(
            self.locator_dictionary['demo_mode_header'])
        demo_mode_on_button = self.find_element(
            self.locator_dictionary['demo_mode_on_button'])

        ActionChains(self.driver).move_to_element(
            demo_mode_header).click(demo_mode_on_button).perform()

    def get_profile_element(self):
        return self.find_element(self.locator_dictionary['user_profile'])


class DemoPage(BasePage):

    locator_dictionary = {
        "services_list": (By.CLASS_NAME, "more"),
        "service_record": (By.CSS_SELECTOR, "a[href='/service/record']"),
        "error_message": (By.CSS_SELECTOR, "div.http_error > h1"),
        "disable_demo_mode_button": (By.CSS_SELECTOR, "div.cap > div.wrapper > div.person > p > a.exit")
    }

    def register_to_doctor(self):
        services_list = self.find_element(
            self.locator_dictionary['services_list'])
        service_record = self.find_element(
            self.locator_dictionary['service_record'])

        ActionChains(self.driver).move_to_element(
            services_list).click(service_record).perform()

    def get_register_message(self):
        return self.find_element(self.locator_dictionary['error_message']).text

    def logout(self):
        self.find_element(
            self.locator_dictionary['disable_demo_mode_button']).click()
