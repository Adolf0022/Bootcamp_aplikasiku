import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_Add_Shooping_Cart_CO(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_a_Checkout_a_Book(self):
        driver = self.driver
        driver.get("https://demowebshop.tricentis.com/")  # Buka link
        driver.maximize_window()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "ico-login").click()  # Klik link login
        time.sleep(1)
        driver.find_element(By.ID, "Email").send_keys("kikir@gmail.com")
        driver.find_element(By.ID, "Password").send_keys("Semangat45!")
        driver.find_element(By.CSS_SELECTOR, "[value='Log in']").click()
        time.sleep(2)
        link_account = driver.find_element(By.CLASS_NAME, "account").text
        self.assertIn("kikir@gmail.com", link_account)
        driver.find_element(By.CSS_SELECTOR, "[href='/books']").click()
        time.sleep(2)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/books", "Did not navigate to the book page") # Verify that user directed to book page
        time.sleep(1)
        text_book= driver.find_element(By.CLASS_NAME, "page-title").text
        self.assertIn("Books", text_book)
        product_1 = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/h2/a").text #Get product name
        print(f"Nama Produk yang diambil: {product_1}")
        driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/a/img").click()
        time.sleep(2)
        product_1a = driver.find_element(By.CSS_SELECTOR, "[itemprop='name']").text #Get product name detail
        print(f"Nama Produk yang diambil: {product_1a}")
        self.assertIn(product_1,product_1a) #Verify product is match
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-button-13").click() #click button add to cart
        time.sleep(3)
        succes_msg = driver.find_element(By.CLASS_NAME, "content").text # Verifikasi message "The product has been added to your cart"
        self.assertIn("The product has been added to your ",succes_msg)
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "cart-label").click() #click cart link
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/cart", "Did not navigate to the Cart page") # Verify that user directed to cart page
        time.sleep(2)
        product_1b = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[3]/a").text
        self.assertIn(product_1,product_1b) #Verify product in cart is available
        driver.find_element(By.CSS_SELECTOR, "[type='checkbox']").click() #check Product
        driver.find_element(By.ID, "termsofservice").click # Check tearm and conditions
        driver.find_element(By.ID, "checkout").click() #click checkout button
        time.sleep(2)
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/onepagecheckout", "Did not navigate to the Check out page") # Verify that user directed to checkout page
        text_co = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[1]/h1").text
        self.assertIn("Checkout", text_co)
        driver.find_element(By.CLASS_NAME, "button-1 new-address-next-step-button").click() #click button continue using existing address
        driver.find_element(By.ID, "PickUpInStore").click() #Pick up in store
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "button-1 new-address-next-step-button").click() #click button continue
        time.sleep(1)
        driver.find_element(By.ID, "paymentmethod_3").click() #select Purchase Order
        driver.find_element(By.CLASS_NAME, "button-1 new-address-next-step-button").click() #click button continue
        time.sleep(1)
        driver.find_element(By.ID,"PurchaseOrderNumber").send_keys("00045tyomrw") #Set po number
        driver.find_element(By.CLASS_NAME, "button-1 new-address-next-step-button").click() #click button continue
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "button-1 new-address-next-step-button").click() #click button continue
        self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/checkout/completed/", "Did not navigate to the Complete page") # Verify that user directed to completed page
        thankyou_text = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[1]/h1") 
        time.sleep(5)
        
if __name__ == "__main__":
    unittest.main()
