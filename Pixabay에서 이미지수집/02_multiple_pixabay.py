from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
import requests
import os

# ChromeDriver 설치 및 초기화
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "https://pixabay.com/ko/images/search/사과/"
driver.get(url=url)

# 이미지 영역 찾기
image_area_xpath = "/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div"
image_area = driver.find_element(By.XPATH, image_area_xpath)
image_elements = image_area.find_elements(By.TAG_NAME, "img")

# 이미지 URL 수집
image_urls = []
for image_element in image_elements:
    image_url = image_element.get_attribute("data-lazy") or image_element.get_attribute("src")
    # placeholder 이미지(`blank.gif`)는 제외
    if "blank.gif" not in image_url:
        image_urls.append(image_url)

# 안전한 파일 이름 생성 함수
def safe_filename(index, url):
    ext = os.path.splitext(url.split("/")[-1])[-1]  # 확장자 추출
    return f"apple_{index}{ext}"

# 이미지 다운로드
for i, image_url in enumerate(image_urls):
    try:
        # HTTP GET 요청
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # 요청 실패 시 예외 발생

        # 안전한 파일 이름 생성
        file_name = safe_filename(i, image_url)

        # 이미지 파일 저장
        with open(file_name, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")

# 종료
driver.quit()
