import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import pandas as pd

PATH = r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)


def Archive_Yearly_Scrapper(ISIN_code):
    driver.get(
        'https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx')

    yearly = driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_rdbYearly")
    yearly.click()

    search_bar = driver.find_element_by_id("ContentPlaceHolder1_smartSearch")
    search_bar.send_keys(ISIN_code)
    search_bar.send_keys(Keys.ARROW_DOWN)
    search_bar.send_keys(Keys.RETURN)

    from_year = driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_cmbYearly")
    from_year_list = from_year.find_elements_by_tag_name('option')
    min_year = from_year_list[-1].text
    from_year = Select(from_year)
    from_year.select_by_value(min_year)

    submit_button = driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_btnSubmit")
    submit_button.click()

    download_button = driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_btnDownload1")
    download_button.click()

    time.sleep(5)

    driver.quit()


# Archive_Yearly_Scrapper("INE009A01021")

def Archive_Daily_Scraper(ISIN_code):
    driver.get(
        'https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx')

    search_bar = driver.find_element_by_id("ContentPlaceHolder1_smartSearch")
    search_bar.send_keys(ISIN_code)
    search_bar.send_keys(Keys.ARROW_DOWN)
    search_bar.send_keys(Keys.RETURN)

    from_search_bar = driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_txtFromDate")
    from_search_bar.click()

    from_year = driver.find_element_by_css_selector(
        "#ui-datepicker-div > div > div > select.ui-datepicker-year")
    from_year_list = from_year.find_elements_by_tag_name('option')
    min_year = from_year_list[0].text
    from_year = Select(from_year)
    from_year.select_by_value(min_year)

    from_month = Select(driver.find_element_by_css_selector(
        "#ui-datepicker-div > div > div > select.ui-datepicker-month")
    )
    from_month.select_by_value("0")

    from_date = driver.find_element_by_css_selector(
        "#ui-datepicker-div > table > tbody > tr:nth-child(1) > td:nth-child(7) > a")
    from_date.click()

    to_search_bar = driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_txtToDate")
    to_search_bar.click()

    to_year = driver.find_element_by_css_selector(
        "#ui-datepicker-div > div > div > select.ui-datepicker-year")
    to_year_list = to_year.find_elements_by_tag_name('option')
    max_year = to_year_list[-1].text
    to_year = Select(to_year)
    to_year.select_by_value(max_year)

    to_month = driver.find_element_by_css_selector(
        "#ui-datepicker-div > div > div > select.ui-datepicker-month")
    to_month_list = to_month.find_elements_by_tag_name('option')
    # max_month = to_month_list[-1].text
    to_month = Select(to_month)
    to_month.select_by_index(len(to_month_list)-1)

    to_date = driver.find_element_by_css_selector(
        "#ui-datepicker-div > table > tbody > tr:nth-child(1) > td:nth-child(6) > a")
    to_date.click()

    submit_button = driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_btnSubmit")
    submit_button.click()

    table = driver.find_element_by_css_selector(
        '#ContentPlaceHolder1_spnStkData > table')
    # print(table.get_attribute('innerHTML'))

    download_button = driver.find_element_by_css_selector(
        "#ContentPlaceHolder1_btnDownload1")
    download_button.click()

    df = pd.read_csv(r"C:\Users\HP\Downloads\{0}.csv".format(bse_code))
    print(df.head())

    time.sleep(5)

    driver.quit()


Archive_Daily_Scraper("INE009A01021", 500209)
# data of Infosys
