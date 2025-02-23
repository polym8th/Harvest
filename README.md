# Harvest

## About

Harvest is a web application for content creators passionate about sharing the best local finds in Brighton and London. From hidden cafés to scenic trails and unique shops, Harvest curates authentic, high-quality recommendations from local voices.

### Target Users

Harvest - Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McC

 # How to Use Harvest

- Lorem Ipsum 
    -  is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to ma
    -  But also the leap into electronic typesetting, remaining essentially unchanged. It was popularised i

- Why do we use it?
    - It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like re
    - scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essential 
    - This option allows you to override the default macronutrient goals with custom values.

- View Daily Goal Analysis:
    - Select option 3 to review your daily goal analysis.
    - The console will display a percentage calculation showing how much of your daily goals have been met based on your food entries.

- Calculate Weekly Totals:
    - Select option 4 - Calorie Mind will calculate and display the total values for Calories, Protein, and Fat over the last seven days, helping you track your progress and adjust your diet if needed.

# Features

   ![Image of Console](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/console.png)
   

## Existing Features

Harvest It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Co

1 - Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney C
  - The app allows the user to select n (no) or y (yes) when the user is asked "Do you know the calorie and macronutrient values? If nutritional information is unknown, the application initiates an API request to retrieve accurate values (calories, protein, fat, and carbs). 

  - Roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sy

  - Daily food calorie and macronutrient intakes are logged into the designated worksheet: Entries.

2 - Record New Daily Goals  

  - Set daily macronutrient targets for protein, fat, and carbs. This feature helps you stay aligned with your nutrition goals and maintain a balanced diet.

  - This function allows users to input new daily goals and replace them with custom values.

      The application is pre-configured with the following default daily macronutrient targets:   
         
     -   protein goal = 100

     -   fat goal = 70
         
     -   carbs goal = 200

     - New daily food calorie and macronutrient goals are logged into the designated Google worksheet: Goal.

3 - Review Your Daily Goal's Analysis  

  - Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor a
   
  - The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32

     i.e,. this is the percentage calculation: 

      -   Protein: (34 / 100) * 100 = 34%
      -   Fat: (4 / 70) * 100 = 5.71%                 
      -   Carbs: (45 / 200) * 100 = 22.5%

  - These calculations help create a logical nutrition plan, whether it’s for weight loss, muscle gain, or maintaining a healthy diet. Calorie Mind is not merely about weight loss.


4 - Calculate Weekly Totals

  - Track your weekly progress by calculating the total calories, protein, and fat consumed over the last seven days.

  - The gspread library retrieves the last 7 entries from Google Sheet for a weekly data analysis. Each entry is recorded with a timestamp, which is used to identify and access the relevant data from the "Week Total" sheet. This functionality enables the accurate calculation of the weekly totals, providing a clear overview of weekly progress. 

  -  Weekly totals are displayed on the console.

  -  Weekly totals are logged into the designated Google worksheet: Week Total.

5 - q for Quit

  - Quit the program at any time by selecting' q'. The program exits.
    A message is printed to the console: "Great job! You've successfully logged all your calories for the day!"    

 
 ### Additional notes: 

  Use of Libraries

  - The gspread library manages API communication with Google Sheets, while google-auth handles authentication to ensure secure access to the spreadsheet data.

  - Google Sheets acts as a lightweight cloud-based database, allowing seamless data storage, updates, and retrieval from designated worksheets.
 
   
   ![Daily Entries worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/entries.png)
    Entries Worksheet

   ![Daily Goals worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/goals.png)
    Goals Worksheet

   ![Weekly Totals worksheet](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/weeklytotals.png)    
    Weekly Totals Worksheet

### Google Sheets Link

- Please click on this link to view the Google worksheets and Entries, Goal and Worktotal sheets:
  https://docs.google.com/spreadsheets/d/1AolucGwHaHIfdgWZprr5FXCtpJqEvPUGCzdBgGhvJrc/edit?usp=sharing. Access is granted with this link.

### Basic UX Design: 

  - Improved console output readability by adding line spacing for clearer print results.

## Future Features

  - Add a GUI interface and upgrade from a mock terminal.
  - Expand Weekly Totals features to alert users if they skipped a day. It currently calculates the last seven days.
  - Add a leaderboard on scores once the GUI is designed and implemented.

## Flowchart

![Flowchart](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/flowchart.png)

# Testing

## Manual Testing

