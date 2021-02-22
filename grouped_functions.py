from detailed_functions import *

def preparation(login_text, password_text):
    log_in(login_text, password_text)
    log_into_company()
    cookie_killer()

def create_correction_invoice(number, db):
    move_to_sale_invoice()
    change_dates(number)
    search_invoice(number)
    correction_press()
    change_exhibit_date()
    change_sale_date(number)
    change_accounting_period()
    change_sequence()
    get_correction_number()
    why_correction()
    change_position()
    finish_correction(number, db)
    download_invoce_correction(number, db)
