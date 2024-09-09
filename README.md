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
  
   - ![Setting Tab](documentation/setting.png)