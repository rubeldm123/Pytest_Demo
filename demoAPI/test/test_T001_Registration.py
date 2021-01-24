import pytest
from selenium.webdriver import Chrome


@pytest.mark.Smoke
def test_registration_valid_data1():
    global path
    path = "./chromedriver"
    driver = Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()


@pytest.mark.Sanity
def test_registration_invalid_data2():
    driver = Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()


@pytest.mark.Smoke
def test_registration_Ivalid_data3():
    driver = Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()


@pytest.mark.Sanity
def test_registration_invalid_data4():
    driver = Chrome(executable_path=path)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.quit()
