# PENNY'S SALES DATA PREDICTION PROGRAMMING
This Python program automates the process of predicting and managing yearly sales data for Penny's store. By integrating with Google Sheets, the program allows the user to input sales data for six different product categories and predict future sales based on a small random variance. The historical sales data for products like Jeans, Trousers, Shoes, Perfumes, Polo, and Knickers is tracked in a Google Sheets worksheet. The program updates this worksheet by adding new sales predictions, which are generated using historical data and random variations.
 Here is the link to Love Sandwish-heroku where employee details are entered [link](https://sales-prediction-f352ba78f145.herokuapp.com/)

  ![Penny's Sales Data Prediction Programming](Documentation/front-page.png)

  ## How to access Penny's Sales Data Prediction Programming:
- Enter the [link](https://sales-prediction-f352ba78f145.herokuapp.com/) alternatively you can also copy the link: `https://sales-prediction-f352ba78f145.herokuapp.com/` and paste it in the browser.
- Wait for the page to load and then you click 'RUN PROGRAM'.
- Choose from the options displayed.
1. Enter your sales Data
2. Automatically, the google sales worksheet for next year will be updated effectively statrting from the year 2020.
3. The program will ask you if you want to predict the sales for next year.
4. Press YES to continue with the sales prediction for next year.
5. press No to Exit the program.


## Users experience

#### To provide the perfect user experience and features for Penny's store statistics app, we need to focus on key elements like simplicity, user guidance, predictive insights, and visualization. Here's an enhanced version of your current app's user experience (UX) and feature set:
- As a user, a welcoming Introduction: When the app starts, give the user a clear overview of what they can do with the app (e.g., predict sales, view past statistics).
- Data Input Help: If the user enters incorrect data, provide specific, helpful error messages. Use color highlights to distinguish between errors and successful inputs (e.g., invalid input in red, successful in green).
- Error Handling for Incorrect Inputs: After a failed validation, guide the user on how to correct the input.
- Immediate Validation: After input, validate the data immediately and highlight success in green, errors in red.
- an error occures if not enough values or if non-numeric values are provided.
- How to exit the program once the valid details has been entered.


## Features

 **When the program is loaded**

- The user will be ushered in with a welcoming message.
- A statement which says you should enter the sales data to precict the next year sales is also displayed.
- An example of the kind and amount of data you should input is displayed 
- if the right combination is inputed a predictive data is generated for 2020, using random variance.
- The data arrays generated will be automatically explained what each data means.
- The data is automatically updated on the google sheet
- The program will ask the users if they still want to predict sales for next year.
- if the user says YES, it automatically predict the next year input and if the user input a NO statement, it exit the program.

![welcome-message](Documentation/welcome-message.png)

The user is expected to input the correct six digit numbers, seperated with commas in other to predict the sales for next year.

**When the user Input the right combination**
- The sales for next year combination will be predicted, starting from the year 2020

![user-input](Documentation/user-input.png)

**When the user enters invalid sales data for prediction**
- When the user enters details that is not equal to six, the user will see an error message and a provision to re-enter sales data to predict the next year sales.
- If the user also enteres an incorrect data, a helpful error messages use color highlights to distinguish between errors and successful input.
- After a failed validation, the code direct the users on how to correct the input.

![invalid-data](Documentation/invalid-data.png)


**When the user enters letters in place of data numbers or data number that are less than six**

- When the user enter letters in place of whole numbers for sales prediction, the user will see an error message and a provision to re-enter sales details for next year prediction.
- When the user enter a data less than the valid six digit, an error warning message will tell the user that they provided number less than six.

![invalid-letters](Documentation/invalid-letter.png)

**When the user enters data numbers that are greater than the valid six digit numbers**
- When the users enters a number greater than the required valid six data number, an error message will tell you that you have provided a higher amount of number.
- It will also tell the user that exactly six numbers are required to predict the next year sales.
- I t also tells the user to re-enter the right amount of combination in other to predict the next year sales

![higher-input](Documentation/highr-input.png)

**When the user enters a valid data numbers**
- When the user enters the valid combination, the predictive sales for the next year will be generated automatically.
- Immediately after the data has been generated, the program will ask you if you want to predict sales for next year.
- when the user enters `Yes`, a random number sales for next upper year will be generated, but if type `NO`you will be automatically exiting the program.

![valid-data](Documentation/valid-data.png)

## Technologies Used
### Language:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/)

### Frameworks/Libraries and Tools:
#### Python modules/packages:


##### Third-party packages:
- [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1IpXqEJz7itPXRXNqylka1a9bT0a5xhQt6_O7Q8lbk18/edit?gid=0#gid=0) for receiving data.

- [Google API](https://console.cloud.google.com/iam-admin/serviceaccounts/details/103855191815773954256?project=pennys-store-statistics-434521&supportedpurview=project) for creating Credentials.

-  [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.

#### Other tools:
- [Gitpod](https://gitpod.io/workspaces/) was used as the main tool to write and edit code.
- [GitHub](https://github.com/) was used to host the code of the website.
- [heroku.com](https://www.heroku.com/) was used for the deployment of project.
- [am i responsive](https://ui.dev/amiresponsive) was used to screenshot devices for responsive design for README purpose.

## Bugs
### Solved bugs
1. The color font text used to color print output was solved by applying `Fore and import colorama`
```
 
    print(Fore.YELLOW + f"Predicted sales for year {year}: {new_row}")
    print(Fore.YELLOW + "Sales worksheet updated successfully.\n")

     cont = input(Fore.GREEN + "Do you want to predict sales for the next year? (yes/no): ")
        if cont.lower() != 'yes':
            print(Fore.RED + "Exiting program.")
            break
```
2. The method ```  print(Fore.RED + "Exiting program.")
            break``` was not properly exiting from the program when run on pthon terminal.

      ```  print(Fore.RED + "Exiting program.")
            break
      ```
     break function was applied in other to exit from the program.             

### Unsolved Bugs

  - None.

 ## Testing
1. ### Overview

This testing report documents the functionality, accuracy, and performance of a Python program developed to predict future sales based on historical data. The predictions are made using a Google Sheets API to update and retrieve data from a Google Spreadsheet titled "pennys_store_statistics."

The program generates randomized predictive sales values for six products—jeans, trousers, shoes, perfumes, polo, and knickers—and appends the results into the spreadsheet while explaining each predicted sales number.

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

4. ### Summary
  - All features were tested successfully, and the program behaved as expected in most cases.
  - Error handling worked correctly when invalid data or network issues occurred, though improvements could be made for handling incorrect Google Sheet structures.
  - The program's integration with Google Sheets worked seamlessly, with sales predictions updating the correct worksheet in real-time.

  
### Validator

- **run.py**
 - No errors were found when passed through the official [Pep8 Python Validator](https://pep8ci.herokuapp.com/). This checking was done manually by copying python code and pasting it into the validator.
 
![Python Validator](Documentation/python-validator.png)

- Github does not show the last empty line in the file, I added a screenshot of it. The screenshot shows that the code is structured according to PEP8 requirements.

![Python Validator](Documentation/python-validator2.png)

## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).

### To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/Ebuka-martins/Pennys-store-statistics-project`

   1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

    1. Push the files to your repository with the following command:
  `git push`
  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).
  1. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):

![New Heroku App](Documentation/new-app.png)

  1. Go to Setting tab:
  
   ![Setting Tab](Documentation/settings.png)

   
   - Scroll to Config Var and click Reveal Config Var.

  ![Config Var](Documentation/config-var.png)

   - Type CREDS into the "KEY" area and copy your CREDS file content from your workspace and paste it into the "VALUE" area. Then click "ADD".
   
  ![Creds Tab](Documentation/creds.png)

  - Scroll to Buildpacks and click Add buildpacks.

     ![Build pack1](Documentation/buildpacks-1.png)

     - Add heroku and nodejs buildpacks, making sure that python comes first and nodejs underneath.

     ![Build pack2](Documentation/buildpacks-2.png)
  
2. Go to the Deploy tab:
     
     ![Build pack2](Documentation/dep.png) 


     - click GitHub and connect to GitHub. Key in your repository name, click search and then connect.

     ![Deployment](Documentation/deployment-method.png) 

  
    ![Deployment](Documentation/depo.png) 

    - Scroll to Manual deploy and click Deploy Branch.
   
    ![Deployment](Documentation/deploy-branch.png) 

    
    - Wait for the completion of the deployment.

     ![Deployment](Documentation/deploying-branch.png) 

     
    - Click "View" to launch the application inside a web page.

     ![Deployment](Documentation/view-button.png) 

 ## Credits

   - Heroku for hosting the application: [heroku.com](https://www.heroku.com/)

   -  Color formatting: [Colorama](https://pypi.org/project/colorama/).

   - Love Sandwish: [Code-Institute](https://codeinstitute.net/).

   - GitHub for hosting the code of the website [GitHub](https://github.com/).

   -  Terminal menu: [Simple Terminal Menu](https://pypi.org/project/simple-term-menu/).

## Acknowledgements
- I give Special thanks to my wife Precious Chidimma, my brother John Paul and my parents who has been a great support to me all through this project.
 - [Vernell Clark](https://github.com/VCGithubCode) is my friend and he has been a great support to me throughout this project.
 - [Jubril Akolade](https://github.com/Jubrillionaire) was a great mentor to me throughout this project.
 -  [Code Institute](https://codeinstitute.net/) tutors and Slack community members for their support and help.
 -  [Love Sandwish](https://codeinstitute.net/) tutors and Slack community members for their support and help.
 - [Ovundiano](https://github.com/Ovundiano) was also my friend who has been very supportive to me throughout this project.

 







