from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
import unittest
import time


class InputForm:
    def __init__(self, driver):
        self.driver = driver
        self.full_name_field = (By.ID, "userName")
        self.email_field = (By.ID, "userEmail")
        self.current_address_field = (By.ID, "currentAddress")
        self.permanent_address_field = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")

    def fill_form(self, full_name, email, current_address, permanent_address):
        # Вводим данные в форму
        self.driver.find_element(*self.full_name_field).send_keys(full_name)
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.current_address_field).send_keys(current_address)
        self.driver.find_element(*self.permanent_address_field).send_keys(permanent_address)
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.driver.find_element(By.XPATH, "//*[@id='submit']").click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "output"))
        )

    def data_checking(self, full_name, email, current_address, permanent_address):
        # Получаем данные из появившейся формы после нажатия на кнопку Submit
        element_names = ['']*4
        element_id = ["name", "email", "currentAddress", "permanentAddress"]
        for i in range(len(element_id)):
            elements = self.driver.find_elements(By.ID, element_id[i])
            if elements:
                element_names[i] = elements[-1].text

        # Сверяем данные
        print(element_names[0])
        print("Name:" + full_name + '\n')
        print(element_names[1])
        print("Email:" + email + '\n')
        print(element_names[2])
        print("Current Address :" + current_address + '\n')
        print(element_names[3])
        print("Permananet Address :" + permanent_address + '\n')
        if element_names[0] == ("Name:" + full_name) and element_names[1] == ("Email:" + email) and element_names[2] == ("Current Address :" + current_address) and element_names[3] == ("Permananet Address :" + permanent_address):
            print("Данные совпадают!")
        else:
            print("Данные не совпадают!")


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/text-box")

    def test(self):
        faker = Faker()
        full_name = faker.name()
        email = faker.email()
        current_address = faker.street_address()
        permanent_address = faker.street_address()

        input_form = InputForm(self.driver)
        input_form.fill_form(full_name, email, current_address, permanent_address)
        input_form.data_checking(full_name, email, current_address, permanent_address)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()





