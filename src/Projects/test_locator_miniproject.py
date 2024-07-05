from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support.relative_locator import locate_with
import allure,pytest,time
def test_codepen():
    driver=webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.maximize_window()
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.ID,"result"))
    submit_btn=driver.find_element(By.XPATH,"//button[text()='Submit']")
    submit_btn.click()
    time.sleep(3)
    user_name=driver.find_element(By.XPATH,"//input[@id='username']")
    error_msg=driver.find_element(locate_with(By.TAG_NAME,'small').below(user_name)).text
    assert error_msg=="Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(),name="login-screenshot",attachment_type=AttachmentType.PNG)
    time.sleep(5)
    driver.quit()