from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Use case: enter leetcode URL to get file name and explanation
# 옵션 생성
options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# 창 숨기는 옵션 추가
options.add_argument("headless")

# initialise browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
						   options=options)
# load page
URL = input('URL: ')
browser.get(URL)

# execute java script
browser.execute_script(
	"return document.getElementsByTagName('html')[0].innerHTML")

sleep(5)
problem_title = browser.find_element(By.XPATH,
									 '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/span')

problem_description = browser.find_element(By.XPATH,
										   '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[3]/div')
# problem_code = browser.find_element(By.XPATH,
# 									'//*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]')

# print(problem_title.text)
s = problem_title.text
s = s.replace(". ", "_")
s = s.replace(" ", "_")
f_name = s + ".py"
f = open("new/" + f_name, "w")
f.write('from typing import List\n')
f.write('\'\'\'\n')
f.write(URL + '\n\n')
f.write(problem_description.text + '\n')
f.write('\'\'\'')
f.write('\n\nif __name__ == "__main__":\n\ts = Solution()')
print("created: ", f_name)
