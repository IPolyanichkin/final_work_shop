import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_acc = driver.find_element_by_css_selector("#menu-item-50 > a")
my_acc.click()
log_email = driver.find_element_by_id("username")
log_email.send_keys("polenko_777@mail.ru")
log_password = driver.find_element_by_id("password")
log_password.send_keys("137nhbvtnbkrcfynby")
login_btn = driver.find_element_by_css_selector("form > p:nth-child(3) > input.woocommerce-Button.button")
login_btn.click()
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout > a")
logout_text = logout.text
assert logout_text == "Logout"