| Test Case                         | Expected Result                                                                     | Test Result |
|-----------------------------------|-----------------------------------------------------------------------              |-------------|
| Run program                       | Click run program.  The app will appear with a multiple choice selection.           | ✅ PASS          |
| Prompt user input                 | Prompt user to enter a food item.                                                   | ✅ PASS          |
| Prompt user input                 | Prompt user to select if they know the macronutrient values. Select n (no) or y (yes).    | ✅ PASS          |
| User input 'y' (y)                | Prompt user to enter their protein, fat and carbs.                                  | ✅ PASS          |
| User input 'n' (no)               | Retrieve API from Calorie Ninjas.                                                   | ✅ PASS          |
| Outputs results to console        | Outputs daily nutrients result to console.                                          | ✅ PASS          |
| Daily nutrients appends worksheet | User inputs daily nutrients, which are appended to the 'Entries' worksheet.         | ✅ PASS          |
| Handles invalid input data        | If the API does not recognize a food item, the app displays the message: 'Food item not recognized'.                                                                                                                                       | ✅ PASS          |
| Select option 2                   | Prompt user to input your daily target goals for Protein, Fat, and Carbs.                | ✅ PASS          |
| No user input detected            | The console will display a message "No entry has been made yet"                     | ✅ PASS          |
| Handles invalid input data        | Prompt the user to input a nutrient value, validate it as a non-negative integer (round number).                         | ✅ PASS  
| Daily goals appends to worksheet  | Default goals added to worksheet if there are no new daily goal entries (option 2). | ✅ PASS          |
| Daily goals appends to worksheet  | User inputs new goals, which are appended to the 'Goal' worksheet.                  | ✅ PASS          |
| Select option 3                   | The console will display a percentage calculation showing how much of your daily goals have been met based on food entries.                                                                                                                  | ✅ PASS          |
| Select option 4                   | Calculates weekly totals of calories and macronutrients. Retrieves from Google worksheet and sums up the last 7 entries.    | ✅ PASS          |
| Outputs results to console        | Outputs weekly totals result to console.                                            | ✅ PASS          |
| Weekly totals appends to worksheet| User inputs option 4. Weekly totals appends to worksheet 'Week Totals'.             | ✅ PASS          |
| Handles invalid input data        | Identifies empty or invalid non-numeric entries in Google worksheet columns.        | ✅ PASS          |
| Select q                          | Select q for quit. Exits mock terminal program.                                     | ✅ PASS          |


   ![Calorie and Macronutrient entries](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/usertesting.png)
   
## Bugs/Updates after Testing

At the beginning of coding the app, I ran into some bugs. The following bugs I encountered are as follows:

- Indentation Fixes: Corrected indentation issues, especially in the calculate_goal_percentage method.

- Issue: Previously, the application would throw an error when the API could not find a specified food item. 
  
  Solution: Added exception handling to manage cases where the API does not recognize the food item or if there’s invalid input. Now, when this occurs, the application catches the error and prints a helpful message— “Food item not recognised” to the console. 

- Issue: The application would reset to the main menu if users entered non-integer values, such as decimals, letters, or special characters. 

  Solution: Add a conditional check to handle invalid user input. Prompt the user to enter a nutrient value, validate it as a non-negative integer, and skip returning to the main menu.

-  A bug was identified where the value 0 was incorrectly rejected as valid input for nutrient values. To resolve this, a new function, 'get_nutrient_input', has been    implemented. This function enforces input validation by ensuring the provided value is a non-negative integer, specifically allowing both 0 and positive integers as valid inputs.

   The screenshot below (Figure 1.0) demonstrates the issue where the value 0 was not accepted. This bug has been resolved in the current implementation.

Figure 1.0 
  ![Bug fix](https://github.com/IsaHu-dev/Calorie-Mind/blob/main/media/roundnumber.png)


- Issue: At the end of the project, the application threw an error when there were empty columns in Google worksheets.

  Solution: In the calculate_weekly_totals function, a validation step is added to ensure only numeric values are summed.

All bugs are presently fixed.

## Code Style and Readability

- The code is formatted with the Black Python Formatter to maintain consistent code style and readability.

## Validator Testing

- Passed the CI Python Linter. "All clear no errors found"



# Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

The steps for deployment are as follows:

- Create a new Heroku app
- Set the build packs to Python and NodeJS in that order
- Link the Heroku app to the Github repository 'Calorie Mind'
- Click on Deploy

## Credits 

  - The python code for the app Calorie Mind was refactored to adopt an object-oriented approach. I sourced this youtube tutorial and used it as a rough guide: https://www.youtube.com/watch?v=0-LDsQpKYFU

  - [Real Python](https://realpython.com/.com/)
  - [Stack Overflow](https://stackoverflow.com/questions/10004850/python-classes-and-oop-basics)
  - [w3schools - Python](https://www.w3schools.com/python/ref_string_isdigit.asp)

 ## Code Attribution

  - There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of 

  ![Code Attribution](####)

  ## Acknowledgements
 