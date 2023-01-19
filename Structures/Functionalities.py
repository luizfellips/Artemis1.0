from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class DriverFunctions:
    def get_contacts(self, contact):
        search_field = self.driver.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
        search_field[0].click()
        search_field[0].send_keys(contact)
        search_field[0].send_keys(Keys.ENTER)

    def send_message(self,file_name,product_description):
        self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
        attach_image = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        sleep(1)
        attach_image.send_keys(file_name)
        sleep(1)
        description_field = self.driver.find_element(By.XPATH, '//p[contains(@class,"selectable-text copyable-text")]')
        description_field.click()
        description_field.send_keys(product_description)
        sleep(0.5)
        send_button = self.driver.find_element(By.CSS_SELECTOR, "span[data-icon='send']")
        send_button.click()
        