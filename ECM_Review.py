import csv
import os

print('starting')

#print('Enter file path')
#excel_file_path = '+input()+

excel_file_path = r'C:\Users\ben01822\Desktop\All.csv'
with open(excel_file_path, 'r') as file:
    rows = list(csv.reader(file))

print('file located')  

print('Enter reviewer name')
reviewerName = input()

#define logic for updating fields
for row in rows:
    if 'Changed Properties' in row[13] and row[15] == 'TJXASVC_BI_COGNOS_SC' or row[15] == 'TJXASVC-BI-MOTIO-PR':
        row[30] = 'Service Account Changed Properties'

    elif 'Initial Version' in row[13] and row[15] == 'MotioCI':
        row[30] = 'Normal Activity - MotioCI Initial Version'
        
    elif 'Initial Version' in row[13] and row[15] == 'TJXASVC_BI_COGNOS_SC' or row[15] == 'TJXASVC-BI-MOTIO-PR':
        row[30] = 'Normal Activity - Service Account Initial Version'

    elif 'Changed Properties' in row[13] and row[15] == 'MotioCI':
        row[30] = 'Normal Activity - MotioCI Changed Properties'
   
    elif 'Promoted' in row[13]:
        row[30] = 'assign chg/inc - manual review'

    else:
        row[30] = 'user change - manual review'
    row[29]= 'A'
    row[28]= reviewerName
print('file updated')    
#post data and save file
edited_excel_file_path = r'C:\Users\ben01822\Desktop\All.csv'
with open(excel_file_path, 'w', newline='', encoding= 'utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
print('file saved')

print('done')
