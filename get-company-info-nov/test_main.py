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
driver.get("https://www.nov.com/contact#8036035a-e577-44bc-a961-631adbc08c0f")



cookey_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=\"not-EE font-primary font-semibold items-center inline-flex min-h-[46px] rounded-none transition ease-in-out delay-15 px-[30px] text-base justify-center py-[15px] text-white no-underline bg-primary cursor-pointer hover:bg-red-dark basicFocus hover:!no-underline ml-[20px] min-w-[120px] max-h-[40px] !min-h-[40px] !text-sm !leading-16 !font-medium hover:!bg-red-light\"]")))
cookey_button.click()
sleep(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
driver.switch_to.frame(iframe)

# scroll_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id=\"TopHolder\"]")))

# print(scroll_div)
# page_height = driver.execute_script("return arguments[0].scrollHeight;", scroll_div)
# driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scroll_div)



sleep(5)

location_list = driver.find_elements(By.CSS_SELECTOR, "tr[class=\"facilityMatch\"]")

print(f'Total Location Count = ', len(location_list))

for index, location in enumerate(location_list):

    company_name = ""
    country_name = ""
    address1 = ""
    address2 = ""
    phone_number = ""
   

    
    try:
        company_name = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class=\"facility-name\"]"))).text
    except:
        pass

    print(f'company_name = ', company_name)

   
    try:
        country_name = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class=\"facility-country\"]"))).text
    except:
        pass

    print(f'country_name = ', country_name)
    

    try:
        address1 = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class=\"facility-address\"]"))).text
    except:
        pass
    
    print(f'address1 = ', address1)

    try:
        address2 = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class=\"facility-address2\"]"))).text
    except:
        pass
    
    print(f'address2 = ', address2)
    
    try:
        cleaned_number = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class=\"facility-phone\"]"))).text
        phone_number = cleaned_number.replace('Phone:', "")
    except:
        pass

    print(f'phone_number = ', phone_number)

    # try:
    #     other_text = WebDriverWait(location, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class=\"hiddenText\"]"))).text
    # except:
    #     pass

    # print(f'other_text = ', other_text)

    sleep(1)    
    quickstart.main()
    columnCount = quickstart.getColumnCount()
   
    
    print(f'columnCount = ',columnCount)

    results = []
    results.append(str(columnCount + 1))
    results.append(company_name)
    results.append(country_name)
    results.append(address1)
    results.append(address2)
    results.append(phone_number)

    quickstart.main()
    RANGE_DATA = f'get_company_location_nov!A{columnCount + 2}:F'
    quickstart.insert_data(RANGE_DATA, results)
    
                        
    sleep(2)

    
driver.quit()
sleep(5)

        
        
    
