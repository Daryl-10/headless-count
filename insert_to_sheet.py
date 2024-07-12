from Google import *
import time


def insert_to_sheets(date_value, count_value):

    CLIENT_SECRET_FILE = 'client_secrets.json'
    API_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    spreadsheet_id = ''

    """
    Append Values
    """

    worksheet_name = 'All'
    cell_range_insert = 'A1'

    print("Date provided: ", date_value)
    print("count provided: ", count_value)

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)


    values = ((date_value, count_value,  current_time), ())
    
    print("Hence, values = ", values)

    value_range_body = {
        'majorDimension': 'ROWS',
        'values': values
    }

    service.spreadsheets().values().append(
        spreadsheetId = spreadsheet_id ,
        valueInputOption='USER_ENTERED',
        range=worksheet_name + '!' + cell_range_insert ,
        body = value_range_body
    ).execute()