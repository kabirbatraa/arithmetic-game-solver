
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep 

import psutil

chrome_options = Options()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-setuid-sandbox')

# set up the webdriver
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

# Get the PID of the Chrome process
pid = driver.service.process.pid

# Set the process priority to "Realtime"
p = psutil.Process(pid)
p.nice(psutil.REALTIME_PRIORITY_CLASS)

# navigate to the website
driver.get('https://arithmetic.zetamac.com/')

# sleep(10)
# duration = driver.find_element(By.CSS_SELECTOR, 'select[name="duration"]')
# duration.click()
# duration_30 = driver.find_element(By.CSS_SELECTOR, 'option[value="30"]')
# duration_30.click()

# click the Start button
start_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Start"]')
start_button.click()

try:
  while True:
  # for i in range(5):
    driver.find_element(By.CSS_SELECTOR, 'input.answer').send_keys(str(int(eval(str(driver.find_element(By.CSS_SELECTOR, 'span.problem').text).replace('÷', '/').replace('–', '-').replace('×', '*')))))
except:
  pass

sleep(1)
driver.save_screenshot('screenshotHeadless.png')

# wait for user input
input('Press Enter to continue...')

# quit
driver.quit()