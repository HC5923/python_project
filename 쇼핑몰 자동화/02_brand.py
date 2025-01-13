# Ch02. 쇼핑몰 주문 요청서 분류 자동화 프로젝트 - 03. 브랜드명과 업체명 찾기
import pandas as pd
import openpyxl


class ClassificationExcel:

    def __init__(self, order_xlsx_filename, partner_info_xlsx_filename):
        # 주문목록 (데이터를 가공함)
        df = pd.read_excel(order_xlsx_filename)
        df = df.rename(columns=df.iloc[1]) #1번을 열제목으로 쓰겠다
        df = df.drop([df.index[0], df.index[1]])
        df = df.reset_index(drop=True)
        self.order_list = df

        # 파트너목록
        df_partners = pd.read_excel(partner_info_xlsx_filename)

        self.brands = df_partners['브랜드'].to_list()
        self.partners = df_partners['업체명'].to_list()

        print(len(self.brands), self.brands)
        print(len(self.partners), self.partners)

        print(self.brands[0], self.partners[0])

        print(self.order_list['상품명'].head()) # 주문목록 top 5 만 출력


if __name__ == '__main__':
    ce = ClassificationExcel('주문목록20221112_NEW.xlsx', '파트너목록_NEW.xlsx')