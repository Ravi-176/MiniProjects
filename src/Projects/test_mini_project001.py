from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
def test_katalon_demo():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #< a
    #id = "btn-make-appointment"
    #href = "./profile.php#login"
    #class ="btn btn-dark btn-lg" > Make Appointment < / a >
    driver.maximize_window()
    appointment_element=driver.find_element(By.ID,"btn-make-appointment")
    appointment_element.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)
    #< input
    #type = "text"
    #class ="form-control" id="c" name="username" placeholder="Username" value="" autocomplete="off" >
    username_element=driver.find_element(By.ID,"txt-username")
    username_element.send_keys("John Doe")
    #< input
    #type = "password"
    #class ="form-control" id="txt-password"
    #name="password" placeholder="Password" value="" autocomplete="off" >
    password_element=driver.find_element(By.ID,"txt-password")
    password_element.send_keys("ThisIsNotAPassword")
    #< button
    #id = "btn-login"
    #type = "submit"
    #class ="btn btn-default" > Login < / button >
    login_element=driver.find_element(By.ID,"btn-login")
    login_element.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/#appointment"
    verify_text=driver.find_element(By.CLASS_NAME,"col-sm-12")
    verify_text.text=="Make Appointment"
    time.sleep(5)
    driver.quit()
