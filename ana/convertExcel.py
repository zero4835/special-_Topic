import openpyxl
import opencc

# 載入 Excel 檔案
wb = openpyxl.load_workbook('segment.xlsx')

# 選擇要處理的工作表
ws = wb['Sheet1']

# 選擇要處理的欄位
column = ws['A']

# 建立繁簡轉換器
converter = opencc.OpenCC('s2t')

# 將簡體中文轉換成繁體中文
for cell in column:
    if isinstance(cell.value, str):
        cell.value = converter.convert(cell.value)

# 將更改寫回 Excel 檔案
wb.save('example.xlsx')
