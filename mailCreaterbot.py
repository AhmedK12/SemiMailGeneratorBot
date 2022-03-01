import os
import threading
import pickle
import string
import Signup1
import time
import random
import Databasehandler1
from selenium.webdriver import ActionChains
import Support
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


def change_ip(control_port='9051'):
    c = '(echo authenticate \'\"likas1\"\'; echo signal newnym; echo quit) | nc localhost ' + control_port
    os.system(c)
    os.system(c)
    time.sleep(3)


def store_coockies(cookies, file_name):
    f = open("Cookies/microsoft/"+file_name, 'wb')
    pickle.dump(cookies, f)
    f.close()


def Create_mail(data):
    option = Options()
    option.add_argument('no-sandbox')
    driver = selenium.webdriver.Chrome(executable_path='/opt/google/chrome/google-chrome',options=option)


    try:
        driver.get('https://console.firebase.google.com/u/1/project/dkexpress-dfbbe/database/dkexpress-dfbbe-default-rtdb/data')


    except:
        driver.quit()
        return






if __name__ == '__main__':
    Create_mail("name")
