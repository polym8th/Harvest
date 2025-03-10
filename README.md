# Harvest

## About

 Harvest is a platform for content creators passionate about sharing the best local finds in Brighton and the surround areas.
 It enables users to share local insights, discover unique experiences, and contribute to a growing community of culture enthusiasts.It provides features for users to sign up to the platform to add articles and related events that are happening in Brighton and parts of East Sussex.

### Target Users

Harvest is designed for people of all ages who are passionate about exploring and sharing cultural experiences in the local area of Brighton. This project was developed as a Full Stack web application, utilizing Python, Django, HTML, CSS, and JavaScript to ensure scalability and maintainability. 
The development process incorporates deployment strategies and follows Agile methodologies to enhance the web application's stability and performance.

### Features

- Index page
    -  The site visitor can read free articles from the front page, to sample the articles before registering to the Harvest Platform.

- Register page
    - An entry for your email, first name, last name and password is included for user registration.
    - Password validation is utilised to ensure that the password is secure. This is integrated with Crispy forms.

- Creator Dashboard
    - Here you can create article, view published articles, manage your account and logout.
    - In the navigation menu 
    -  Dashboard - the user arrives at the front page of the dashboard.
    -  Create article - allows creator (users) to create and publish and article. They can add the title and content.
    -  Upload Image - Image png, jpegs and webp can be uploaded to be displayed in the article above the text.
    -  Published - Allows creator (users) to see the article that has been published.  In addition, they can update and delete articles from the published page. The article is identified to the user who created it, so they have access privileges to delete the article they created only. A Superuser can delete and update all articles. 
    -  Manage account 
        - Users can update their account details; First Name, Last Name and Email.
        - Users can delete their account / cancel their subscription.  
    -  Logout
        - The creator (user) can log out of the Creator Dashboard.

- General User Dashboard
    - In the navigation menu
    -  Dashboard - the user arrives at the front page of the dashboard.
    -  View article - allows registered users to view published articles.
    -  Manage account 
        - Users can update their account details; first name, last name and email.
        - Users can delete their account/cancel their subscription.  
     - Logout
        - The user can log out of the General Dashboard.    

### UX WireFrames
  
   Index Page

  ![Index Page](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/indexpage_rm.png)

  Registration Page

  ![Register Page](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/register_rm.png)

  User (General) Dashboard
  
  ![User Dashboard](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/generaluser_rm.png)

  Creator Dashboard - Create Article Page 

  ![Creator Dashboard](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/generaluser_rm.png)

  Creator Dashboard - Published Articles Page

  ![Creator Dashboard](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/publishedarticles_rm.png)

## Agile Framework and Project Management

  - To keep the project organized, I used an Agile workflow with GitHub Projects and Issues.
  - User Stories & Acceptance Criteria - Each feature was decomposed into User Stories with clearly defined Acceptance Criteria, maintaining the main objectives and usability.
  - Task Prioritization:  Issues were categorized using labels to establish development priorities; such as Must-Have, User Story or Implementing a new user authentication system.
  - Kanban Workflow - A three-stage Kanban board was utilized for task management: 
    -  To Do – Newly created tasks pending development. 
    -  In Progress – Tasks actively being developed. 
    -  Done – Completed and verified tasks, ready for deployment.

#### User Stories
   The following sections outline user stories and their acceptance criterias. These demonstrate how the application fulfills user requirements and delivers front-end CRUD functionality.

#### As a Visitor (Unregistered User)
Acceptance criteria:
- **Browsing Content** – As a visitor, I want to browse free articles on the index page, so that I can explore what the platform offers before registering an account.
- As a user, I want to see a navigation bar so I can navigate to the register button to sign up for an account and access new articles.
- As a user, I want to receive a password sent to my email so that I can log in to my account.

#### As a User (Logged-in User)
- As a registered user, I want to access exclusive articles.
- As a registered user, I want the option to pay for a premium account with access to exclusive articles and events.

#### Access the Dashboard to Manage User Account
- As a registered logged-in user, I want to access the dashboard and manage my account.
- As a registered logged-in user, I want to access exclusive articles.

#### Create an Article
- Given that I am a Creator (registered user) and declared that I am a creator by checking the box.
- When I provide a title and content.
- Then I should be able to submit the article successfully, and it should be saved in the system with a date stamp.

