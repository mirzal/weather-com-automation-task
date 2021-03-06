from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.abstract.weather_page import WeatherPage
from pages.home_page import MainPage


class LoginPage(WeatherPage):
    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "loaded_form_indicator": (By.CSS_SELECTOR, '#loginSignUpForm[novalidate=true]'),
        "email_input": (By.CSS_SELECTOR, 'input[name=id]'),
        "password_input": (By.CSS_SELECTOR, 'input[name=token]'),
        "log_in_button": (By.CSS_SELECTOR, '#loginSignUpForm button[type=submit]'),
        "invalid_login_popup": (By.CSS_SELECTOR, '.validation-wrapper')
    })

    def login(self, user):
        # See comment in pages/create_account_page.py
        self.wait_for_presence_of_element(self.locator_dictionary["loaded_form_indicator"])
        self.find_element(self.locator_dictionary["email_input"]).send_keys(user.email)
        self.find_element(self.locator_dictionary["password_input"]).send_keys(user.password)
        self.find_element(self.locator_dictionary["log_in_button"]).click()

        try:
            self.wait_for_presence_of_element(self.locator_dictionary["invalid_login_popup"], 2)
            return self
        except TimeoutException:
            return MainPage()
