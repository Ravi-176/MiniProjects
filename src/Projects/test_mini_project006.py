from selenium import webdriver
from selenium.webdriver.common.by import By
import time,allure,pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
@pytest.mark.smoke
@allure.title("Add user and then search in OrangeHRM")
@allure.description("#TC1-Verify that the added user is present by searching in OrangeHRM")
def test_OrangeHRM():
    driver=webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    #time.sleep(5)
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//input[@name='username']")))
    driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//span[text()='Admin']")))
    driver.find_element(By.XPATH,"//span[text()='Admin']").click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//button[normalize-space()='Add']")))
    driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,"//h6[text()='Add User']")))
    #Select User Role
    driver.find_element(By.XPATH,"//div[@class='oxd-select-wrapper']//div[@class='oxd-select-text oxd-select-text--active']//div[@class='oxd-select-text-input' and text()='-- Select --']").click()
    #driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow']").click()
    #enter employee name
    driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Samia")