
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


import time


global browser
browser = Browser('chrome')
x=23
while x < 45:

	url = "http://results.vtu.ac.in/vitaviresultcbcs2018/index.php"
	browser.visit(url)
	ec = expected_conditions
	
	browser.fill('lns', '1SK16CS'+str(x).zfill(3)+'\n')
	if ec.alertIsPresent():
		alert = browser.get_alert()
		alert.accept()
	time.sleep(1)
	screenshot_path = browser.screenshot('/home/lenvin/Documents/results/results')
	x = x+1

