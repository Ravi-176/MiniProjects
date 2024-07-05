from selenium import webdriver
import time,allure,pytest
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify the error message when username field is empty")
@allure.description("#TC-Enter all fields except username")
def test_codepen():
    driver =webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.ID,"result"))
    email_id=driver.find_element(By.XPATH,"//input[@id='email']")
    email_id.send_keys("somesh065@gmail.com")
    password=driver.find_element(By.XPATH,"//input[@id='password']")
    password.send_keys("123456")
    cnf_password=driver.find_element(By.XPATH,"//input[@id='password2']")
    cnf_password.send_keys("123456")
    time.sleep(2)
    submit_btn=driver.find_element(By.XPATH,"//button[text()='Submit']")
    submit_btn.click()
    allure.attach(driver.get_screenshot_as_png(),name="login-screenshot",attachment_type=AttachmentType.PNG)
    assert (driver.find_element(By.XPATH,"//input[@id='username']/following::small").text=="Username must be at least 3 characters")
    time.sleep(5)
    driver.quit()