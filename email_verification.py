import os
import threading
import pickle
import string
import time
import random
import Databasehandler
from selenium.webdriver import ActionChains
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


def store_coockies(cookies, file_name):
    f = open("Cookies/microsoft/"+file_name, 'ab')
    pickle.dump(cookies, f)
    f.close()


def read_cookiess(file_name):
    f = open("Cookies/microsoft/" + file_name, 'rb')
    cookies = pickle.load(f)
    f.close()
    return  cookies


def change_ip(control_port='9051'):
    c = '(echo authenticate \'\"likas1\"\'; echo signal newnym; echo quit) | nc localhost ' + control_port
    os.system(c)
    os.system(c)
    time.sleep(3)


def Create_mail(email):
    change_ip('9061')
    PROXY = "127.0.0.1:9060"  # IP:PORT or HOST:PORT
    chrome_options = selenium.webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=socks5://' + PROXY)
    driver = selenium.webdriver.Chrome(executable_path='/root/Desktop/Desktop1/chromedriver_linux64/chromedriver',
                                       options=chrome_options)


    driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1594804686&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d7032c737-eaea-1ced-2179-d2296b6bcf11&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
    # for cookie in read_cookiess(email.split('@')[0]):
    #     driver.add_cookie(cookie)
    print(email.split('@')[0])
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, 'i0116')))
    driver.find_element_by_id('i0116').send_keys(email)
    time.sleep(1)
    # driver.execute_script("window.open('https://www.google.com');")
    # driver.switch_to.window(driver.window_handles[-1])
    # driver.find_element_by_id('idSIButton9').click()
    # print("dfghjk")
    # WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, 'i0118')))
    # print('2')
    # # driver.find_element_by_id('i0118').send_keys("1")
    # print('3')
    time.sleep(1)
    while 1>0:
        if input('enter_num')==1:
            store_coockies(driver.get_cookies(), email.split('@')[0])
            driver.close()
            return
        else:
            driver.close()
            return



if __name__ == '__main__':
    f = open('email1').readlines()
    for email in f:
        try:
            Create_mail(email)
        except:
            print('hdfjcxz')
            pass

