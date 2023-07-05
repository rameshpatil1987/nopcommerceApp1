import openpyxl


class Excel:
    @staticmethod
    def get_cellvalue(path, sheet, row, col):
        wb = openpyxl.load_workbook(path)
        value = wb[sheet].cell(row, col).value
        print('xl value is:', value)
        return value
