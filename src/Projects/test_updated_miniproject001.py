from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import time
import allure
from selenium.webdriver.common.by import By
@pytest.mark.smoke
@allure.title("Verify that login is working in Cura website")
@allure.description("#TC1-Simple login check on cura katalon website")
def test_katalon_demo():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()
    #make_appointment_btn=driver.find_element(By.LINK_TEXT,"Make Appointment")
    #make_appointment_btn.click()
    #make_appointment_btn=driver.find_element(By.PARTIAL_LINK_TEXT,"Appointment")
    #make_appointment_btn.click()
    #tag_name
    list_of_a_tags=driver.find_elements(By.TAG_NAME,"a")
    appointment_btn=list_of_a_tags[5]
    appointment_btn.click()
    allure.attach(driver.get_screenshot_as_png(),name="login-Screenshot",attachment_type=AttachmentType.PNG)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login","Assertion Fail Message1-Error matching the URLs"
    username_element = driver.find_element(By.ID, "txt-username")
    username_element.send_keys("John Doe")
    password_element = driver.find_element(By.ID, "txt-password")
    password_element.send_keys("ThisIsNotAPassword")
    login_element = driver.find_element(By.ID, "btn-login")
    login_element.click()
    allure.attach(driver.get_screenshot_as_png(),name="Appointment-Screenshot",attachment_type=AttachmentType.PNG)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment","Assertion Fail Message2-Error matching the URL(Appointment)"
    time.sleep(5)
    driver.quit()
