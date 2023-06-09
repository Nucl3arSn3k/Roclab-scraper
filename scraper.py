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
import time
from selenium.common.exceptions import NoSuchElementException
import json


def main():
    webscrape()


def webscrape():
    optionsv2 = Options()
    # optionsv2.add_argument("--headless")
    url = "https://cdcs.ur.rochester.edu/"

    optionsv2.binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    browser = webdriver.Firefox(
        executable_path="C:\Program Files (x86)\geckodriver-v0.32.2-win32\geckodriver.exe",  # desktop gecko adress C:\Program Files (x86)\geckodriver-v0.32.2-win32\geckodriver.exe
        options=optionsv2,   #laptop gecko adress C:\geckodriver-v0.31.0-win64\geckodriver.exe
    )

    # driver = webdriver.Firefox(options=optionsv2)
    browret = browser.get(url)
    req = requests.get(url)
    

    dropdown = Select(browser.find_element_by_id("ddlTerm"))
    # print(job0)
    dropdown.select_by_value("D-Summer 2023")

    button = browser.find_element_by_id("btnSearchTop")

    # elements are all stored at odd numbers
    # numlist = [01,03,05,07,09,11,13,14]

    # final odd number for summer 2023 is 975
    """
    
    """

    button.click()
    time.sleep(20)
    page_source = browser.page_source
    
    #job0 = browser.find_element_by_id("rpResults_ctl01_lblSchool")
    #content = job0.text
    #writes html to a file
    with open("tablecontents.html", "w", encoding="utf-8") as file:
        file.write(page_source)

    data_dict = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "data": [],
    }

    # Write the dictionary to a JSON file
    with open("data.json", "w") as f:
        json.dump(data_dict, f)


    with open("tablecontents.html", "r",encoding="utf-8") as file:
        html_code = file.read()
    soup = BeautifulSoup(html_code, 'html.parser')
    for i in range(1, 3000, 2):
        formatted_number = "{:02d}".format(i)
        # print(formatted_number)
        sub_array = {}
        try: 
            print("Starting try for "+ str(i))
            #str0 = soup.find(id="rpResults_ctl{}_lblSchool".format(formatted_number))
            #strval = "rpResults_ctl{}_lblSchool".format(formatted_number)
            #str2 = soup.find(id="rpResults_ctl{}_lblDept".format(formatted_number))
            str3 = soup.find(id="rpResults_ctl{}_cellCourse".format(formatted_number))
            strval = "rpResults_ctl{}_cellCourse".format(formatted_number)
            str4 = soup.find(id="rpResults_ctl{}_cellTitle".format(formatted_number))
            str5 = soup.find(id="rpResults_ctl{}_lblTerm".format(formatted_number))
            str6 = soup.find(id="rpResults_ctl{}_lblStatus".format(formatted_number))
            str7 = soup.find(id="rpResults_ctl{}_lblCredits".format(formatted_number))
            #sub_array["school"] = str0.text
            #sub_array["dept"] = str2.text
            sub_array["course"] = str3.text
            sub_array["title"] = str4.text
            sub_array["term"] = str5.text
            sub_array["status"] = str6.text
            sub_array["credits"] = str7.text

        except AttributeError:
            print("No such element as " + strval)
            break

        data_dict["data"].append(sub_array)

    with open("data.json", "w") as f:
        json.dump(data_dict, f)
    # print(str0)
    print("Program ending,wiping local html file.")
    os.remove("tablecontents.html")
    # browser.quit()


def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver


if __name__ == "__main__":
    main()
