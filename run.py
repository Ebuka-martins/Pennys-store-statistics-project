import gspread
from google.oauth2.service_account import Credentials
import random


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
    Collect sales data input from the user to get the base sales for the next year prediction.
    """
    while True:
        print("Welcome to Penny's Sales Data Prediction Programming")
        print("Please enter the sales data to predict the next year sales.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 24,34,40,52,63,71\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

    return sales_data


def validate_data(values):
    """
    Validates that exactly 6 numeric values are entered by the user.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
               "Exactly 6 values required to predict the next year sales, "
                f"you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def generate_random_sales(sales_data):
    """
    Generates random sales predictions by adding a small variance to the provided sales data.
    The variance is between -10% and +10% for each sales number.
    """
    predicted_sales = []
    for sale in sales_data:
        sale = int(sale)
        variance = random.uniform(-0.10, 0.10)  
        new_value = int(sale + sale * variance)
        predicted_sales.append(new_value)
    
    return predicted_sales


def predict_sales_for_year(year, data):
    """
    Predict the sales for the specific year, adding a new row with the year
    and predicted sales data.   
    """
    print(f"Predicting sales for year {year}...\n")
    
    
    sales_worksheet = SHEET.worksheet("sales")
    
    # Generate predicted sales data
    predicted_sales = generate_random_sales(data)
    
    # Combine the year with the predicted sales data
    new_row = [year] + predicted_sales
    
    # Append the new row to the worksheet
    sales_worksheet.append_row(new_row)
    
    print(f"Predicted sales for year {year}: {new_row}")
    print("Sales worksheet updated successfully.\n")



if __name__ == "__main__":
    # Initialize the starting year
    year = 2020
    
    while True:
        data = get_sales_data()
        sales_data = [int(num) for num in data]  
        predict_sales_for_year(year, sales_data)
        
        # Increment the year for the next prediction
        year += 1
        
        # Ask if the user wants to continue
        cont = input("Do you want to predict sales for the next year? (yes/no): ")
        if cont.lower() != 'yes':
            print("Exiting program.")
        break
