from selenium import webdriver
import time
import datetime
import calendar
from db import Database
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome("chromedriver.exe")
year_now = datetime.datetime.now().year
month_now = datetime.datetime.now().month
day_now = datetime.datetime.now().day

def log_in(login_text, password_text):
    with open('top_secret.txt', 'r') as reader:
        url = reader.readlines()[0]
    browser.get(url)
    login = browser.find_element_by_id('form_login_username')
    login.send_keys(login_text)
    password = browser.find_element_by_id('form_login_password')
    password.send_keys(password_text)
    zaloguj = browser.find_element_by_id('form_login_submit')
    zaloguj.click()
    time.sleep(1)

def log_into_company():
    with open('top_secret.txt', 'r') as reader:
        url = reader.readlines()[1]
    browser.get(url)
    time.sleep(1)

def cookie_killer():
    cookies = browser.find_element_by_class_name('btn-gray-gradient')
    cookies.click()

def move_to_sale_invoice():
    invoicing = browser.find_element_by_link_text("FAKTUROWANIE")
    invoicing.click()
    time.sleep(1)

def change_dates(number):
    number = number.split('/')
    date_from = browser.find_element_by_xpath("//input[@type='text'][@data-name='date_date_from']")
    date_from.click()
    date_from.clear()
    date_from.send_keys('{}-{}-{}'.format(str(number[3]), str(number[2]), str(last_day_month(number[3], number[2]))))
    ActionChains(browser).move_by_offset(20, 20).click().perform()

    date_to = browser.find_element_by_xpath("//input[@type='text'][@data-name='date_date_to']")
    date_to.click()
    date_to.clear()
    date_to.send_keys('{}-{}-{}'.format(str(number[3]), str(number[2]), str(last_day_month(number[3], number[2]))))
    ActionChains(browser).move_by_offset(-20, -20).click().perform()

def search_invoice(number):
    invoice_search = browser.find_element_by_id('dt-sale-search')
    invoice_search.click()
    invoice_search.clear()
    invoice_search.send_keys('{}'.format(number))
    time.sleep(2)
    document = browser.find_element_by_class_name('va-middle')
    document.click()
    time.sleep(1)

def correction_press():
    correction = browser.find_element_by_link_text("KOREKTA")
    correction.click()
    time.sleep(1)

def change_exhibit_date():
    exhibit_date = browser.find_element_by_id('form_doc_date')
    exhibit_date.click()
    exhibit_date.clear()
    exhibit_date.send_keys('{}-{}-{}'.format(str(year_now), str(month_now).zfill(2), str(day_now)))
    time.sleep(1)

def last_day_month(year, month):
    return calendar.monthrange(int(year), int(month))[1]

def change_sale_date(number):
    number = number.split('/')
    sale_date = browser.find_element_by_id('form_doc_dateofsale')
    sale_date.click()
    sale_date.clear()
    sale_date.send_keys('{}-{}-{}'.format(str(number[3]), str(number[2]), str(last_day_month(number[3], number[2]))))
    time.sleep(1)

def change_accounting_period():
    accounting_period = browser.find_element_by_id('form_doc_acc_period')
    accounting_period.click()
    accounting_period.clear()
    accounting_period.send_keys('{}-{}'.format(str(year_now), str(month_now).zfill(2)))
    time.sleep(1)

def change_sequence():
    sequence = browser.find_element_by_id('form_doc_sequence')
    sequence.click()
    time.sleep(1)
    kmf = browser.find_element_by_css_selector('#form_doc_sequence [value="11"]')
    kmf.click()
    time.sleep(1)

def get_correction_number():
    global correction_number
    correction_number = browser.find_element_by_xpath('//input[@id="form_doc_no"][@value]').get_attribute('value')


def why_correction():
    reason = browser.find_element_by_id('form_doc_correction_reason')
    reason.send_keys("Błędna aktywacja")
    time.sleep(1)

def change_position():
    positions = len(browser.find_elements_by_xpath("//tr[@class='cursor-pointer item']"))
    for i in range(positions):
        position = browser.find_elements_by_class_name('ml-2')[i]
        position.click()
        quantity = browser.find_element_by_xpath("//div[@class='flex xs1']/div/div/div/div/input")
        quantity.click()
        quantity.send_keys('0')
        save_position = browser.find_element_by_xpath('//button[.="Zapisz"]')
        save_position.click()
        time.sleep(1)

def finish_correction(number, db):
    finish_it = browser.find_element_by_id('form_doc_submit')
    finish_it.click()
    time.sleep(10)
    db.created(number)

def download_invoce_correction(number, db):
    download = browser.find_element_by_class_name('flat-button')
    download.click()
    db.downloaded(number)
    time.sleep(12)