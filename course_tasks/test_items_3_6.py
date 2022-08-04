from selenium.webdriver.common.by import By


class TestBtnAdd:
    def test_btn_add_to_basket_should_be_present(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(5)
        btn = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
        assert len(btn)
