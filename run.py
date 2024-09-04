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
    print(f"The data provided is {data_str}")

get_sales_data()    
