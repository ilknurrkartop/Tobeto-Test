from selenium import webdriver
from webdriver_manager . chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Test_SauceDemo:

    def test_username_password_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("")
        sleep(3)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        sleep(3)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"BOŞ TEST SONUCU: {testResult}")
        
    def test_password_empty(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("İlknur")
        sleep(2)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"ŞİFRE YAZILI DEGİLKEN TEST SONUCU: {testResult}")
        

    def test_error(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"HATALI TEST SONUCU: {testResult}")
    def successfull_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window() 
        sleep(3)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID , "login-button")
        loginButton.click()
        sleep(3)
        listOfElement = driver.find_elements(By.CLASS_NAME, "inventory_item")
        urunSayisi = len(listOfElement) == 6
        print(len(listOfElement))
        print(f"BEKLENEN SONUC : {urunSayisi}")



testClass = Test_SauceDemo()
testClass.test_username_password_empty()
testClass.test_password_empty()
testClass.test_error()
testClass.successfull_login() 