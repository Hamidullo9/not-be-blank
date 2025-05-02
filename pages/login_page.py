from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.phone_number = (By.NAME, 'phone')
        self.button_submit = (By.CSS_SELECTOR, "button[type='submit']")
        self.password = (By.NAME, "password")

    def EnterPhoneNumber(self, phone_number):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((self.phone_number))).send_keys(phone_number)

    def EnterPassword(self, password):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((self.password))).send_keys(password)

    def ClickLogin(self):
        WebDriverWait(self.driver, 12).until(
            EC.element_to_be_clickable(self.button_submit)
        ).click()

    def LogOutInitial(self):
        WebDriverWait(self.driver, 12).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(4) > div > div > div.list-tile__trailing > button"))
        ).click()
        WebDriverWait(self.driver, 12).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#dialog > div > div > div > div.material-dialog__window-body.material-dialog__window-body_modify > div > div:nth-child(4) > div.drop-down-component__content > div.sessions__item-content > button > span"))
        ).click()