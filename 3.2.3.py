from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestInputs(unittest.TestCase):

    def test_1(self, link):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("a")
            browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("a")
            browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("a")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(10)
            browser.quit()

    def test_2(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("a")
            browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("a")
            browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("a")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        finally:
            time.sleep(10)
            browser.quit()


if __name__ == "__main__":
    unittest.main()

