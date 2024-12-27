from selenium import webdriver #selenium 모듈 설치해야함 (pip install selenium -> pip show selenium)

import chromedriver_autoinstaller #chromedriver-autoinstaller 모듈 설치해야함 (pip install chromedriver-autoinstaller)

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "https://pixabay.com/ko/"
driver.get(url=url)