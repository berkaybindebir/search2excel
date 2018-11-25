import os
import csv
import datetime

import xlsxwriter as x_writer
from config import config as _config

base_dir = _config['base_directory']
file_name = _config['file_name']

def folder_setup(fn, base_dir = base_dir, file_name = file_name):
    
    """Directory Variables
    """
    cwd = ''
    is_dir_exist = False
    is_file_name_exist = False

    # Check Base Directory
    if base_dir is 'Default':
        cwd = os.getcwd()
    else:
        cwd = base_dir

    # Check is Dir Exist
    for def_dir in os.listdir(cwd):
        if def_dir == 's2excelDocuments':
            is_dir_exist = True
    
    if is_dir_exist == False:
        print("Directory is not exist!")
        print("Directory Creating..")
        os.mkdir("{}/s2excelDocuments".format(cwd))
    

    # Add Time Unique File Name
    full_time = datetime.datetime.now()
    formatted_time = full_time.isoformat().split(".")[0]

    # Create a Workbook & Worksheet for Excel
    workbook = x_writer.Workbook('{}/s2excelDocuments/{}-{}.xlsx'.format(cwd, file_name, formatted_time))
    worksheet = workbook.add_worksheet()
    
    # Row and Column Setup
    worksheet.write(0, 0, "TITLE")
    worksheet.write(0, 1, "WEB SITE URL")
    worksheet.write(0, 2, "WEB SITE DESCRIPTION")
    
    
    expenses = (fn)

    row = 1
    col = 0

    for name, link, desc in (expenses):
        worksheet.set_column("A:A", len(name))
        worksheet.write(row, col, name)
        
        worksheet.set_column("B:B", len(link))
        worksheet.write(row, col + 1, link)
        
        worksheet.set_column("C:C", len(desc))
        worksheet.write(row, col + 2, desc)
        
        row += 1

    workbook.close()

    print('Your File is \n{}/s2excelDocuments/{}-{}.xlsx'.format(cwd, file_name, formatted_time))




