from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
from argparse import ArgumentParser

# arg parser if needed
parser = ArgumentParser()
parser.add_argument('email', help='Facebook email', type=str)
parser.add_argument('password', help='Facebook password', type=str)
parser.add_argument('classification', help='select classification of questions', type=str)
parser.add_argument('file', help='text file name', type=str)
parser.add_argument('idx', help='index of the target question in every line of text file', type=int)
args = parser.parse_args()

# launch chrome driver
options = Options()
options.add_argument('--disable-notifications')

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)

# facebook login
chrome.get('https://www.facebook.com/')

email = chrome.find_element_by_id('email')
password = chrome.find_element_by_id('pass')

email.send_keys(args.email)
password.send_keys(args.password)
password.submit()

time.sleep(3)

# gartic
chrome.get('https://gartic.io/auth/facebook')

chrome.find_element_by_class_name('btBlueBig.ic-rooms').click()

time.sleep(1.5)

chrome.find_element_by_class_name('btBlueBig.ic-rooms').click()

time.sleep(1.5)

button = chrome.find_elements_by_tag_name('button')
count = 0
for i in button:
    if count == 0:
        count += 1
    elif count == 1:
        i.click()
        break

time.sleep(1.5)

# select the classification of questions
s = Select(chrome.find_element_by_tag_name('select'))
s.select_by_value(args.classification)

# input questions
ipt = chrome.find_elements_by_tag_name('input')

f = open(args.file, 'r')
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split()
for word in lines:
    for i in ipt:
        if i.get_attribute('type') == 'text' :
            i.send_keys(word[args.idx])
            i.submit()
            break
    time.sleep(0.05)

time.sleep(1.5)

# submit
chrome.find_element_by_class_name('btYellowBig.ic-config').click()

time.sleep(3)

# quit chrome
chrome.quit()
