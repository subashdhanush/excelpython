from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Inputs"

ws.append(["Field", "Value"])  # Header

name = input("Enter name: ")
age = input("Enter age: ")
role = input("Enter role: ")

ws.append(["Name", name])
ws.append(["Age", age])
ws.append(["Role", role])

wb.save("output.xlsx")
print("Excel file created!")



# pip install openpyxl
