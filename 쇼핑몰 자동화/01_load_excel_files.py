import pandas as pd
import openpyxl


class ClassificationExcel:

    def __init__(self, order_xlsx_filename, partner_info_xlsx_filename):
        
        df = pd.read_excel(order_xlsx_filename)