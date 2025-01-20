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

# 이전 코드와 달라진 부분
    def classify(self):
        
        for i, row in self.order_list.head(5).iterrows(): # df 데이터를 >> 이터로우즈=2개의 행들을 쭉 반복하겠다는 뜻 / head(5)=너무 많아서 복잡하니까 위에서 5개만 뽑겠다
            brand_name = ''
            idx_partner = 0
            for j in range(len(self.brands)):
                if self.brands[j] in row['상품명']:
                    print(f'{self.brands[j]}이(가) {j}번째에 포함되어 있습니다.')
                    brand_name = self.brands[j]
                    idx_partner = j
                    break
            print(f'{row["상품명"]} 은 {brand_name} 브랜드 입니다. {j}번째')
            print(f'업체명:{self.partners[idx_partner]}')
            # print(row['상품명'])

        print(len(self.brands), self.brands)
        print(len(self.partners), self.partners)
# 이전 코드와 달라진 부분

if __name__ == '__main__':
    ce = ClassificationExcel('주문목록20221112_NEW.xlsx', '파트너목록_NEW.xlsx')
    ce.classify()