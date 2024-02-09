from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import requests
import quickstart
import re
from translate import Translator
import get_latitude_and_longitude



# Create a Translator object and translate the string
translator = Translator(to_lang="en")

    
driver = webdriver.Chrome()    
driver.maximize_window()
driver.get("https://www.weatherford.com/about-us/locations/")

cookey_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id=\"CybotCookiebotDialogBodyButtonAccept\"]"))).click()

try:
    country_groups = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class=\"country-group\"]")))
except:
    pass

print(f'country group count = ', len(country_groups))

for index, country_group in enumerate(country_groups):
    driver.execute_script("arguments[0].scrollIntoView(false); window.scrollBy(0, 0);", country_group)
    
    try:
        countries = WebDriverWait(country_group, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class=\"accordion accordion-section location-country-group accordion-init\"]")))
    except:
        pass
    
    print(f'countries of country group = ', len(countries))

    for index, country in enumerate(countries):

        country_name = ""
        city_name = ""
        company_name = ""
        address = ""
        phone_number = ""

        try:
            country_name_div = WebDriverWait(country, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"accordion-head\"]")))
            country_name_div.click()
            country_name = country_name_div.text
        except:
            pass
        
        try:
            company_ul = WebDriverWait(country, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[class=\"list-offices list-offices-columns\"]")))
            company_lis = WebDriverWait(company_ul, 15).until(EC.presence_of_all_elements_located((By.TAG_NAME, "li")))
        except:
            pass

        print(f'country count of country = ', len(company_lis))

        for index, company in enumerate(company_lis):

            try:
                city_name = WebDriverWait(company, 15).until(EC.presence_of_element_located((By.TAG_NAME, "h6"))).text
            except:
                pass

            print(f'city_name = ', city_name)

            try:
                company_name = WebDriverWait(company, 15).until(EC.presence_of_element_located((By.TAG_NAME, "strong"))).text
            except:
                pass

            print(f'company name = ', company_name)

            try:
                address_lines = WebDriverWait(company, 15).until(EC.presence_of_element_located((By.TAG_NAME, "address"))).text
                separator = ', '
                address = separator.join(address_lines.split('\n'))
            except:
                pass

            print(f'address =', address)

            try:
                phone_number = WebDriverWait(company, 15).until(EC.presence_of_element_located((By.TAG_NAME, "a"))).text
            except:
                pass
            
            print(f'phone number = ', phone_number)

            sleep(1)    
            quickstart.main()
            columnCount = quickstart.getColumnCount()
        
            
            print(f'columnCount = ',columnCount)

            cleaned_number = re.sub(r'[+\s]', '', phone_number)

            results = []
            results.append(str(columnCount + 1))
            results.append(country_name)
            results.append(city_name)
            results.append(company_name)
            results.append(address)
            results.append(phone_number)

            quickstart.main()
            RANGE_DATA = f'get_company_location_weatherford!A{columnCount + 2}:F'
            quickstart.insert_data(RANGE_DATA, results)
        
    
driver.quit()

        
        
    
