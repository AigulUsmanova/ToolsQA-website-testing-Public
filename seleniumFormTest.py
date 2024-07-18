from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time


class InputForm:
    URL = "https://www.selenium.dev/selenium/web/inputs.html"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self):
        faker = Faker()
        first_name = faker.first_name()
        range_value = str(faker.random_int(min=0, max=100))
        number = faker.random_number(digits=3)
        email = faker.email()
        password = faker.password()
        phone = faker.phone_number()
        address = faker.random_number(digits=5)
        last_name = faker.last_name()
        url = faker.url()
        color = "#" + ''.join([faker.random_letter() for _ in range(6)])

        send_keys_names = [first_name, range_value, number, email, password, phone, address, last_name, url]
        element_names = ["no_type", "number_input", "range_input", "email_input", "password_input", "search_input", "tel_input", "text_input", "url_input"]

        for i in range(len(element_names)):
            self.driver.find_element(By.NAME, element_names[i]).clear()
            time.sleep(0.2)
            self.driver.find_element(By.NAME, element_names[i]).send_keys(send_keys_names[i])

        self.driver.find_element(By.NAME, "checkbox_input").click()
        elements = self.driver.find_elements(By.NAME, "radio_input")
        if elements:
            elements[-1].click()
        self.driver.find_element(By.NAME, "color_input").click()
        self.driver.find_element(By.NAME, "color_input").clear()
        self.driver.find_element(By.NAME, "color_input").send_keys(color)
        time.sleep(0.2)
        self.driver.find_element(By.NAME, "date_input").click()
        self.driver.find_element(By.NAME, "button_input").click()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    page = InputForm(driver)

    try:
        page.open()
        page.fill_form()
    finally:
        driver.quit()