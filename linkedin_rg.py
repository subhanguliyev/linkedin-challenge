from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# specify the location of the Google Chrome webdriver
s = Service('C://Users//squ_a//OneDrive//Рабочий стол//proton_mail//linkedin-challenge//chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
# linkedin registration url
url = 'https://www.linkedin.com/signup'

Ln_User_Name = input("Enter User name:\n")
Ln_Password = input("Enter Password:\n")
first_name = input("Enter First name:\n")
last_name = input("Enter Last name:\n")
phone_number = input("Enter Phone number:\n")

driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

# fill reg form
time.sleep(5)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'email-address'))).send_keys(Ln_User_Name)
time.sleep(3)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(Ln_Password)
time.sleep(3)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[text()='Согласиться и присоединиться']"))).click()

# fill user information
time.sleep(5)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
time.sleep(3)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(last_name)
time.sleep(3)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[text()='Продолжить']"))).click()

# after captcha
print("LinkedIn account created")

# If phone verification is needed
# time.sleep(5)
# WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it
#                                 ((By.XPATH, "//iframe[@title='Проверка безопасности']")))
# time.sleep(3)
# WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "phonenumber"))).send_keys(phone_number)

# time.sleep(5)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
#     (By.XPATH, "//button[text()='Отправить']"))).click()
# time.sleep(20)
# verify_code = input("Enter verification code from SMS:\n")
