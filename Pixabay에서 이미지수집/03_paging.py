import os
import requests
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

# ChromeDriver 설치 및 초기화
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(5)

def crawl_image(keyword, pages):
    image_urls = []
    for i in range(1, pages + 1):
        url = f"https://pixabay.com/ko/images/search/{keyword}/?pagi={i}"
        driver.get(url=url)

        # 이미지 영역 XPath (최종 코드에서 사용된 XPath)
        image_xpath = "//div[contains(@class, 'verticalMasonry')]//img"
        try:
            image_elements = driver.find_elements(By.XPATH, image_xpath)

            for image_element in image_elements:
                image_url = image_element.get_attribute("data-lazy") or image_element.get_attribute("src")
                # Placeholder 이미지 제외
                if "blank.gif" not in image_url:
                    print(f"Found image: {image_url}")
                    image_urls.append(image_url)
        except Exception as e:
            print(f"Error while parsing page {i}: {e}")

    return image_urls

def save_images(keyword, image_urls):
    path = keyword

    # 디렉토리 만들기
    if not os.path.exists(path):
        os.mkdir(path)

    for i, image_url in enumerate(image_urls):
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()

            filename = os.path.join(path, image_url.split("/")[-1])
            with open(filename, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {image_url}: {e}")

def crawl_and_save_image(keyword, pages):
    print(f"Crawling images for keyword: {keyword}, Pages: {pages}")
    image_urls = crawl_image(keyword, pages)
    print(f"Total images found: {len(image_urls)}")
    save_images(keyword, image_urls)

# 실행
crawl_and_save_image("가지", 1)
crawl_and_save_image("양파", 2)

# 종료
driver.quit()
