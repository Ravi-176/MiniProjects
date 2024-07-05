from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import time
import allure
from selenium.webdriver.common.by import By
@pytest.mark.smoke
@allure.title("Verify that login is working properly and trial expired message is displayed")
@allure.description("Simple login and message check on idrive360 website")
def test_website():
    driver=webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    user_name=driver.find_element(By.XPATH,"//input[@id='username']")
    user_name.send_keys("augtest_040823@idrive.com")
    password=driver.find_element(By.XPATH,"//input[@id='password']")
    password.send_keys("123456")
    sign_in=driver.find_element(By.XPATH,"//button[@id='frm-btn']")
    sign_in.click()
    time.sleep(20)
    header_text=driver.find_element(By.XPATH,"//h5[@class='id-card-title']")
    assert header_text.text=="Your free trial has expired","Assertion Fail-Wrong header message"
    assert driver.current_url=="https://www.idrive360.com/enterprise/account?upgradenow=true"
    allure.attach(driver.get_screenshot_as_png(),name="SignIn-screenshot",attachment_type=AttachmentType.PNG)
    driver.quit()
