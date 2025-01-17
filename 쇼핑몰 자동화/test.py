# Ch02. 쇼핑몰 주문 요청서 분류 자동화 프로젝트 - 02. 엑셀파일을 불러오고 브랜드와 업체명 매핑 준비하기
import pandas as pd
import openpyxl

class ClassificationExcel:

    def __init__(self, order_xlsx_filename):
        # 주문목록 (데이터를 가공함)
        df = pd.read_excel(order_xlsx_filename)
        self.order_list = df

        print(self.order_list.head()) # 주문목록 top 5 만 출력

if __name__ == '__main__':
    ce = ClassificationExcel('주문목록20221112_NEW.xlsx')