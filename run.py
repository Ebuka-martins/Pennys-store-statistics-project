import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pennys_store_statistics')
   

def get_sales_data():
    """
    Predict sales figures input from the users to get the perfect sales for the next year each
    Adding a while loop to collect data from the users and predict the future sales for next year
    """
    while True:
        print("please enter the sales data to predict the next year sales")
        print("Data should be six numbers, seperated by commas.")
        print("Example: 24,34,40,52,63,71\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")
        
        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data      


def validate_data(values):
    """
    In the try syntax convert strings into intergers.
    Raises ValueError if strings cannot be converted into int.
    or if they are not exactly 6 values.

    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required to predict the next year sales, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False    

    return True      

def predict_sales_worksheet(data):
    """
    predict sales worksheet for next year, add new row with the list data provided  
    """      
    print("predict sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales_worksheet predicted successfull.\n")
            

data = get_sales_data()   
sales_data = [int(num) for num in data]
predict_sales_worksheet(sales_data)
