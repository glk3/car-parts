
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

def update_worksheet(data, worksheet):
    """
    Updates the relevant worksheet with the provided data.
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully.\n")

def calculate_returned_data(sales_row):
    """
    Compare sales with ordered and calculate the returned
    """
    print("Calculating returned data...\n")
    ordered = SHEET.worksheet("ordered").get_all_values()
    ordered_row = ordered[-1]
    returned_data = []
    for ordered, sales in zip(ordered_row, sales_row):
        returned = int(ordered) - sales
        returned_data.append(returned)

    return returned_data

def main():

    data = get_sales_data()
    sales_data = [int(num) for num in data]  # Convert input to integers
    update_worksheet(sales_data, "sales")  # Update sales worksheet

print("Welcome to Car Parts Sale Data Management")
main()