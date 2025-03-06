# Harvest

## About

 Harvest is a platform for content creators passionate about sharing the best local finds in Brighton and the surround areas.
 It enables users to share local insights, discover unique experiences, and contribute to a growing community of culture enthusiasts.It provides features for users to sign up to the platform to add articles and related events that are happening in Brighton and parts of East Sussex.

### Target Users

Harvest is designed for people of all ages who are passionate about exploring and sharing cultural experiences. This project was developed as a Full Stack web application, utilizing Python, Django, HTML, CSS, and JavaScript to ensure scalability and maintainability. 
The development process incorporates deployment strategies and follows Agile methodologies to enhance the application's stability and performance.

 # Features

- Index page
    -  The site visitor can read free articles from the front page, to sample the articles before registering to the Harvest Platform.

- Register page
    - An entry for your email, first name, last name and password is included for user registration.
    - Password validation is utilised to ensure that the password is secure. This is integrated with Crispy forms.

- Creator Dashboard
    - Here you can create article, view published articles, manage your account and logout.
    - In the navigation menu 
    - - Dashboard - the user arrives at the front page of the dashboard.
    - - Create article - allows creator (users) to create and publish and article. They can add the title and content.
    - - Upload Image - Image png, jpegs and webp can be uploaded to be displayed in the article above the text.
    - - Published - Allows creator (users) to see the article that has been published.  In addition, they can update and delete articles from the published page.
    - - Manage account 
        - Users can update their account details; First Name, Last Name and Email.
        - Users can delete their account /cancel their subscription.  
    - - Logout
        - The creator (user) can log out of the Creator Dashboard.

- General User Dashboard
    - In the navigation menu
    - - Dashboard - the user arrives at the front page of the dashboard.
    - - View article - allows registered users to view published articles.
    - - Manage account 
        - Users can update their account details; first name, last name and email.
        - Users can delete their account/cancel their subscription.  
     - Logout
        - The user can log out of the General Dashboard.    

- Color Palette 
   ![Image of Console](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/colorpalette.png)
   

## Technologies Used

  - Backend: Python 3.13, Django 4.2
  - Frontend: HTML, CSS (Bootstrap 5), JavaScript
  - Database: PostgreSQL 
  - Tools: Git, GitHub, Heroku, VS Code
  - Testing: Flake8 and and Black to adhere to PEP 8 standards.
 
 ### Original Custom Models:

  - The project includes two custom models . An Account model and Creator model.
    - - In the Account model (account/models.py) The CustomUser model is a custom implementation of Django's user authentication system. It replaces the default user model and is responsible for managing authentication and user attributes.
    - - The Article model represents content created by users. Each article belongs to a specific user and may include optional event-related content, which can be rendered below the article upon creation.
 

   ![Daily Entries worksheet](https://)
    Entries Worksheet


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
 