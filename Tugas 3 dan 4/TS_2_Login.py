import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_a_login_success(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")  # Buka link
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ico-login").click()  # Klik link login
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/login", "Did not navigate to the register page") # Verify that user directed to login page
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys("kikir@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("Semangat45!")
        driver.find_element(By.CSS_SELECTOR, "[value='Log in']").click()
        time.sleep(2)
        link_account = driver.find_element(By.CLASS_NAME, "account").text
        self.assertIn("kikir@gmail.com", link_account)

    def test_b_login_Failed_Empty_email(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ico-login").click() # Click link login
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/login", "Did not navigate to the register page") # Verify that user directed to login page
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set valid password
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "[value='Log in']").click() # click button Login
        time.sleep(3)
        msg_1 = driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again", msg_1 ) # verify message Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect appear
        time.sleep(3)
        time.sleep(3)
        msg_2 = driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
        self.assertIn("No customer account found", msg_2 )
        time.sleep(3)

    def test_c_login_Failed_Empty_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ico-login").click() # Click link login
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/login", "Did not navigate to the register page") # Verify that user directed to login page
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("kikir@gmail.com") # Set valid email 
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "[value='Log in']").click() # click button Login
        time.sleep(3)
        msg_3 = driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again", msg_3) # verify message Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect appear
        time.sleep(3)
        msg_4 = driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
        self.assertIn("The credentials provided are incorrect", msg_3)
        time.sleep(3)

    def test_d_login_Failed_wrong_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ico-login").click() # Click link login
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/login", "Did not navigate to the register page") # Verify that user directed to login page
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("kikir@gmail.com") # Set valid email 
        time.sleep(2)
        driver.find_element(By.ID,"Password").send_keys("1234567890!") # Set valid password
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "[value='Log in']").click() # click button Login
        time.sleep(3)
        msg_3 = driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again", msg_3) # verify message Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect appear
        time.sleep(3)
        msg_4 = driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
        self.assertIn("The credentials provided are incorrect", msg_4)
        time.sleep(3)

    def test_e_login_Failed_Invalid_account(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ico-login").click() # Click link login
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/login", "Did not navigate to the register page") # Verify that user directed to login page
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("123444kikir@gmail.com") # Set valid email 
        time.sleep(2)
        driver.find_element(By.ID,"Password").send_keys("1234567890!") # Set valid password
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "[value='Log in']").click() # click button Login
        time.sleep(3)
        msg_5 = driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
        self.assertIn("Login was unsuccessful. Please correct the errors and try again", msg_5) # verify message Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect appear
        time.sleep(3)
        msg_6 = driver.find_element(By.CLASS_NAME,"validation-summary-errors").text
        self.assertIn("No customer account found", msg_6)
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()








