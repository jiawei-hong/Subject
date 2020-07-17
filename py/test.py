from selenium import webdriver
import time

while (True):
    browser = webdriver.Chrome()
    browser.get('http://localhost:8000/category/1')
    time.sleep(3)
    browser.close()