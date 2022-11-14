from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from selenium.webdriver.chrome.options import Options

# use https://account.proton.me/signup as an example to create email account
url = 'https://account.proton.me/signup'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# specify the location of the Google Chrome webdriver
s = Service('C://Users//squ_a//OneDrive//Рабочий стол//proton_mail//linkedin-challenge//chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)

# User information
User_Name = input('Enter UserName:\n')
Password = input('Enter Password:\n')
Verif_Mail = input('Verification email address:\n')

driver.get(url)
driver.implicitly_wait(20)
driver.maximize_window()

# fill main form
# Enter user_name
time.sleep(10)
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it
                                ((By.XPATH, "//iframe[ @ title = 'Имя пользователя']")))
pyautogui.typewrite(User_Name)
pyautogui.press("TAB")
time.sleep(3)
pyautogui.press("TAB")
time.sleep(3)
# enter password
pyautogui.typewrite(Password)
pyautogui.press("TAB")
time.sleep(3)
# repeat password
pyautogui.typewrite(Password)
pyautogui.press("TAB")
pyautogui.press("ENTER")

# verification
time.sleep(5)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[text()='Эл. почта']"))).click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.ID, 'email'))).send_keys(Verif_Mail)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//button[text()='Получить проверочный код']"))).click()

# Write from verification email address 6 digit code
Verif_Code = input('Input verification number:\n')
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='verification']").send_keys(Verif_Code)
time.sleep(3)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Подтвердить']"))).click()
print("Account is created")
time.sleep(10)
driver.close()
