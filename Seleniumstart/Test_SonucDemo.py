from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_SonucDemo:
    def test_invalid_login():
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        driver.maximize_window() #ekranı büyütür
        sleep(5)
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(5)
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)
        errorMessage = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
        testResult  = errorMessage.text("Epic ")
        print(f"TEST SONUCU: {testResult}")


testClass = Test_SonucDemo()
testClass.test_invalid_login()