from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functions.web_functions import *
import time 
import json

driver = webdriver.Chrome()

driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")

last_comment = " "

#loading user variables
config_data = load_config()
target = config_data["target"]
username = config_data["username"]
password = config_data["password"]

sign_into_reddit(driver, username, password)
time.sleep(2)

while True:

    search_user(driver, target)
    last_comment = search_for_new_comment(driver, last_comment)
    nice_word = get_random_nice_word()
    time.sleep(4)
    post_reply(driver, nice_word)

