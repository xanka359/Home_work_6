import zipfile, os
from zipfile import ZipFile
from pypdf import PdfReader
import openpyxl

from openpyxl import load_workbook
from xlrd import open_workbook

from script_os import TMP_DIR

path = TMP_DIR
file_dir = os.listdir(path)

with zipfile.ZipFile('resource/test.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:
        add_file = os.path.join(path, file)
        zf.write(add_file)

add_file = 'resource/test.zip'

with zipfile.ZipFile('resource/test.zip', mode='a', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(add_file, arcname='tmp/file_example_XLSX_50.xlsx')
    zf.write(add_file, arcname='tmp/file_example_XLS_10.xls')
    zf.write(add_file, arcname='tmp/Python Testing with Pytest (Brian Okken).pdf')

with zipfile.ZipFile('resource/test.zip', mode='a') as zf:
    for file in zf.namelist():
        print(file)

zip_ = ZipFile('resource/test.zip')

with ZipFile('resource/test.zip', 'r') as zip_file:
    print(zip_file.namelist())

    # тут начинается xlsx
    text_xlsx = zip_.read('tmp/file_example_XLSX_50.xlsx')
    workbook = load_workbook('tmp/file_example_XLSX_50.xlsx')
    sheet = workbook.active
    wb = openpyxl.load_workbook('tmp/file_example_XLSX_50.xlsx')
    length = len(wb.sheetnames)
    sheet_xlsx = wb.sheetnames
    row_count = sheet.max_row
    column_count = sheet.max_column

    print(text_xlsx)
    print(length)
    print(sheet_xlsx)
    print(row_count)
    print(column_count)
    print(sheet.cell(row=51, column=8).value)
    print(sheet.cell(row=2, column=2).value)

    # тут начинается xls
    workbook1 = open_workbook("tmp/file_example_XLS_10.xls")
    text_xls = zip_.read('tmp/file_example_XLS_10.xls')

    print(text_xls)
    print(workbook1.nsheets)
    print(workbook1.sheet_names())

    sheet = workbook1.sheet_by_index(0)
    print(sheet.nrows)
    print(sheet.ncols)
    print(sheet.cell_value(rowx=5, colx=1))

    # тут начинается pdf
    reader = PdfReader('tmp/Python Testing with Pytest (Brian Okken).pdf')
    print(len(reader.pages))
    print(reader.pages[5])
    print(reader.pages[255].extract_text())
    print(os.path.getsize("tmp/Python Testing with Pytest (Brian Okken).pdf"))
    print(reader.__sizeof__())

    assert "this is the book for you" in reader.pages[255].extract_text()
    assert os.path.getsize('tmp/Python Testing with Pytest (Brian Okken).pdf') == 3035139
    assert reader.__sizeof__() == 16

    zip_.close()
