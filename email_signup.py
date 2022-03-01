import os
import threading
import pickle
import string
import Signup1
import time
import random
import Databasehandler
from selenium.webdriver import ActionChains
import Support
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


def read_email():
    return open('email1','r').readlines()


def save_login_credentials(email_id, password, type):
    if type == 1:  # we got the point
        f = open('keywithrewards1', 'a')
        f.write(email_id + "#$" + password+"\n")
        f.close()
    if type == 2:  # same ip error
        f = open('keywithoutrewards', 'a')
        f.write(email_id + "#$" + password+"\n")
        f.close()
    if type == 3:  #
        pass


def perchage(driver):
    driver.find_element_by_id('req_for_bonuses_link').click()
    print('1')
    time.sleep(1)
    driver.find_element_by_link_text(' PLAY FREE BTC WITHOUT CAPTCHA ').click()
    print(2)
    time.sleep(1)
    text = driver.find_element_by_class_name('account_unblock_span option_play_multiply_span').text
    print(text)
    driver.find_element_by_class_name('lottery_link').click()
    driver.find_element_by_id('lottery_tickets_purchase_count').send_keys(text)
    driver.find_element_by_id('purchase_lottery_tickets_button').click()
    return


def store_coockies(cookies, file_name):
    f = open("Cookies/"+file_name, 'wb')
    pickle.dump(cookies, f)
    f.close()


def change_ip(control_port='9061'):
    c = '(echo authenticate \'\"likas1\"\'; echo signal newnym; echo quit) | nc localhost ' + control_port
    os.system(c)
    os.system(c)
    time.sleep(3)

def signup(email,password,driver):
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "signup_button")))
        time.sleep(4)
        driver.find_element_by_id('signup_form_email').send_keys(email)
        time.sleep(2)
        driver.find_element_by_id('signup_form_password').send_keys(password)
        return True
    except:
        return False

def open_browser(port):
    change_ip(str(int(port) + 1))
    PROXY = "127.0.0.1:" + port  # IP:PORT or HOST:PORT
    chrome_options = selenium.webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=socks5://' + PROXY)
    driver = selenium.webdriver.Chrome(executable_path='/root/Desktop/Desktop1/chromedriver_linux64/chromedriver',options=chrome_options)




if __name__ == '__main__':
    pass