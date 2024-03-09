from selenium import webdriver
from selenium.webdriver.common.by import By
import my_id  # private info

ID = my_id.id
PASSWORD = my_id.password

driver = webdriver.Chrome()
url = 'https://ecampus.kookmin.ac.kr/login/index.php'
driver.get(url)  # bring us to the URL


driver.find_element(By.NAME, 'loginId').send_keys(ID)

driver.find_element(By.NAME, 'loginPwd').send_keys(PASSWORD)

driver.find_element(By.CLASS_NAME, 'submitform').click()







