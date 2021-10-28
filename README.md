
![image](https://user-images.githubusercontent.com/58527807/139157500-0de62f08-547f-49b5-aa3c-f7173d3cb7e2.png)


## **Goal for this project**

This project is all about managing business contacts for freelancers. It’s supposed to allow you to organize your contacts by Industry and flag if they are helpful or not. You can add personal data so when you reach out you the information at hand to know their family status, hobbies, etc to make the relationship more personal and help you make a lasting impression even if your memory isn’t that good.  Users register then can log in and add, edit and delete contacts.
You can click to the link for the deployed site. (https://my-persona-portfolio-project.herokuapp.com/ )


## Table of Contents
* [UX](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Colors](#colors)
        * [Structure](#structure)
* [Wireframes:](#wireframes)
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
    * [Database Structure](#database-structure)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)

<a name="ux"></a>
 
## **UX**

<a></a>  

### **User Goals**

* This website has to work well on on all kind of devices like mobile phones, tablets and desktops.
* The site must be easy to use.
* The site must be atleast nevigable locatable onsite and offsite.
* The website has to be easy to use and easy to update information.
* The site must be visually appealing website


[Back to Top](#table-of-contents)

<a></a>

### **User Stories**

* As a user, I want to login after I created an account and see my previous inserted information.
* As a user, I would like to have a personal profile for my contact management.  
* As a user, I would like to have a dashboard where I can have a good overview. 
* As a user, I want to be able to search on date to get specific data. 
* As a user, I want to be able to edit the contact management profile.
* As a user, I want to have the possibility to edit a log when I made a mistake or want to add/delete some info. 
* As a user, I want to have the possibiltiy to delete a log as well when no longer relevant. 
* As a user, I want the website to be easy to use. 
* As a user, I want the process to add / edit / delete info to be easy

<a></a>

### **Site owners Goals**
* To have an appealing website that it is easier to scroll on different different pages.
* To make the web user friendly great functionality. 
* To make the website to help the user to delete, update and sign in.

[Back to Top](#table-of-contents)

<a></a>

### **User Requirements and Expectations**

<a></a>

#### Requirements
* Easy way to sign In and Out.
* Easy to navigate.
* Appealing dashboard with a functional overview.

<a></a>

#### Expectations

[Back to Top](#table-of-contents)

<a></a>

### **Design Choices**

<a></a>
#### Colors

I have decided to use some colors that fit well with the strong presentation of the portfolio.
Below I will explain more why I choose the various colors and for what I will be using them.

![Color Palette](wireframes/color_pallet.png)

* #F8F9FA: I have decided to keep the background of the overall website white-Cultured in order give the clean look of the Site.
* #CED4DA: This color I will use as a background color for whole dashboard. 
* #6C757D: This color I will use as a background color for the logs on the dashboard in order to have a small contract versus #D9D9D9 dashboard color.
* #212121: This color that I will use for my navigation bar and buttons in order to give a bit of color to the website. This color will also be used as the overall text color.

I have used a contrast checker in order to make sure that the contrast is sufficient.
This way my content will be easily readable. 

<a></a>

#### Structure

I have chosen to use [Materialize](https://materializecss.com/) to create an overall structure for my website. 
Materialize provides various elements of CSS and Javascript which is very helpful to keep a good structure on your page. 
The reason why I choose Materiaize is mainly due to the various features they offer like a datepicker, floating action button etc. 

[Back to Top](#table-of-contents)

--- 
<a></a>

## **Wireframes**
I just used only hand drawing for my wireframes to try bring out the ecxact work I wanted.
You can as well find my wire frame below:
For the homepage I have only created 1 wireframe as the design is quite basic and looks identical on all screen sizes.

* [Home](wireframes/desktop-home.png)

### Desktop  Wireframes

* [Login](wireframes/desktop-login.png)
* [Contact](wireframes/contact-form-desktop.png)

### Mobile Wireframes

* [Login](wireframes/login-form-mobile.png)
* [Contact](wireframes/contact-form-mobile.png)


### **Flowcharts**

I have decided to make a flowchart for the sign-in / register proccess to completely understand each step of the process.  

### Database Structure

### Database
I used mongodb to store the data in the contact manager app.

#### Users
Authentication and Contacts Management uses the USER Model.

| Parameter | DataType | Validation                                                            |
|-----------|----------|-----------------------------------------------------------------------|
| _id       | ObjectId | auto generated as Primary Key                                         |
| username  | String   | must be 5 characters or more, alphanumeric only, unique to system     |
| password  | string   | stored as a hash, but must be 5 characters or more, alphanumeric only |

- [x] Create is done in the Registration Process
- [x] Read is done on all pages
- [ ] Update must be done as ADMIN user in mongodb
- [ ] Delete must be done as ADMIN user in mongodb

### Fields
Fields represent the Choices for business Categories that you assign to contacts

| Parameter  | DataType | Validation                    |
|------------|----------|-------------------------------|
| _id        | ObjectId | auto generated as Primary Key |
| field_name | String   | string                        |

- [ ] Create must be done as ADMIN user in mongodb
- [x] Read is done for create contact page and edit contact page
- [ ] Update must be done as ADMIN user in mongodb
- [ ] Delete must be done as ADMIN user in mongodb

### Contacts
Contacts are business contacts that users manage through this app

| Parameter     | DataType | Validation                                                                                                                               |
|---------------|----------|------------------------------------------------------------------------------------------------------------------------------------------|
| _id           | ObjectId | auto generated as Primary Key                                                                                                            |
| contact_name  | String   | string, must be between 5 and 50 characters                                                                                              |
| industry_name | String   | restricted to FIELD.field_name values                                                                                                    |
| email_name    | String   | must be a valid email address  1+ characters followed by @ sign followed by  1+ characters followed by . sign followed by  1+ characters |
| person_detail | String   | must be between 5 and 500 characters                                                                                                     |
| is_helpful    | Boolean  | default is False                                                                                                                         |
| created_by    | ObjectId | Auto generated, relates to the user that created the contact                                                                             |
| created_on    | String   | Auto created by datetime as today in YYYY-MM-DD format                                                                                   |
| updated_on    | String   | auto created on edit as datetime of today in YYYY-MM-DD format                                                                           |

- [x] Create is done on the Add Contact Page
- [x] Read is done on My Contacts Page, Contact Detail Page, Edit Contact Page.
- [x] Update is done by the Edit Contact Page
- [x] Delete is done by a button on the My Contacts Page or a Button on the Contact Detail page. 



## Features 
### Implemented Features
### LogIn Page
- Allows you to log to see their private information
- Has unauthenticated menu options
- 
![image](https://user-images.githubusercontent.com/58527807/139317959-d977c4f8-284a-415b-855b-e4ec9a630abd.png)


#### Register Page
- Allows user to have an account on the site
- User name must be unique

![image](https://user-images.githubusercontent.com/58527807/139318206-93decbcd-8b15-41b6-8b62-6e829d28ff40.png)


#### My Contacts Page
- Shows user dashboard of contacts they have with just name, a star if helpful and business category, link to details,   edit button, delete button
- has special message if no contacts yet
- Has add button

![image](https://user-images.githubusercontent.com/58527807/139319256-9664d047-f0c6-4f68-8529-def6f9eb2e66.png)


#### Contact Detail Page
- Shows user all information about contact
- has edit and delete buttons
- checks that user owns contact before allowing user to look

![image](https://user-images.githubusercontent.com/58527807/139319535-c01e76c0-f652-485c-bfa8-e59b7f8e73e9.png)


#### Add Contact Page
- Allows user to add a contact
- Has cancel button if user decides not to add a contact

![image](https://user-images.githubusercontent.com/58527807/139320526-f615cade-01d8-403e-ae2c-39d59ef3adc6.png)


#### Edit Contact Page
- Allows user to edit a contact
- Has a cancel button if user decides not to add a contact
- checks that user is logged in and owns contact before allowing user to do things

![image](https://user-images.githubusercontent.com/58527807/139320702-37a66f54-2868-482f-9694-00dc4d45b59a.png)


#### Home Page
- Has nice graphic carousel telling users why the contact management system is useful
- has navigation to other pages

![image](https://user-images.githubusercontent.com/58527807/139320974-7f30bced-57e8-4358-87e4-8849c4963ff6.png)


#### Navigation
- mobile is via hamburger menu
- Desktop are links
- Options changed if user is logged in or not

### Future Features
- add filtering on contact page by created/updated date, industry, is helpful
- add search on contacts page by name or words in details
- add updated date to contacts page and details page
- add conversations that can be linked to contacts with date and details
- add way to manage conversations
- add link to conversations to detail and my contacts page
- hook email to email app launcher
- add ability to have users list them self as contacts that all users can search and import to their own contacts

## **Technologies used**

<a></a>

### **Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

<a></a>

### **Libraries and Frameworks**

* [Font Awesome](https://fontawesome.com/)
* [Materialize](https://materializecss.com/)
* [Google Fonts](https://fonts.google.com/)
* [jQuery](https://jquery.com/)

### **Tools**
* [Git](https://git-scm.com/)
* [GitPod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [techsini](http://techsini.com/)
* [MongoDB Atlas](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

[Back to Top](#table-of-contents)

<a></a>
## Testing

### Validation Testing

- [CSS Validator](https://jigsaw.w3.org/css-validator/) Note, any error associated with root: color variables were ignored.
- I copied my style.css as direct input and fixed one issue to pass validation

![image](https://user-images.githubusercontent.com/58527807/138954730-44aa019e-e4a4-4fcd-b082-0f966cd48abf.png)


- [HTML Validator](https://validator.w3.org/)

Home page validation. (Use url)

![image](https://user-images.githubusercontent.com/58527807/138957822-a52fdbd2-2974-4b78-b639-d6b0801becb6.png)

logIn validation. (Use url)

![image](https://user-images.githubusercontent.com/58527807/138958254-e4330d41-6975-4738-9954-acd62e43b2c6.png)

Registration Validation. (Use url)

![image](https://user-images.githubusercontent.com/58527807/138958414-f5f5472c-52d2-486c-b3f9-ed3fba7ddb6d.png)

Contacts Page Validation{Page Source}

![image](https://user-images.githubusercontent.com/58527807/138960138-435f7ad2-0786-4f1a-955c-823470c8dd79.png)

Edit Contact Page validation. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/138961906-f8b0e1ce-90d8-4a48-a5f9-da6d1cb0c53d.png)

Add Contact Page validation. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/138962667-aadabe2f-0fbe-48dd-bdda-2b1d41318eb5.png)


Contact Detail Page validation. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/138963981-87c2b478-6e5e-4c36-9dda-dac7c424318e.png)


- [JS validation](https://jshint.com) for each .js file/ , if using ES6, add this before pasting in your file: `/*jshint esversion: 6 */ `

Script.Js Validation Results.

![image](https://user-images.githubusercontent.com/58527807/138965733-2e23a570-9c76-463f-b39d-9f60dcf41bbe.png)


- [PEP8 Validator](http://pep8online.com/)

App.py Validation Results.

![image](https://user-images.githubusercontent.com/58527807/138968633-0c276963-64f3-4f61-818e-caee6a92357d.png)


### Cross Browser and Cross Device Testing
I made sure my application looks good on different kind devices, different Operating systems and browsers!.


| Device                | Browser  | OS             | SCREEN WIDTH |
|-----------------------|----------|----------------|--------------|
| iphone 7              | Chrome   | ios            | 375 x 667    |
| ipad(Chrome emulator) | Chrome   | ios            | 768 x 1024   |
| Laptop HP Elite       | Fire Fox | window 10 Pro  | 1920 x 1080  |
| Laptop HP Elite       | Edge     | Windows 10 Pro | 1920 x 1080  |

### Automated Testing
I did not run automating testing. I didn't have time to learn the skill but I  really would like to do it in the future.

### Manual Testing

I excuted the following tests manually in chrome on my Laptop using the chrome browser.

1. **Register Page**
>  Go to the Register page: http://my-persona-portfolio-project.herokuapp.com/register
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on my contact page
>    - [x] Be logged in and go to register page http://my-persona-portfolio-project.herokuapp.com/register should have error saying you are already registered and be on contacts page

2. **Login Page**
>  Go to the LogIn page: http://my-persona-portfolio-project.herokuapp.com/login
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an non existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on contact page
>    - [x] Be logged in and go to register page http://my-persona-portfolio-project.herokuapp.com/login should have error saying you are already registered and be on contacts page

 3. **My Contact Page**
>  Go to the Register page: http://my-persona-portfolio-project.herokuapp.com/my_contact
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on my contact page
>    - [x] Be logged in and go to register page http://my-persona-portfolio-project.herokuapp.com/my_contact should have error saying you are already registered and be on contacts page

4. **Add Contact**
>  Go to the Register page: http://my-persona-portfolio-project.herokuapp.com/add_contact
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on my contact page
>    - [x] Be logged in and go to register page http://my-persona-portfolio-project.herokuapp.com/add_contact should have error saying you are already registered and be on contacts page

5. **Contact Detail Page**
>  Go to the Register page: http://my-persona-portfolio-project.herokuapp.com/contact_detail
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on my contact page
>    - [x] Be logged in and go to register page http://my-persona-portfolio-project.herokuapp.com/contact_detail should have error saying you are already registered and be on contacts page

6. **Edit Contact & Delete Process**
>  Go to the Register page: http://my-persona-portfolio-project.herokuapp.com/edit_contact
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on my contact page
>    - [x] Be logged in and go to register page http://my-persona-portfolio-project.herokuapp.com/edit_contact should have error saying you are already registered and be on contacts page

## Accessibility

Home Page Validation Results. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/139154986-2c59b1c7-6d3f-492c-91df-eca222d967e9.png)

LogIn Validation Results. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/139155247-f14fddde-5c2a-45ec-8c9e-63155c343fe4.png)

Registration Validation Page Results.(Use Page source)

![image](https://user-images.githubusercontent.com/58527807/139155435-41f55def-0dc5-4250-a601-41e4c5964c8e.png)

Contacts Page validation Results. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/139156113-7a6b33f5-2970-4979-9167-9037388a9169.png)

Add Contact Page Validation Results. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/139156537-0d5bad14-e28c-4f5b-851c-4a33101a7d0c.png)

Edit Contact Page Validation Results. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/139156751-446eedc5-538f-4b5c-9483-b867f712b653.png)

Contact Detail Page Validation Results. (Use Page source)

![image](https://user-images.githubusercontent.com/58527807/139157018-4f94c051-3431-4997-9073-7194acf4f840.png)



### Defect Tracking

You should mention  any  bugs or problems you discovered during your testing, even if you haven't addressed them yet.

Here is a [Defect Tracking Template](https://docs.google.com/spreadsheets/d/1tYB4X4wTCNEW_Y1no3hsGbclh2bLokl_I5Ev3s5EuJA/edit?usp=sharing) you use as a starting point to track defects. Make a copy of the sheet to your own account and update the Features sheet to match your project. 

Again, you could use [github issues](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit?usp=sharing) to track you defects. Or write them up with markdown.

### Outstanding Defects
It's ok to not resolve all the defects you found. If you know of something that isn't quite right, list it out and explain why you chose not to resolve it.

## Deployment
### Local Deployment

I have created the Portfolio project using Github, from there I used [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits to git followed by "git push" to my GitHub repository. 
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

This project can be ran locally by following the following steps: (
I used Gitpod for development, so the following steps will be specific to Gitpod. 
You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/David-Gyavi/my-persona-portfolio-project.git
    ``` 

1. Access the folder in your terminal window and install the application's [required modules](https://github.com/David-Gyavi/my-persona-portfolio-project/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

    1. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ.setdefault("IP", "0.0.0.0")
    os.environ.setdefault("PORT", "5000")
    os.environ.setdefault("SECRET_KEY"
    os.environ.setdefault("MONGO_URI"
    os.environ.setdefault("MONGO_DBNAME", "DATABASE_NAME")
    ```

    Please note that you will need to update the **SECRET_KEY** with your own secret key, as well as the **MONGO_URI** and **MONGO_DBNAME** variables with those provided by MongoDB.
    Tip for your SECRET_KEY, you can use a [Password Generator](https://passwordsgenerator.net/) in order to have a secure secret key. 
    I personlly recommend a length of 24 characters and exclude Symbols.
    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. 
    Don't forget to update the necessary fields like password and database name. 

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

1. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```

### To deploy your project on Heroku, use the following steps: 

1. Login to your Heroku account and create a new app. Choose your region. 
1. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.  
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: python app.py
    ```

1. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
1. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):
    !You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website. 

    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    MONGO_URI = YOUR_MONGODB_URI
    MONGO_DBNAME = DATABASE_NAME
    ```

1. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 
    

[Back to Top](#table-of-contents)

<a></a>   

## **Credits**

* I would like to thank my mentor Malia [Malia_mentor](https://github.com/maliahavlicek/ci_mentor_insights.git) for her endless support and guiding me into becomming a better developer!

But unfortunately I was not really settled she really tried her best but I was also up and down due to the kind of work am currently doing but i know I will improve with more practice. thanks Malia

[Back to Top](#table-of-contents)

    

    
    
