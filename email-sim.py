####################################################################################################################
# Generator Email/messenger/etc.
####################################################################################################################

import sys
import string
import time
import threading 
import datetime
from datetime import date

import random
from time import gmtime, strftime
from random import seed
from random import randint
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
seed()

keyword = sys.argv[1]

def ReadAllLines(filename):
	file = open(filename,mode='r')
	allread = file.read()
	file.close()
	return allread

def GmailLogin(email, password, driver):
	wait = WebDriverWait(driver, 20)
	driver.get("https://gmail.com/");
	driver.maximize_window()
	
	loginBox = wait.until(ec.visibility_of_element_located((By.ID, "identifierId")))
	loginBox.send_keys(email)

	nextBtn = wait.until(ec.visibility_of_element_located((By.ID, "identifierNext")))
	nextBtn.click()

	pwBox = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
	pwBox.send_keys(password)

	signinBtn = wait.until(ec.visibility_of_element_located((By.ID, "passwordNext")))
	signinBtn.click();
	
	driver.implicitly_wait(3)
	wait.until(ec.visibility_of_element_located((By.XPATH, "//tr")))
	driver.implicitly_wait(3)
	
def MessengerLogin(email,password, driver):
	wait = WebDriverWait(driver, 20)
	driver.get("https://www.messenger.com/");
	driver.maximize_window()

	loginBox = wait.until(ec.visibility_of_element_located((By.ID, "email")))
	loginBox.send_keys(email)

	pwBox = wait.until(ec.visibility_of_element_located((By.ID, "pass")))
	pwBox.send_keys(password)

	loginBox = wait.until(ec.visibility_of_element_located((By.ID, "loginbutton")))
	loginBox.click()
	driver.implicitly_wait(3)

def InstagramLogin(username,password, driver):
	wait = WebDriverWait(driver, 20)
	driver.implicitly_wait(10)
	login = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Log In')]")))
	login.click()
	
	driver.implicitly_wait(8)
	WebDriverWait(driver,10000).until(ec.visibility_of_element_located((By.XPATH,"//*[contains(@aria-label,'Phone number, username, or email')]")))
	userName = driver.find_element_by_name("username")
	userName.click()
	userName.send_keys(username)
	driver.implicitly_wait(1)

	WebDriverWait(driver,10000).until(ec.visibility_of_element_located((By.CSS_SELECTOR,"input[name='password']")))
	passwordElement = driver.find_element_by_name("password")
	passwordElement.click()
	passwordElement.send_keys(password + Keys.ENTER)
	
	driver.implicitly_wait(1)
	
#	login2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
#	login2.click()
	
	save = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Save Info')]")))
	save.click()
	
	driver.implicitly_wait(2)

	cancel = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Cancel')]")))
	cancel.click()
	driver.implicitly_wait(2)
	
if(keyword == "instagram"):
	chrome_options = webdriver.ChromeOptions()
	mobile_emulation = { "deviceName": "iPhone 6" }
	chrome_options.add_argument("--disable-notifications")
	chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get("https://instagram.com/")
	driver.maximize_window()
	
	wait = WebDriverWait(driver, 20)
	InstagramLogin(sys.argv[2],sys.argv[3], driver)
	
	switchonce = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href ='/direct/inbox/']")))
	switchonce.click()
	
	x = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Not Now']")))
	x.click()

	secondbutton = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(@aria-label,'New Message')]")))
	secondbutton.click()

	array = [""] 
	for i in range(10):
		array.append(sys.argv[4])
	f = open(sys.argv[5], "r")
	stuff = f.read()
	
	for search in array:
		namebox = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[name='queryBox']")))
		namebox.clear()
		namebox.send_keys(search)
		
		searchedfor = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'" + search + "')]")))
		searchedfor.click()

		buttonNext2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Next')]")))
		buttonNext2.click()

		myBuffer = stuff
		textArea = wait.until(ec.visibility_of_element_located((By.TAG_NAME, "textarea")))
		textArea.clear()
		textArea.send_keys(myBuffer)
	
		sendbutton = wait.until(ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Send')]")))
		sendbutton.click()
		driver.implicitly_wait(5)
		
		back = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@aria-label='Back']")))
		back.click()
		driver.implicitly_wait(2)
		
	print("Finished the instabot")
	driver.close()
	
elif(keyword == "messenger"):
	chrome_options = webdriver.ChromeOptions()
	#chrome_options.add("--disable-notifications")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	MessengerLogin(sys.argv[2],sys.argv[3], driver)
	wait = WebDriverWait(driver, 20)
	array = ["nick", "nick"] 
	for i in range(10):
		array.append(sys.argv[4])
	f = open(sys.argv[5], "r")
	stuff = f.read()
	
	for name in array:
		namebox = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search Messenger']")))
		namebox.clear()
		namebox.send_keys(name)
		driver.implicitly_wait(2)
		
		search = "//div//div//div//div//div//div[2]//ul[1]//li[1]//a[1]//div[1]//div[2]//div[1]//div[1]";
		myClick = wait.until(ec.visibility_of_element_located((By.XPATH, search)))
		myClick.click()

		myBuffer = stuff
		#myBuffer = myBuffer + ReadAllLines("C:\");
		
		message = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[starts-with(@class,'notranslate _5rpu')]")))
		message.clear()
		message.send_keys(myBuffer + Keys.ENTER)
		driver.implicitly_wait(2)
		message = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[starts-with(@class,'notranslate _5rpu')]")))
		message.clear()
	driver.close()
	print("Finished Messenger")
elif(keyword=="email"):
	chrome_options = webdriver.ChromeOptions()
	#chrome_options.add("--disable-notifications")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	GmailLogin(sys.argv[2],sys.argv[3], driver)
	
	array = [""]
	nameArray = [""]
	for i in range(10):
		array.append(sys.argv[4])
		nameArray.append(sys.argv[4])
	wait = WebDriverWait(driver, 15)
	f = open(sys.argv[5], "r")
	stuff = f.read()
	numEmails = 0
	for numEmails in range(0,len(array)):
		myBuffer ="Today: " + date.today().strftime("%m/%d/%Y") + "\n";
		myBuffer = myBuffer + "Dear " + nameArray[numEmails] + ",\n";
		myBuffer = myBuffer + stuff
		myBuffer = myBuffer + "\n"
		composebutton = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Compose')]")))
		composebutton.click()
		input = wait.until(ec.visibility_of_element_located((By.XPATH, "//textarea[@name='to']")))
		input.clear()
		input.send_keys(array[numEmails]);
		
		driver.implicitly_wait(3)
		subject = driver.find_element_by_name("subjectbox")
		subject.clear()
		subject.send_keys(subText);
		
		body = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@aria-label='Message Body']")))
		body.clear()
		body.send_keys(myBuffer)
		
		send = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[starts-with(@class,'dC')]")))
		send.click()
		driver.implicitly_wait(5)
		print("Finished email")
		wait.until(ec.visibility_of_element_located((By.XPATH, "//tr")))

	driver.close()
	print("Finished email")