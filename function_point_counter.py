#! python
# -*- coding: utf-8 -*-

import sys
import xlrd
import package2system

def open_excel(excel_file="/cygdrive/c/tmp/shangxian_condition.xlsx"):
    '''打开EXCEL_FILE'''
    try:
        data = xlrd.open_workbook(excel_file)
        return data
    except Exception,e:
        print str(e)

def open_sheet(excel_file,sheet_name):
    '''打开EXCEL_FILE并找到名为SHEET_NAME的表格'''
    try:
        data = open_excel(excel_file)
        return data.sheet_by_name(sheet_name)
    except Exception,e:
        print str(e)

def count_function_points_from_sheets(excel_file,*sheet_names):
    '''统计EXCEL_FILE中SHEET_NAMES中的各系统及其功能变更个数'''
    function_points_map = {}
    for sheet_name in sheet_names:
        sheet = open_sheet(excel_file,sheet_name)
        p2s = package2system.package2system()
        for i in range(1,sheet.nrows):
            if xlrd.oNUM == sheet.row_types(i)[0]:
                new_function_points = str(int(sheet.row_values(i)[0])).split()
            else:
                new_function_points = sheet.row_values(i)[0].split()
                package = sheet.row_values(i)[1]
                system = p2s.get_system(package)
                function_points = function_points_map.get(system,[])
                function_points.extend(new_function_points)
                function_points_map[system] = function_points

    for system,function_points in function_points_map.items():
        print system,len(set(function_points))

if __name__ == "__main__":
    if len(sys.argv) <3 :
        script = sys.argv[0]
        print "Usage: %s excel_file sheet_names..." % script
    else:
        excel_file = sys.argv[1]
        sheet_names = sys.argv[2:]
        count_function_points_from_sheets(excel_file,*sheet_names)
