## Testing
1. ### Overview

This testing report documents the functionality, accuracy, and performance of a Python program developed to predict future sales based on historical data. The predictions are made using a Google Sheets API to update and retrieve data from a Google Spreadsheet titled "pennys_store_statistics."

The program generates randomized predictive sales values for six products—jeans, trousers, shoes, perfumes, polo, and knickers—and appends the results into the spreadsheet while explaining each predicted sales number.

The deployed project live link is [HERE](https://sales-prediction-f352ba78f145.herokuapp.com/)- ***Use Ctrl (Cmd) and click to open in a new window.*** 

2. ### Environmental setup
- Programming Language: Python 3.x
- External Libraries Used:
 
  - `gsprad`  (Google Sheets API integration)
  - `google.oauth2.service_account.Credentials` (OAuth 2.0 for Google APIs)
  - `random` (for generating sales predictions)
  - `colorama` (for colored terminal output)
- Google Sheets Setup:
  - The "pennys_store_statistics" spreadsheet must have a worksheet named "sales" with pre-existing historical data and a structure where the first column is the year, and subsequent columns represent sales of six products (jeans, trousers, shoes, perfumes, polo, knickers).

  ### sample historical data:

  | **Year** | **jeans** | **Trousers** | **Shoes** | **Perfumes** | **Polo** | **Knickers**|
  |----------|-----------|--------------|-----------|--------------|----------|-------------|
  |  2015   |   24      |      36      |     16    |      31      |     30   |      26     |
  |  2016   |   22      |      32      |     35    |      29      |     30   |      33     |
  |  2017   |   34      |      28      |     33    |      19      |     23   |      18     |
  |  2018   |   27      |      36      |     31    |      24      |     19   |      25     |
  |  2019   |   29      |      28      |     27    |      26      |     23   |      28     |


3. ### Testing Procedure
 - #### Test Case 1: Validate Data Input
   Objective: Ensure the program accepts valid sales data in the correct format and rejects invalid data.

   #### Steps:
   1. Run the program and enter valid sales data(e.g, `24,34,40,52,63,71`)
   2. Enter invalid data (e.g, `24,34,xyz,52,` or too few/many values.)

   #### Results:
   - Valid data: The program accepted the input and confirmed the data is valid.
   - Invalid data: The program provided appropriate error messages and requested valid input.

 - #### Test Case 2: Generate Random Sales Predictive 
   Objective: Ensure the random sales generation falls within the specified range (±10% variance).

   #### Steps:
    1. Provide sales data (e.g, `[24,34,40,52,63,71]`).
    2. The program generates predictive values with random variance for each item.

   #### Result:
    - Predictive values adhered to the ±10% variance, calculated correctly.

   #### Example:
    - Input `[24,34,40,52,63,71]`
    - Predicted output: `[26,32,36,47,68,78]` (values vary between -10% and +10%)   

 - #### Test Case 3: Update Google Sheets
    Objective: Ensure that each prediction is correctly appended to the Google Sheets "sales" worksheet.

   #### Steps:
   1. Run the prediction for year 2021.
   2. Verify that the newly predicted values are appended to the worksheet.

   #### Results:
   - The program successfully appended the predictions to the Google Sheet.    

 - #### Output Explanation
   - Ensure the program explains each prediction in a user-friendly manner.

   #### Steps:
   - Run the program and verify that explanations for each sales number appear as expected.

   #### Results:
   - The program correctly printed the explanations.
   

Here is also a tabular representation of the **Features**, **Action**, **Expected Results**, and **Actual Result**.
| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Data Input Validation | Enter valid sales data (`e.g., 24,34,40,52,63,71`) | The program accepts the inputand confirms the data is valid | The program accepted the valid input and confirmed `it is valid` |
| Data Input Validation (Invalid) | Enter invalid sales data (`e.g., 24,34,xyz,52` or too few/many values) | The program rejects the invalid input and requests the user to re-enter the data, displaying a relevant error message | The program provided appropriate error messages and prompted for valid input | 
| Random Sales Generation | Run the program with valid input (`e.g., 24,34,40,52,63,71`)  | The program generates predictive sales values with random variance (±10% of the original values). | The program successfully generated predictive sales values within the specified variance. |
| Google Sheets Update | Predict sales for a year (e.g., 2020) and check Google Sheets | The program appends the predicted sales data for the year to the Google Sheets worksheet in the correct format. | The program successfully appended the prediction for the year to the Google Sheets worksheet. |
| Yearly Increment | User inputs symbol or number | Error message appears | Works as expected |
| Name input | Run the program in a loop (with valid data) | The program increments the year with each iteration (e.g., from 2020 to 2021, 2022, etc.) and correctly predicts sales for the incremented year | The program successfully increments the year and generates the predicted values for the next year. |
| Sales Explanation | Run the program with valid input (`e.g., 24,34,40,52,63,71`) | The program prints an explanation of the sales prediction for each product (e.g., "The sales for jeans is 26") | The program correctly displayed explanations for each sales prediction. |
| User Control (Continue/Exit) | After each prediction, choose to continue (`yes`) or exit (`no`) | The program either proceeds to the next year prediction if the user enters `yes` or exits if the users enters `no`. | The program correctly continued or exited based on the user input. |
| Error Handling for Network/Sheet Issues | Disconnect network or use an invalid Google API credentials file | The program displays an error message indicating it could not connect to the Google Sheets API or could not access the Google Sheets file. | The program raised an appropriate error when the network or credentials were invalid. |
 | Colored Output (via colorama) | Run the program and observe terminal output | The terminal output is color-coded to enhance user experience (e.g., sales explanations in cyan, warnings/errors in red, predictions in yellow). | The terminal output displayed colored text as expected using the `colorama` package. |  
| Sales Variance Control | Observe the variance in predicted sales values | The program adds or subtracts up to 10% of the original value to generate predicted sales data. | Variance applied as expected; predicted sales varied by ±10% from the original values. |
| Handling Empty or Malformed Spreadsheet | Run the program on a malformed Google Sheet (e.g., missing columns) | The program either appends data correctly if the structure matches, or raises an error if the worksheet does not meet the expected structure (year, jeans, trousers, etc.). | The program encountered errors if the Google Sheet was not correctly structured. Proper structure is required.
 |    
 ### 4. Summary
  - All features were tested successfully, and the program behaved as expected in most cases.
  - Error handling worked correctly when invalid data or network issues occurred, though improvements could be made for handling incorrect Google Sheet structures.
  - The program's integration with Google Sheets worked seamlessly, with sales predictions updating the correct worksheet in real-time.