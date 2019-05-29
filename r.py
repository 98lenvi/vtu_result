from splinter import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


import time


global browser
browser = Browser('chrome')
x=10
while x < 18:

	url = "http://results.vtu.ac.in/resultsvitavicbcs_19/index.php"
	browser.visit(url)
	ec = expected_conditions
	time.sleep(7)
	browser.fill('lns', '1SK16CS'+str(x).zfill(3)+'\n')
	time.sleep(1)
	screenshot_path = browser.screenshot('/home/lenvi/Desktop/results/results')
	x = x+1

