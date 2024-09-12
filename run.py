
import gspread
from google.oauth2.service_account import Credentials

# Define Google Sheets API scope and credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('car_parts_sale')


def get_sales_data():
    """
    Get sales figures input from the user for car parts.
    Data should be three numbers: oil, oil filter, and tyres.
    """
    while True:
        print("Please enter sales data for the car parts.")
        print("Data should be three numbers, separated by commas.")
        print("Example: 10,20,30 for oil, oil filter, tyres\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Validates that input data contains exactly 3 values are integers.
    """
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(f"Exactly 3 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True