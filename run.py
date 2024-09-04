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
    """
    print("please enter the sales data to predict the next year sales")
    print("Data should be six numbers, seperated by commas.")
    print("Example: 24,34,40,52,63,71")

    data_str = input("Enter your data here: ")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    In the try syntax convert strings into intergers.
    Raises ValueError if strings cannot be converted into int.
    or if they are not exactly 6 values.

    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required to predict the next year sales, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")        
            
     
   
get_sales_data()    
