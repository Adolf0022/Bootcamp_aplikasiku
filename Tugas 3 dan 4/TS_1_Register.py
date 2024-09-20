import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_Register(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_a_register_success(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/register", "Did not navigate to the register page")
        time.sleep(1)
        driver.find_element(By.ID,"gender-male").click()  # Klik checkbox gender
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Abg") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("Super") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("abgsuper0790@gmail.com") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45!") # Set the confirm password
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        succes_msg = driver.find_element(By.CLASS_NAME, "result").text # verify message Your registration completed appear
        self.assertIn("Your registration completed",succes_msg)
        time.sleep(1)

    def test_b_register_failed_empty_firstname(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/register", "Did not navigate to the register page") # verify that user is on register page
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("nunung") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("nunung@gmail.com") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45!") # Set the confirm password 
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        error_msg_1 = driver.find_element(By.CLASS_NAME, "field-validation-error").text # verify message Your First name is required appear
        self.assertIn("First name is required.",error_msg_1)
        time.sleep(1)

    def test_c_register_failed_empty_lastname(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/register", "Did not navigate to the register page") # verify that user is on register page
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Nunung") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("nunung@gmail.com") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45!") # Set the confirm password 
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        error_msg_2 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="LastName"]').text # verify message Last name is required required appear
        self.assertIn("Last name is required.",error_msg_2)

    def test_d_register_failed_empty_email(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/register", "Did not navigate to the register page") # verify that user is on register page
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Nunung") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("Super") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45!") # Set the confirm password 
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        error_msg_3 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="Email"]').text # verify message Email is required appear
        self.assertIn("Email is required.",error_msg_3)

    def test_e_register_failed_invalid_email(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/register", "Did not navigate to the register page") # verify that user is on register page
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Nunung") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("Super") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("nunung@") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45!") # Set the confirm password 
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        error_msg_4 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="Email"]').text # verify message Wrong email is appear
        self.assertIn("Wrong email",error_msg_4)

    def test_f_register_failed_empty_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url,"https://demowebshop.tricentis.com/register", "Did not navigate to the register page") # verify that user is on register page
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Nunung") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("Super") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("nunung@gmail.com") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45!") # Set the confirm password 
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        error_msg_5 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="Password"]').text # verify message Password is required. is appear
        self.assertIn("Password is required.",error_msg_5)
        error_msg_6 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="ConfirmPassword"]').text # verify message The password and confirmation password do not match is appear
        self.assertIn("The password and confirmation password do not match.",error_msg_6)

    def test_g_register_failed_invalid_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url,"https://demowebshop.tricentis.com/register", "Did not navigate to the register page") # verify that user is on register page
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Nunung") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("Super") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("nunung@gmail.com") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Sem") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45!") # Set the confirm password 
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        error_msg_7 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="Password"]').text # verify message The password should have at least 6 characters is appear
        self.assertIn("The password should have at least 6 characters.",error_msg_7)
        error_msg_8 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="ConfirmPassword"]').text # verify message The password and confirmation password do not match is appear
        self.assertIn("The password and confirmation password do not match.",error_msg_8)

    def test_h_register_failed_empty_ConfirmPassword(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url,"https://demowebshop.tricentis.com/register", "Did not navigate to the register page") # verify that user is on register page
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Nunung") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("Super") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("nunung@gmail.com") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        error_msg_9 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="ConfirmPassword"]').text # verify message Password is required. is appear
        self.assertIn("Password is required.",error_msg_9)

    def test_i_register_failed_ConfirmPassword_not_same_with_password(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url,"https://demowebshop.tricentis.com/register", "Did not navigate to the register page") # verify that user is on register page
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Nunung") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("Super") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("nunung@gmail.com") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45") # Set the confirm password not match with password
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        error_msg_10 = driver.find_element(By.CSS_SELECTOR,'[data-valmsg-for="ConfirmPassword"]').text # verify message The password and confirmation password do not match is appear
        self.assertIn("The password and confirmation password do not match.",error_msg_10)

    def test_j_register_failed_Duplicate_email(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/") # Open Link 
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME,"ico-register").click() # Click Link Register
        time.sleep(1)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/register", "Did not navigate to the register page")
        time.sleep(1)
        driver.find_element(By.ID,"gender-male").click()  # Klik checkbox gender
        time.sleep(1)
        driver.find_element(By.ID,"FirstName").send_keys("Abg") # Set the firstname
        time.sleep(1)
        driver.find_element(By.ID,"LastName").send_keys("Super") # Set the lastname
        time.sleep(1)
        driver.find_element(By.ID,"Email").send_keys("abhx@gmail.com") # Set the email
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("Semangat45!") # Set the password
        time.sleep(1)
        driver.find_element(By.ID,"ConfirmPassword").send_keys("Semangat45!") # Set the confirm password
        time.sleep(1)
        driver.find_element(By.ID,"register-button").click() # click button register
        time.sleep(1)
        fail_msg = driver.find_element(By.CLASS_NAME, "validation-summary-errors").text # verify message The specified email already exists appear
        self.assertIn("The specified email already exists",fail_msg)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()



