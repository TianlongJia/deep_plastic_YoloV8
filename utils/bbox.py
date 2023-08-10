from numpy import empty
import xlwings as xw
import os
import sys


def save_bbox_info_in_excel(excel_path, worksheet, filename_list, 
         xmin_list, ymin_list, xmax_list, ymax_list, conf_list, class_bbox_list, area_bbox_list):
  app = xw.App(visible = True,add_book = False)  
  workbook = app.books.open(excel_path)
  worksheet = workbook.sheets(worksheet)
 
  worksheet.range('A1').options(transpose=True).value = "filename"
  worksheet.range('B1').options(transpose=True).value = "xmin"
  worksheet.range('C1').options(transpose=True).value = "ymin"
  worksheet.range('D1').options(transpose=True).value = "xmax"
  worksheet.range('E1').options(transpose=True).value = "ymax"
  worksheet.range('F1').options(transpose=True).value = "conf"
  worksheet.range('G1').options(transpose=True).value = "class_bbox"
  worksheet.range('H1').options(transpose=True).value = "area_bbox"

  
  j = 2

  
  for i in range(len(filename_list)):
      worksheet.range('A'+str(j)).options(transpose=True).value = filename_list[i]
      worksheet.range('B'+str(j)).options(transpose=True).value = xmin_list[i]
      worksheet.range('C'+str(j)).options(transpose=True).value = ymin_list[i]
      worksheet.range('D'+str(j)).options(transpose=True).value = xmax_list[i]
      worksheet.range('E'+str(j)).options(transpose=True).value = ymax_list[i]
      worksheet.range('F'+str(j)).options(transpose=True).value = conf_list[i]
      worksheet.range('G'+str(j)).options(transpose=True).value = class_bbox_list[i]
      worksheet.range('H'+str(j)).options(transpose=True).value = area_bbox_list[i]
      
      j+=1

  workbook.save(excel_path)
  workbook.close()
  app.quit()


def save_num__bbox_in_excel(excel_path, worksheet, filename_list, 
                            num_classes, num_0_list, num_1_list, num_2_list
         ):
  app = xw.App(visible = True,add_book = False)  
  workbook = app.books.open(excel_path)
  worksheet = workbook.sheets(worksheet)
 
  if num_classes == 3:
    worksheet.range('A1').options(transpose=True).value = "filename"
    worksheet.range('B1').options(transpose=True).value = "num_0"
    worksheet.range('C1').options(transpose=True).value = "num_1"
    worksheet.range('D1').options(transpose=True).value = "num_2"
     
    j = 2

  
    for i in range(len(filename_list)):
      worksheet.range('A'+str(j)).options(transpose=True).value = filename_list[i]
      worksheet.range('B'+str(j)).options(transpose=True).value = num_0_list[i]
      worksheet.range('C'+str(j)).options(transpose=True).value = num_1_list[i]
      worksheet.range('D'+str(j)).options(transpose=True).value = num_2_list[i]


      
      j+=1

    workbook.save(excel_path)
    workbook.close()
    app.quit()


