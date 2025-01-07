from selenium import webdriver  # selenium 모듈 설치
import chromedriver_autoinstaller  # chromedriver-autoinstaller 모듈 설치
from time import sleep
from urllib.request import Request, urlopen
from selenium.webdriver.common.by import By

# Chromedriver 자동 설치 및 실행
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# URL 설정
url = "https://pixabay.com/ko/images/search/사과/?pagi=3"
driver.get(url=url)

all_images = set()

# 이미지 영역 탐색
image_area_xpath = "/html/body/div[1]/div[1]/div/div[2]/div[2]/div"
image_area = driver.find_element(By.XPATH, image_area_xpath)
image_elements = image_area.find_elements(By.TAG_NAME, "img")

# 이미지 URL 수집
for image_element in image_elements:
    image_url = (
        image_element.get_attribute("data-src") or
        image_element.get_attribute("data-lazy") or
        image_element.get_attribute("src")
    )
    if image_url and "cdn.pixabay.com/photo/" in image_url:
        all_images.add(image_url)

print(f"총 이미지 개수: {len(all_images)}")

# 이미지 다운로드
for idx, image_url in enumerate(all_images):
    try:
        image_byte = Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        with open(f"apple{idx}.jpg", "wb") as f:
            f.write(urlopen(image_byte).read())
        print(f"[다운로드 성공] apple{idx}.jpg")
    except Exception as e:
        print(f"[다운로드 실패] {image_url} - {e}")

# 브라우저 종료
driver.quit()
