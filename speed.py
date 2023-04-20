
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

import psutil

# set up the webdriver
driver = webdriver.Chrome()

# Get the PID of the Chrome process
pid = driver.service.process.pid

# Set the process priority to "Realtime"
p = psutil.Process(pid)
p.nice(psutil.REALTIME_PRIORITY_CLASS)

# navigate to the website
driver.get('https://arithmetic.zetamac.com/')

sleep(10)

# click the Start button
start_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Start"]')
start_button.click()

try:
  while True:
    driver.find_element(By.CSS_SELECTOR, 'input.answer').send_keys(str(int(eval(str(driver.find_element(By.CSS_SELECTOR, 'span.problem').text).replace('÷', '/').replace('–', '-').replace('×', '*')))))
except:
  pass

# wait for user input
input('Press Enter to continue...')

# quit
driver.quit()