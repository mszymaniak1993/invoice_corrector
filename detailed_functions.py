from selenium import webdriver
import time
import datetime
import calendar

browser = webdriver.Chrome("chromedriver.exe")
year_now = datetime.datetime.now().year
month_now = datetime.datetime.now().month
day_now = datetime.datetime.now().day

def log_in():
    with open('top_secret.txt', 'r') as reader:
        url = reader.readlines()[0]
    browser.get(url)
    login = browser.find_element_by_id('form_login_username')
    login.send_keys('mszymaniak@superksiegowa.pl')
    password = browser.find_element_by_id('form_login_password')
    password.send_keys('dsfk938u')
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

def search_invoice():
    invoice_search = browser.find_element_by_id('dt-sale-search')
    year = datetime.date.today().year
    invoice_search.send_keys('A1/1/{}'.format(year))
    time.sleep(1)
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

def change_sale_date():
    sale_date = browser.find_element_by_id('form_doc_dateofsale')
    sale_date.click()
    sale_date.clear()

    def last_day_of_month(any_day):
        next_month = any_day.replace(day=28) + datetime.timedelta(days=4) # this will never fail
        return (next_month - datetime.timedelta(days=next_month.day)).strftime('%Y-%m-%d')
    year = datetime.date.today().year
    month = datetime.datetime.today().month-1
    sale_date.send_keys(str(last_day_of_month(datetime.date(year, month, 10))))
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

def why_correction():
    reason = browser.find_element_by_id('form_doc_correction_reason')
    reason.send_keys("Błędna aktywacja")
    time.sleep(1)

def change_position():
    position = browser.find_element_by_class_name('ml-2')
    position.click()
    quantity = browser.find_element_by_id('input-41')
    quantity.click()
    quantity.send_keys('0')
    save_position = browser.find_element_by_xpath('//button[.="Zapisz"]')
    save_position.click()
    time.sleep(1)

def finish_correction():
    finish_it = browser.find_element_by_id('form_doc_submit')
    finish_it.click()
    time.sleep(10)

def download_invoce_correction():
    download = browser.find_element_by_class_name('flat-button')
    download.click()
    time.sleep(10)