#### Delete an Article
   - **As a Creator (registered user)**, I want to delete my own articles so that I can remove outdated or unnecessary content.
   - **Given** that I have registered as a content creator user.
   - **Given** that I am a Creator (registered user) – I have privileges to delete only the articles that I created.

   -  More User stories to be found directly on Github: 
    For detailed user stories, refer to the **[Harvest User Stories](https://github.com/IsaHu-dev/Harvest/issues)**.

#### UX Design - Color Palette

  The Harvest platform has a calm and modern design with soft, muted colors that are easy on the eyes. Instead of using bright colors, the visual focus is on article images, content, and button styling to create a smooth and relaxing user experience.

  This approach ensures a clean and modern aesthetic, enhancing accessibility and making the overall experience more calming for users, conveying the spirit of Brighton and it's relaxed environs,

   ![Image of UX Colour Palette](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/colorpalette.png)

## Technologies Used

  - Backend: Python 3.13, Django 4.2
  - Frontend: HTML, CSS (Bootstrap 5), JavaScript
  - Database: PostgreSQL 
  - Tools: Git, GitHub, Heroku, VS Code
  - Testing: Flake8 and and Black to adhere to PEP 8 standards.

 
 ### Original Custom Data Models:

- **Account Model (`account/models.py`)**
  - The `CustomUser` model is a custom implementation of Django's user authentication system.
  - It replaces the default user model and manages authentication and user attributes.

- **Article Model** (`creator/models.py`)**
 The creator app defines an `Article` model, which is therefore a custom model. It has custom fields like `article_teaser`, `is_event_related`, and `event_venue` are tailored for specific functionality.
  - Represents content created by the user.
  - Each article belongs to a specific user.
  - May include optional event details (time, date, venue, and address).
  - Event details can be rendered below the article upon creation.
	
## Deployment

  The application was deployed with Heroku. The following preparatory steps are as follows:
  1. Set Debug Mode to False. In settings.py, the DEBUG setting was set to False to ensure a production-ready environment.
  2. A Procfile document is defined. web: gunicorn harvest_main.wsgi.
  3. Store Dependencies - All required dependencies were documented in requirements.txt using: pip3 freeze --local > requirements.txt.
  4. Create a New Heroku App. 
    - Log in to the Heroku Dashboard.
    - Click New > Create New App.
    - Enter a unique app name and select the desired region.
    - Click Create App.
  5.  Configure Application Settings
    - Navigate to the Settings tab.
    - In the Config Vars section, add the required environment variables:
      -  Database_URL
      -  DJANGO_SECRET_KEY
    - Add the Heroku/Python buildpack.
  6.  Install Whitenoise for Heroku to serve static files / images on Heroku.
      - Setting Up Whitenoise for Static Files in Heroku

    - pip install whitenoise

    Add to settings.py: 

    MIDDLEWARE = [
         "whitenoise.middleware.WhiteNoiseMiddleware",
    ]

    STATIC_URL = "/static/"
    STATIC_ROOT = BASE_DIR / "staticfiles"  # Heroku serves from this folder
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

  7. Connect to GitHub Repository.
      -  In the Deploy tab, under Deployment Method, select GitHub.
      -  Follow the steps to authorize and connect your GitHub account.
      -  Search for the repository and click Connect.
  8.  Deploy the Application.   
      -  Select manual deployment
      -  In the Manual Deploys section, select a branch and click Deploy Branch.
  9.  Access the Live Application.
      -  Once the deployment is complete an app link is generated. The live application can be accessed at <a href="https://harvest-main-55fca7957f91.herokuapp.com/" target="_blank">Harvest App</a>
  

## Flowchart

![Flowchart](https://)

# Testing

## Manual Testing

| Test Case                         | Expected Result                                                                     | Test Result |
|-----------------------------------|-----------------------------------------------------------------------              |-------------|
| Lorem                             |readable content of a page when looking at its layout. The point of using Lorem I    | ✅ PASS          |
| Lorem                             | Prompt user to enter a food item.                                                   | ✅ PASS          |
| Lorem                             | readable content of a page when looking at its layout. The point of using Lorem I   | ✅ PASS          |
| Lorem                             | readable content of a page when looking at its layout. The point of using Lorem I   | ✅ PASS          |
| Lorem                             | readable content of a page when looking at its layout. The point of using Lorem I   | ✅ PASS          |
| Lorem                             | readable content of a page when looking at its layout. The point of using Lorem I   | ✅ PASS          |
| Lorem                             | readable content of a page when looking at its layout. The point of using Lorem I   | ✅ PASS          |
| Lorem                             | If the API does not recognize a food item, the app displays the message: 'Food item 

   
## Bugs/Updates after Testing

- Indentation Fixes: Corrected indentation issues.
- A fix on the image uploader in the published section "Update Article" could not re-upload new images. 
  - Update: `update-article.html`

Changes Made:

1. **Form Update:**
   - Added `enctype="multipart/form-data"` to the `<form>` tag (required for file uploads).

   ```html
   <form method="POST" enctype="multipart/form-data">
   ```

2. **View Update:**
   - Updated the `render` function to pass the `article` object to the template, ensuring the current image is displayed.

   ```python
   return render(request, 'creator/update-article.html', {
       'UpdateArticleForm': form,
       'article': article  # Pass the article to the template for displaying current image
   })
   ```
	
---

Bug Fix: `Value Too Long` Error

Issue:
- **BUG:** `DataError at /creator/create-article` – Value too long for type character varying(10).

Solution:
- Increased the `CharField` length for the `title` field from 10 to 255 characters.

  ```python
  class Article(models.Model):
      title = models.CharField(max_length=255)  # Increased max_length to 255
      event_date = models.CharField(max_length=10)
  ```

- **Status:** Bug fixed.

		 	
## Code Style and Readability

- The code is formatted with the Black Python Formatter to maintain consistent code style and readability.

## Validator Testing

- Passed the CI Python Linter. "All clear no errors found"


## Credits 

  - [Real Python](https://realpython.com/.com/)
  - [Stack Overflow](https://stackoverflow.com/questions/10004850/python-classes-and-oop-basics)
  - [w3schools - Python](https://www.w3schools.com/python/ref_string_isdigit.asp)

  ## Acknowledgements
 