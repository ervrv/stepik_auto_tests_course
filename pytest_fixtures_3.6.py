import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize(
    'link_part', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, link_part):
        link = f"https://stepik.org/lesson/{link_part}/step/1"
        browser.get(link)
        answer = math.log(int(time.time()))
        WebDriverWait(browser, 5)\
            .until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea"))).send_keys(answer)
        WebDriverWait(browser, 5)\
            .until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))).click()
        text = WebDriverWait(browser, 5)\
            .until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text

        assert text == "Correct!", "Not correct."
