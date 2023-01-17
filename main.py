from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C://Program Files (x86)/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3282140366&f_AL=true&f_E=1%2C2%2C3&f_WT=2&geoId=105149290' \
      '&keywords=python%20developer&location=Ontario%2C%20Canada&refresh=true '
driver.maximize_window()
driver.get(URL)

# job apply page before login
time.sleep(3)
signin_btn = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
signin_btn.click()


# signin page
time.sleep(3)
email = driver.find_element(By.ID, "username")
email.send_keys("Email ID")
password = driver.find_element(By.ID, "password")
password.send_keys("Password")
login = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login.click()

# job apply page after login
time.sleep(3)
job_apply = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div['
                                          '1]/div[1]/div[3]/div/div/div')
job_apply.click()

# contact information popup
time.sleep(3)
country_code = driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:('
                                             'urn:li:fs_normalized_jobPosting:3282140366,381997202687483517,'
                                             'phoneNumber~country)"]/option[1]')
country_code.click()
contact_num = driver.find_element(By.XPATH, '//*[@id="urn:li:fs_easyApplyFormElement:('
                                            'urn:li:fs_normalized_jobPosting:3282140366,381997202687483517,'
                                            'phoneNumber~nationalNumber)"]')
contact_num.clear()
next_btn = driver.find_element(By.CSS_SELECTOR, 'footer div button span')
next_btn.click()

# resume upload page
time.sleep(3)
resume_next_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div['
                                                '2]/button[2]')
resume_next_btn.click()


# review page
time.sleep(3)
review = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
review.click()

# review & submit application page
time.sleep(3)
submit_btn = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
submit_btn.click()
