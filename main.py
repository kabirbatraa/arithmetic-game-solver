from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 
import random

# set up the webdriver
driver = webdriver.Chrome()

# navigate to the website
driver.get('https://arithmetic.zetamac.com/')

sleep(2)

# in the element:
"""
<select name="duration">
            <option value="30">30 seconds</option>
            <option value="60">60 seconds</option>
            <option selected="" value="120">120 seconds</option>
            <option value="300">300 seconds</option>
            <option value="600">600 seconds</option>
          </select>
"""
# open the duration drop down and select 30 seconds
# duration = driver.find_element(By.CSS_SELECTOR, 'select[name="duration"]')
# duration.click()
# sleep(1)
# duration_30 = driver.find_element(By.CSS_SELECTOR, 'option[value="30"]')
# duration_30.click()
# sleep(1)

sleep(4)

# click the Start button
start_button = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Start"]')
start_button.click()


# repeat until game is over
while True:

  # sleep for a random time between 0.8 and 1.3 seconds
  sleep(random.uniform(1.3, 1.8))


  # if span.problem doesnt exist, then break out of the loop
  if not driver.find_elements(By.CSS_SELECTOR, 'span.problem'):
    break

  # find span with this data:  <span class="problem">74 + 35</span>
  problem = driver.find_element(By.CSS_SELECTOR, 'span.problem')

  # find input block:  <input class="answer">
  answer = driver.find_element(By.CSS_SELECTOR, 'input.answer')

  # write the number 0 in answer block
  # answer.send_keys('0')

  # convert problem.text to a string and replace ÷ division sign with /
  # also convert – to - and × to *
  # problemText = str(problem.text).replace('÷', '/')
  problemText = str(problem.text).replace('÷', '/').replace('–', '-').replace('×', '*')


  # read the problem as a string and then execute it as if it is a math expression
  # then convert to integer and then to string
  executedString = str(int(eval(problemText)))

  # write the executedString to answer block on character at a time with a small delay between each character
  for char in executedString:
    answer.send_keys(char)
    # sleep for random time between 0.08 and 0.15 seconds
    sleep(random.uniform(0.08, 0.15))
    # sleep(0.15)



# wait for user input
input('Press Enter to continue...')

# quit
driver.quit()