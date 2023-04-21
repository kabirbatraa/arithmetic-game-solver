from selenium import webdriver
from selenium.webdriver.common.by import By
import psutil
# Here Chrome  will be used
driver = webdriver.Edge()
# answer.send_keys(str(int(eval(problem.text.replace('÷','/').replace('–','-').replace('×','*')))))
pid = driver.service.process.pid
p = psutil.Process(pid)
p.nice(psutil.REALTIME_PRIORITY_CLASS)
# Opening the website
driver.get("https://arithmetic.zetamac.com/")
 
table = {247:47, 8211:45, 215:42}

start_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Start"]')
start_button.click()

# find span with this data:  <span class="problem">74 + 35</span>
problem = driver.find_element(By.CSS_SELECTOR, 'span.problem')

# find input block:  <input class="answer">
answer = driver.find_element(By.CSS_SELECTOR, 'input.answer')

# repeat until game is over
while True:
  try:
    answer.send_keys(f'{int(eval(problem.text.translate(table)))}')
  except:
    break



# wait for user input
input('Press Enter to continue...')

# quit
driver.quit()