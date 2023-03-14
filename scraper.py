from fileinput import close
import requests
from xml.etree import ElementTree as et
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
from lxml import html
from selenium.webdriver.firefox.options import Options
import bleach
import re
import os
from selenium.webdriver.support.ui import Select

def main():
    webscrape()

















def webscrape():
    optionsv2 = Options()
    #optionsv2.add_argument("--headless")
    url = "https://cdcs.ur.rochester.edu/"
    
    optionsv2.binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    browser = webdriver.Firefox(
        executable_path="C:\Program Files (x86)\geckodriver-v0.32.2-win32\geckodriver.exe",
        options=optionsv2,
    )

    #driver = webdriver.Firefox(options=optionsv2)
    browret = browser.get(url)
    page_source = browser.page_source
    soup = BeautifulSoup(page_source, "lxml")
    job0 = soup.find(id="ddlTerm")
    dropdown = Select(browser.find_element_by_id("ddlTerm"))
    # print(job0)
    dropdown.select_by_value("D-Fall 2023")
    with open("test.html", "w+") as f:
        f.write(str(job0))

    button = browser.find_element_by_id("btnSearchTop")
    button.click()
    #browser.quit()




def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver


if __name__ == "__main__":
    main()