from selenium import webdriver #selenium 모듈 설치해야함 (pip install selenium -> pip show selenium)
import chromedriver_autoinstaller #chromedriver-autoinstaller 모듈 설치해야함 (pip install chromedriver-autoinstaller)
from time import sleep

from urllib.request import Request, urlopen

from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "https://pixabay.com/ko/images/search/사과/"
driver.get(url=url)

image_xpath = "/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div/div[1]/div[3]/div/a/img"
image_url = driver.find_element(By.XPATH, image_xpath).get_attribute('src')
print("image_url:", image_url)

image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
f = open("applehahaha.jpg", "wb")
f.write(urlopen(image_byte).read())
f.close()

sleep(300)