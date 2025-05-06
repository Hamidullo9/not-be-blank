import pytest
from pages.login_page import LoginPage


def test_login_success(driver):
    driver.get("https://my.proweb.uz/log-in")

    login = LoginPage(driver)
    login.EnterPhoneNumber('998330091296')
    login.ClickLogin()
    login.EnterPassword('Hamidullo8')
    login.ClickLogin()
    # login.LogOutInitial()


def test_login_unsuccess(driver):
    driver.get("https://my.proweb.uz/log-in")
    try:
        login = LoginPage(driver)
        login.EnterPhoneNumber('998000000000')
        login.ClickLogin()
        login.EnterPassword('Hamidullo8')
        login.ClickLogin()
    except:
        return