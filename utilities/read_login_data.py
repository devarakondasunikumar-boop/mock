from openpyxl import load_workbook


def read_data():
    workbook = load_workbook("/mock1/test_data//flight_data.xlsx")
    worksheet = workbook.active

    from_city = sheet["A2"].value
    to_city = sheet["B2"].value

    workbook.close()
    return from_city, to_city