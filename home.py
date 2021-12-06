import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,600);")
selenium_ruby = driver.find_element_by_css_selector("div#text-22-sub_row_1-0-2-0-0 ul.products > li > a >h3")
selenium_ruby.click()
reviews = driver.find_element_by_css_selector("#product-160 > div > ul > li:nth-child(2)  > a")
reviews.click()
five_stars = driver.find_element_by_css_selector("a.star-5")
five_stars.click()
comment = driver.find_element_by_id("comment")
comment.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Ilia")
email = driver.find_element_by_id("email")
email.send_keys("polenko_777@mail.ru")
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()