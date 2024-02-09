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
driver.get("https://www.slb.com/contact-us/locations")



cookey_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id=\"onetrust-accept-btn-handler\"]")))
cookey_button.click()
sleep(5)

# Get the initial page height
page_height = driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


while True:
    try:
         # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        location_list = driver.find_elements(By.CSS_SELECTOR, "article[class=\"address-card-article-container address-card-jv\"]")
        more_div = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"location-landing-page-load-more-container\"]")))
        WebDriverWait(more_div, 10).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    except:
        print("Click Exception Ouucurs")
        break



sleep(3)

location_list = driver.find_elements(By.CSS_SELECTOR, "article[class=\"address-card-article-container address-card-jv\"]")

print(f'Total Location Count = ', len(location_list))

for index, location in enumerate(location_list):
    try:
        print(f'Total Location Count = ', len(location_list))
        company_name = ""
        country_name = ""
        address = ""
        phone_number = ""
        
        try:
            company_name = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"address-card-article-location-name\"]"))).text
        except:
            pass

        print(f'company_name = ', company_name)
    
        try:
            address_div = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class=\"address-card-article-location-address\"]")))
            address = address_div.text
            country_name = address_div.find_elements(By.CSS_SELECTOR, "span[class=\"address-card-article-location-name\"]")[2].text
        except:
            pass
        
        print(f'address = ', address)
        print(f'country_name = ', country_name)

        try:
            phone_number = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[class=\"address-card-article-location-phone-number\"]"))).text
        except:
            pass

        print(f'phone_number = ', phone_number)

    
        sleep(1)    
        quickstart.main()
        columnCount = quickstart.getColumnCount()
    
        
        print(f'columnCount = ',columnCount)

        cleaned_number = re.sub(r'[+\s]', '', phone_number)

        results = []
        results.append(str(columnCount + 1))
        results.append(company_name)
        results.append(country_name)
        results.append(address)
        results.append(cleaned_number)

        quickstart.main()
        RANGE_DATA = f'get_company_location_slb!A{columnCount + 2}:E'
        quickstart.insert_data(RANGE_DATA, results)
        
                            
        sleep(2)
    except:
        continue

    
driver.quit()
sleep(5)

        
        
    
