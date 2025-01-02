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

# find(), find_all() .find_elements
image_area_xpath = "/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div"
image_area = driver.find_element(By.XPATH, image_area_xpath)
image_elements = image_area.find_elements(By.TAG_NAME, "img")

for image_element in image_elements:
    image_url = image_element.get_attribute("src")
    print(image_url)

# image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
# f = open("applehahaha.jpg", "wb")
# f.write(urlopen(image_byte).read())
# f.close()

# sleep(300)