import pyexcel

book = pyexcel.get_book(file_name= r'C:\Users\raja6\Desktop\study\emc python training\hosts.xlsx')

for sheet in book:
    if sheet.name == 'Sheet1':
        print(sheet.name)

        for row in sheet:
            print(row)

