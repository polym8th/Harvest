# Harvest

![Index Page](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/screensresponsive.webp)

[HARVEST Live Page](https://harvest-main-55fca7957f91.herokuapp.com)

## About

Harvest is a platform for content creators, interested in sharing their best local finds in Brighton and the surrounding areas. It enables users to share local insights, discover unique experiences, and contribute to a growing community of culture enthusiasts. It provides features for users to sign up to the platform to add articles and related events that are happening in Brighton and parts of East Sussex.

### Target Users

Harvest is designed for people of all ages, both residents and locals, who want to explore the local area of Brighton and surrounding areas. 

### Features

This project was developed as a full stack web application, utilizing Python, Django, HTML, CSS, and JavaScript to ensure scalability and maintainability. 
The development process incorporates deployment strategies and follows Agile methodologies to enhance the web application's stability and performance.

- **Index Page**
    - The site visitor can read articles in full with unrestricted guest access to sample content before registering on the Harvest Platform.
    - There are articles whereby the content is abridged for registered users only. The visitor can click on the register button to sign up. 

- **Register Page**
    - Users must enter their email, first name, last name, and password for registration.
    - Password validation is implemented to ensure security, integrated with Crispy Forms.
     See Figure 1

- **Login Page**
    - The user can log in with their email and password to log into the Creator dashboard or the Client dashboard.
     See Figure 2

- **Creator Dashboard**
    - Creators can create articles, add related events, view published articles, manage their accounts, and log out.
    See Figure 3, 4 & 5

  **Super Users** can create articles, add related events and have the privilege to update and delete ALL articles. 

    - **Navigation Menu:**
        - **Dashboard** - The user arrives at the front page of the dashboard. The dashboard shows the articles that have created by the authenticated user.
        - **Create Article** - Allows authenticated users with the 'creator' role to create and publish an article by adding a title and content. A Rich Text Editor allows users to format text using paragraphs, bold, italics, and more.
        - **Add an Event** - Beneath the "Create Article" form, users can add an event related to the article.
        - **Upload Image** - Supports PNG, JPEG, and WebP formats. The uploaded image will be displayed above the article text.
        - **Published** - Allows creators to view and edit their published articles. They can edit, update or delete their own articles. 
            - Articles are identified by the user who created them with an ID number.
            - Superusers can update and delete all articles.
            - Authenticated users can use the search bar for articles by entering a part of the title or keyword. 
        - **Manage Account**
            - Users can update their first name, last name, and email.
            - Users can delete their account or cancel their subscription.
        - **Logout** - The creator (user) can log out of the Creator dashboard.

- **General User Dashboard**
    - **Navigation Menu:**
        - **Dashboard** - The user arrives at the front page of the dashboard.
        - **View Article** - Allows registered users to view published articles.
        - **Manage Account**
            - Users can update their first name, last name, and email.
            - Users can delete their account or cancel their subscription.
        - **Logout** - The user can log out of the General dashboard.


![Register](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/screens/register.webp)

Figure 1 - Registration Form 



![Login](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/screens/login.webp)

Figure 2 - Login form



![Create Article](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/screens/createarticle.webp)

Figure 3 - Create an Article



![Events](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/screens/events.webp)

Figure 4 - Create an Event



![Published](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/screens/published.webp)

Figure 5 - View Published Articles

## How to Use the Harvest Site

### 1. Register an Account

To register for an account, follow these steps:

- Click on the **Register** button.
- If you want to be a contributor to Harvest as a Content Creator, check the box labelled **"Are you a Content Creator"** for access to the Creator dashboard.
- Fill in your details:
  - Name
  - Email
  - Password
- Click **Submit**.

### 2. Register as a General User

If you are **not** a content creator:

- Leave the **"Are you a Content Creator"** box unchecked.
- Log in with your email and password.
- You will be redirected to the general user's dashboard, where you can:
 
  - View the dashboard. 
  - Read articles.
  - Manage your account.

### 3. Login

To log in:

- Navigate to the **Login** page.
- Enter your registered email and password.
- Click **Login** to access the Creator dashboard.

### 4. Create an Article

To create an article:

- Fill in the **Title**, **Content**, and **Upload an Image**.
- If the article is related to an event, tick the checkbox **"Is this article related to an event?"**
  - Enter the **Event Date and Time**.
  - Provide the **Event Name**.
  - Enter the **Event Venue**, **Event Address**, and **Event Postcode**.
  - Once this Event form is submitted, the Article will be assigned an Event ID, allowing you to update or delete it from the Published section as an **event**.

### 5. Update or Delete Your Articles

As a content creator, you can manage your published articles:

#### To update an article:

- Go to the **Published** section of the Creator dashboard.

#### Use search bar to search for the article or event. Search by Article or Event Title.

- Click **Update Article** next to the article you want to update.
- Make the necessary changes to the **Title**, **Content**, or **Image**.
- If the article is not currently viewable by guest visitors, you can make it public by checking the box labelled **"Make this article a teaser for guest visitors"**.
- Click **Update** to save your changes.
- Please note you can only update the article you have created.
- To update or delete an event, follow the same steps as above. Simply click **Update Event** or **Delete Event** next to the relevant event to open the edit form.

#### To delete an article:
- In the **Published** section, click **Delete** next to the article you want to remove.
- Confirm the deletion when prompted.  
- The article will be permanently removed from the platform.
- Please note you can only delete the article you have created.

### 6. Manage Account

To update account details:

- Navigate to **Account Settings** in the Creator dashboard.
- Update your:
  - First Name
  - Last Name
  - Email
- Click **Update Details**.

### 6. Cancel Your Subscription

If you wish to cancel your subscription:

- Navigate to your account settings.
- Delete your account.


### UX WireFrames

The Harvest wireframes, designed in Figma, served as my initial sketches to plan the platform's layout and functionality. They were significant in ensuring a user-friendly experience with intuitive navigation. These wireframes outline key pages, including the Landing Page, Registration, Login, Creator Dashboard, General User Dashboard, Article/Event Submission, and Account Settings. This mockup of the Harvest project helped me map out each page before I started coding it in Python.

- See below a wireframe for each page:
  
   Index Page

  ![Index Page](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/indexpage.webp)

  Registration Page

  ![Register Page](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/register.webp)

  User (General) Dashboard
  
  ![User Dashboard](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/generaluser.webp)

  Creator Dashboard - Create Article Page 

  ![Creator Dashboard](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/createarticle.webp)

  Creator Dashboard - Published Articles Page

  ![Creator Dashboard](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/wireframes/publishedarticles.webp)

## Agile Framework and Project Management

  - I used an Agile workflow with GitHub Projects and Issues to keep the project organised.
  - User Stories & Acceptance Criteria - Each feature was decomposed into User Stories with clearly defined Acceptance Criteria, maintaining the main objectives and usability.
  - Task Prioritization:  Issues were categorized using labels to establish development priorities; such as Must-Have, User Story or Implementing a new user authentication system.
  - Kanban Workflow - A three-stage Kanban board was utilized for task management: 
    -  To Do – Newly created tasks pending development. 
    -  In Progress – Tasks actively being developed. 
    -  Done – Completed and verified tasks, ready for deployment.

#### User Stories
   The following sections outline user stories and their acceptance criterias. These demonstrate how the application fulfils user requirements and delivers frontend CRUD functionality.

#### As a Visitor (Unregistered User)
Acceptance criteria:
- **Browsing Content** – As a visitor, I want to browse free articles on the index page, so that I can explore what the platform offers before registering an account.
- As a user, I want to see a navigation bar so I can navigate to the register button to sign up for an account and access new articles.
- As a user, I want to receive a password sent to my email so that I can log in to my account.

#### As a User (Logged-in User)
- As a registered user, I want to access exclusive articles.
- As a registered user, I want to access the platform and view events that are scheduled.

#### Access the Dashboard to Manage User Account
- As a registered logged-in user, I want to access the dashboard and manage my account.
- As a registered logged-in user, I want to access exclusive articles.

#### Create an Article
- Given that I am an authenticated user with the Creator role and that I declared that I am a content creator by checking the box.
- When I provide a title and content.
- Then I should be able to submit the article successfully, and it should be saved in the system with a date stamp.

#### Delete an Article
   -  As an authenticated user with the role of the Creator, I want to delete my own articles so that I can remove outdated or unnecessary content.
   - **Given** that I am an authenticated user/ Creator.
   - **Given** that I am an authenticated user/ Creator – I have the privileges to delete only the articles that I created.

   -  More User stories to be found directly on Github: 
    For detailed user stories, refer to the **[Harvest User Stories](https://github.com/users/IsaHu-dev/projects/10)**.

#### Update own Articles: 
   - **Given** that I am an authenticated user with the 'creator' role, I want to update my own articles, so that i can keep my content relevant.
   - I can Update all articles and keep the content relevant to the theme of Harvest
   - I have privileges to delete any articles to keep the content relevant and to delete unnecessary content
   - A date stamp is published under the article
   - Then my name (as an authenticated user / creator) is displayed under the article as "Updated by: [Creator Name]".

#### UX - Colour Palette

  The Harvest platform has a calm and modern design with soft, muted colours that are easy on the eyes. Instead of using bright colours, the visual focus is on article images, content, and button styling to create a smooth user experience.

  This approach ensures a clean and modern aesthetic, enhancing accessibility and making the overall experience more calming for users, conveying the spirit of Brighton.

   ![Image of UX Colour Palette](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/colorpalette.png)


## Technologies Used

  - Backend: Python 3.13, Django 4.2
  - Frontend: HTML, CSS (Bootstrap 5), JavaScript and Django Crispy Forms
  - Database: PostgreSQL 
  - Tools: Git, GitHub, Heroku, VS Code
  - Testing: Flake8 and and Black to adhere to PEP 8 standards.

 
 ### Original Custom Data Models:

- **Account Model (`account/models.py`)**
  - The `CustomUser` model is a custom implementation of Django's user authentication system.
  - It replaces the default user model and manages authentication and user attributes.

- **Article Model** (`creator/models.py`)**
 The creator app defines an `Article` model, which is therefore, a custom model. It has custom fields like `article_teaser`, `is_event_related`, and `event_venue` are tailored for specific functionality.
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
    - Log in to the Heroku dashboard.
    - Click New > Create New App.
    - Enter a unique app name.
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
      -  Once the deployment is complete, an app link is generated. The live application can be accessed at <a href="https://harvest-main-55fca7957f91.herokuapp.com/" target="_blank">Harvest App</a>

## Installation of Harvest app 

Follow these steps to set up and run the project locally:

#### 1. Clone the Repository
In Git Bash, clone the repository:
```bash
git clone https://github.com/IsaHu-dev/Harvest

cd Harvest
```

#### 2. Create a Virtual Environment
It’s recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

#### 3. Install Dependencies
Use `pip` to install the required dependencies.

```bash
pip install -r requirements.txt
```
#### 4. Run Database Migrations
Apply database migrations:

```bash
python manage.py migrate
```

#### 5. Create a Superuser (Optional)
To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

#### 6. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
```

Local access to the application is at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Flowchart

![Flowchart](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/flowchart.webp)
 [View PDF](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/flowchart.pdf)

# Testing

## Manual Testing
## User Testing Report

---

## A. User Registration & Login

| **Test Case**                   | **Steps**                                                                                                                                   | **Expected Result**                                                                   | **Pass/Fail** |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|--------------|
| Register as a General User     | 1. Navigate to the Register page.<br>2. Fill in all required fields.<br>3. Leave 'Are you a Content Creator' unchecked.<br>4. Click 'Submit'. | User sees a success message and can log in to the General User Dashboard.             | ✅ PASS      |
| Register as a Content Creator  | 1. Navigate to the Register page.<br>2. Fill in all required fields.<br>3. Check 'Are you a Content Creator'.<br>4. Click 'Submit'.          | User sees a success message and gains access to the Content Creator Dashboard.        | ✅ PASS      |
| Invalid Registration           | 1. Leave required fields blank.<br>2. Enter an invalid email format.<br>3. Use an already registered email.<br>4. Click 'Submit'.            | A registration error messages is displayed.                                             | ✅ PASS      |
| Login with Valid Credentials   | 1. Navigate to the Login page.<br>2. Enter valid email and password.<br>3. Click 'Login'.                                                   | User is redirected to their respective dashboard.                                     | ✅ PASS      |
| Login with Incorrect Credentials | 1. Navigate to the Login page.<br>2. Enter incorrect email or password.<br>3. Click 'Login'.                                               | Error message is shown.                                                               | ✅ PASS      |
| Password Mismatch During Signup | Enter different values in the two password fields during registration.                                                                      | Error message displays: *"The two password fields didn't match."*                     | ✅ PASS      |

---

## B. Navigation & UI Testing

| **Test Case**              | **Steps**                             | **Expected Result**                          | **Pass/Fail** |
|---------------------------|---------------------------------------|----------------------------------------------|--------------|
| Landing Page Loads        | Open the home page.                   | Page loads with visible navigation options.  | ✅ PASS      |
| Navigation Menu Works     | Click on each menu option.            | Each option redirects to the correct page.   | ✅ PASS      |
| Button Interactivity      | Click action buttons and hover.       | Buttons respond, hover effects work as expected. | ✅ PASS   |
| Page Load Speed           | Test initial load time.               | Page loads within 3 seconds.                 | ✅ PASS      |
| Mobile & Responsive Design| Open site on mobile/tablet devices.   | UI adjusts to screen size appropriately.     | ✅ PASS      |
| Access to Index Page via Harvest Logo   | After logging in as a Content Creator, click the Harvest logo.     | User is redirected to the index page and has full access to all articles. | ✅ PASS      |
| Access to Index Page via Harvest Logo   | After logging in as a General User, click the Harvest logo.        | User is redirected to the index page and has full access to all articles. | ✅ PASS      |

---

## C. Content Creation - Access for Content Creators

| **Test Case**                         | **Steps**                                                                                 | **Expected Result**                                                             | **Pass/Fail** |
|--------------------------------------|-------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------|
| Access the Dashboard                 | Log in as a Content Creator.                                                              | Creator Dashboard loads successfully.                                           | ✅ PASS      |
| Create an Article                    | Fill in the Title, Content, and upload an image. Click 'Submit'.                          | Article appears in the dashboard.                                               | ✅ PASS      |
| Create Article (Invalid)             | Try submitting an article with missing required fields.                                   | An appropriate error message is displayed.                                      | ✅ PASS      |
| Enable "Teaser" Mode for Article     | Select the "Teaser" checkbox.                                                             | Article is shown as a teaser to guest (unauthenticated) users.                  | ✅ PASS      |
| Edit / Update an Article             | Modify an existing article and save.                                                      | Changes are saved and reflected.                                                | ✅ PASS      |
| Delete an Article                    | Click 'Delete' on an article.                                                             | Article is permanently removed.                                                 | ✅ PASS      |
| Enable Guest Visibility on the Update form | Tick the "Guest Visibility" checkbox and submit the form.                           | Article becomes accessible to unauthenticated users as part of the update.      | ✅ PASS      |
| Create an Event                      | Enter event details (name, venue, time, etc.) and click 'Submit'.                         | Event appears in the Creator Dashboard.                                         | ✅ PASS      |
| Select Calendar Date & Time          | Attempt to select a date in the past.                                                     | Past dates are restricted; future date is saved successfully.                   | ✅ PASS      |
| Add Postcode                         | Enter postcode in correct format (less than 10 characters).                               | Error appears if the format is incorrect.                                       | ✅ PASS      |
| Leaving the Postcode field blank     |'Please enter a postcode' - pop up message occurs when the field is left blank.            | Error message appears when the user tries to submit without input.              | ✅ PASS      |
| Edit an Event                        | Modify existing event details and save.                                                   | Updates are saved.                                                              | ✅ PASS      |
| Delete an Event                      | Click 'Delete' on an event.                                                               | Event is removed from the dashboard.                                            | ✅ PASS      |
| Restrict Update (Article Ownership)  | Log in as Creator B and attempt to update Creator A’s article.                            | Action is blocked; error or redirect occurs.                                    | ✅ PASS      |
| Restrict Delete (Article Ownership)  | Log in as Creator B and attempt to delete Creator A’s article.                            | Action is blocked; error or redirect occurs.                                    | ✅ PASS      |
| Restrict Event (Event Ownership)     | Log in as Creator B and try deleting Creator A’s event.                                   | Deletion fails; appropriate error or redirect is shown.                         | ✅ PASS      |

---

## D. General User Actions - Access for General Users

| **Test Case**                            | **Steps**                                      | **Expected Result**                                | **Pass/Fail** |
|-----------------------------------------|------------------------------------------------|----------------------------------------------------|--------------|
| View Client Dashboard                   | Log in as a General User.                      | General User Dashboard loads correctly.            | ✅ PASS      |
| Browse Articles                         | Open and read multiple articles.              | Articles load and display content as expected.     | ✅ PASS      |
| View Article Counter                    | Fetch the article count from the server.       | Article count displays correctly.                  | ✅ PASS      |
| Search for Articles or Events           | Enter a keyword in the search bar.             | Matching articles or events are returned.          | ✅ PASS      |

---

## E. Account Management

| **Test Case**           | **Steps**                                                            | **Expected Result**                             | **Pass/Fail** |
|------------------------|----------------------------------------------------------------------|-------------------------------------------------|--------------|
| Update Profile         | Go to Manage Account.<br>Edit name and/or email.<br>Click 'Save'.    | Profile updates are saved.                      | ✅ PASS      |
| Change Password        | Go to Manage Account.<br>Enter new password.<br>Click 'Update'.       | Password is successfully changed.               | ✅ PASS      |
| Cancel Subscription    | Navigate to Manage Account.<br>Click 'Cancel Subscription'.           | Subscription is deactivated.                    | ✅ PASS      |
| Delete Account         | Navigate to Manage Account.<br>Click 'Delete Account'.                | Account is permanently deleted.                 | ✅ PASS      |

---

## F. Mobile & Cross-Browser Testing

| **Test Case**             | **Steps**                                             | **Expected Result**               | **Pass/Fail** |
|--------------------------|--------------------------------------------------------|-----------------------------------|--------------|
| Mobile Compatibility     | Open site on mobile, tablet, and desktop devices.       | UI renders properly on all devices.| ✅ PASS     |
| Cross-Browser Test       | Open site in Chrome, Firefox, Safari, and Edge.         | Layout and functionality remain consistent. | ✅ PASS |

---

## G. CKEditor Rich Text Editor Testing

| **Test Case**              | **Steps**                                                    | **Expected Result**                                        | **Pass/Fail** |
|---------------------------|--------------------------------------------------------------|-------------------------------------------------------------|--------------|
| Load CKEditor on Form     | Open the article creation page (`/create-article/`).         | CKEditor loads without issues.                             | ✅ PASS      |
| Bold & Italic Text        | Type text, select it, and apply bold or italic formatting.   | Formatting is applied as expected.                         | ✅ PASS      |
| Line Breaks               | Press `Enter` while typing.                                  | A new paragraph is created.                                | ✅ PASS      |
| Save & Render HTML        | Submit an article and view the published page.               | HTML tags (`<p>`, `<strong>`, etc.) render correctly.      | ✅ PASS      |

---

**Last Updated:** April 7, 2025


## Summary

This **manual user testing** ensures **Harvest** functions as expected across different scenarios. Regular testing will improve **reliability, usability, and user experience**. 

### Bugs/Updates after Testing
1. 📌Issue: The image uploader in the published section "Update Article" could not re-upload new images. 
  - Update: `update-article.html`

 🛠 Solution: 
 Form Update:
   - Added `enctype="multipart/form-data"` to the `<form>` tag (required for file uploads).

   ```html
   <form method="POST" enctype="multipart/form-data">
   ```
 🛠 Changes made **View Update:**
   - Updated the `render` function to pass the `article` object to the template, ensuring the current image is displayed.

   ```python
   return render(request, 'creator/update-article.html', {
       'UpdateArticleForm': form,
       'article': article  # Pass the article to the template for displaying current image
   })
   ```

2.📌 Issue: `Value Too Long` Error
   `DataError at /creator/create-article` – Value too long for type character varying(10).

 🛠 Solution:
  - Increased the `CharField` length for the `title` field from 10 to 255 characters.

  ```python
  class Article(models.Model):
      title = models.CharField(max_length=255)  # Increased max_length to 255
      event_date = models.CharField(max_length=10)
  ```
3. Fixing CKEditor 5 Form Submission in Django

  📌 Issue: ``Required`` Content Was Removed
  By default, Django **adds the `required` attribute** to form fields. However, CKEditor 5 **replaces the default `<textarea>`** with a custom rich text editor while hiding the original field.

-  Django renders the `<textarea>` with `required=True`:
    ```html
    <textarea name="content" required id="id_content"></textarea>
    ```
-  Once CKEditor loads, it hides the textarea:
    ```html
    <textarea name="content" required id="id_content" style="display: none;"></textarea>
    ```
-  Since the `<textarea>` is now hidden, the browser cannot validate it.
-  This results in the error:
    ```
    An invalid form control with name='content' throws an error in the javascript console.
    ```
-  The form fails to submit.

---

### Solution: Remove `required` from the Form Field
Since CKEditor **handles input differently**, we **removed `required=True`** from the Django form field:

### **Fixed `forms.py`**
```python
content = forms.CharField(
    widget=CKEditor5Widget(config_name='default'),
    required=False  
)
```
### **Status:** All Bugs are fixed.


## Code Style and Readability

- The code is formatted with the Black Python Formatter to maintain consistent code style and readability.

## Validator Testing

- Passed the CI Python Linter. "All clear no errors found"
- Code passed JSHint – a JavaScript validator that checks for syntax errors and coding issues.

 ![W3 HTML Validator](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/testing/w3html.webp)
 ![W3 CSS Validator](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/testing/cssw3.webp)
 ![LightHouse](https://github.com/IsaHu-dev/Harvest/blob/main/media/readme/testing/lighthouse.webp)

## Credits 

  - [Real Python](https://realpython.com/.com/)
  - [Stack Overflow](https://stackoverflow.com/questions/10004850/python-classes-and-oop-basics)
  - [w3schools - Python](https://www.w3schools.com/python/ref_string_isdigit.asp)
  - [Codemy.com -a code snippet adapted from this tutorial -YouTube](https://www.youtube.com/watch?v=O5YkEFLXcRg&t=617s)
  - Wire Frames and Diagram Basics Templates adapted from [Figma](https://www.figma.com/)
  - Several photos on the web app are royalty-free images from [Envato](https://elements.envato.com/). A couple of the photos are my own, taken in Brighton.
  - Writing and Content adapted from [Wikipedia](https://en.wikipedia.org/wiki/Brighton_Palace_Pier) and online resources. Content is also rewritten by myself.
  - Richtext Editor on the Create Article page (ckeditor.js) Javascript adapted from [CKEditor 5](https://cdn.ckeditor.com/)
  - The Harvest Logo is my original design.
  
## Acknowledgements
 
 - Thanks to the mentor programme at Code Institute with Moritz Wach.