from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json 

def load_config():
    """Loads config data from config.json and returns as a dict"""
    with open("text_files/config.json") as config:
        config_data = json.load(config)
    return config_data

def sign_into_reddit(driver, username, password):
    """Signs into the bot Reddit account using the passed username and password"""
    usernameField = driver.find_element_by_id("loginUsername")
    usernameField.send_keys(username)
    passwordField = driver.find_element_by_id("loginPassword")
    passwordField.send_keys(password)
    logInButton = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button")
    logInButton.click()

def search_user(driver, target_user):
    """Function to bring up the profile page of the target user"""
    target_user_url = "https://www.reddit.com/user/" + target_user + "/comments/"
    driver.get(target_user_url)

def search_for_new_comment(driver, last_comment):
    """compares last posted comment to current comment to see if it has changed"""
    current_comment = driver.find_element_by_class_name('_1qeIAgB0cPwnLhDF9XSiJM').text
    while True:
        if current_comment != last_comment:
            return current_comment
        else:
            time.sleep(15)
            driver.refresh()

def get_random_nice_word():
    """Extracts a word from the nice_adjectives txt and returns one at random"""
    nice_words_txt = open("text_files/nice_adjectives.txt").read().splitlines()
    return random.choice(nice_words_txt)

def post_reply(driver, nice_word):
    """posts a new reply to the targets latest comment"""
    replyButton = driver.find_element_by_class_name('VFryWeVNuBPgqyjc5h68S')
    replyButton.click()
    time.sleep(3)
    comment_box = driver.find_element_by_class_name('public-DraftEditor-content')
    comment_box.send_keys("This comment is " + nice_word + ".")
    replyButton = driver.find_element_by_class_name('_22S4OsoDdOqiM-hPTeOURa')
    replyButton.click()




