# Wyldeflower Designs
 
Wyldeflower designs is an Ecommerce store that sells wall art and activities for young children. The majority of items are printable from home so will be downloaded upon purhcase. Users will be able to purchase items, save delivery details, and view past orders. 

The site is live, the link to this is found [HERE](#).

![Website mockup](static/assets/images/readme/mock-up.JPG)

## Contents

- [User Experience (UX)](#user-experience-ux)
  - [Goals](#goals)
  - [Users](#users)
  - [New User Stories](#new-user-stories)
  - [Existing User Stories](#existing-user-stories)
  - [Admin User Stories](#admin-user-stories)
- [Design](#design)
  - [Wireframes](#wireframes)
  - [Database](#database)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Effects](#effects)
  - [Design Choices](#design-choices)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
  - [Main Languages](#main-languages)
  - [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)
- [Deployment](#deployment)
  - [PostgreSQL Database](#postgresql-database)
  - [Heroku Deployment](#heroku-deployment)
  - [Local Source Files](#local-source-files)
    - [Cloning](#cloning)
    - [Forking](#forking)
    - [Running Locally](#running-locally)
- [Credits](#credits)
  - [Content](#content)
  - [Images](#images)
  - [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Goals

The aim of the site is to allow users to browse the store and make purchases instantly or save to a wishlist to encourage future purchases. 

- Users want to be able to intuitively navigate the site and receive immediate feedback when they interact with it. 
- Users want to be able to search through products and view all relevant details. 
- Users want to be able to add products to their bag and easily checkout. 
- Users want to be able to view past orders. 

### Users

Users of the site will most likely be famale parents looking for activities or wall art for their children. 

### New User Stories

As a first time user I want to be able to:
- View a list of products to find out what the company sells
- View product details to find out prices and details on sizes etc
- Easily register an account to view my profile and easily make purchases
- Sort the products by price, date added or best sellers
- Filter products by category to find what I'm looking for easily
- Search for a specific item using keywords to see if the shop stocks what I'm looking for
- Easily add an item to my basket to purchase an item 

### Existing User Stories

As an existing user I want to be able to:
- Login or logout easily to access my account
- Recover or reset my password in case I forget it so I can still access my account
- View order history 

As a shopper I want to be able to:
- Easily enter payment and delivery information
- View an order confirmation page and have a confirmation emailed as a reciept 

### Admin User Stories

As an admin I want to be able to: 
- Add new product listings easily 
- Delete product listings if it's no longer in stock
- Edit product listings such as prices, images or descriptions
- View all orders 

## Design

### Wireframes

| Home Page | How It Works | Products View | Detailed Product View | Bag | Checkout | Sign Up | Login | Profile | Edit Profile | Add/Edit Product |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [Mobile](#) | [Mobile](#) | [Mobile](#) | [Mobile](#) | [Mobile](#) | [Mobile](#) | [Mobile](#) | [Mobile](#) | [Mobile](#) | [Mobile](#) | [Mobile](#) |
| [Tablet](#) | [Tablet](#) | [Tablet](#) | [Tablet](#) | [Tablet](#) | [Tablet](#) | [Tablet](#) | [Tablet](#) | [Tablet](#) | [Tablet](#) | [Tablet](#) |
| [Desktop](#) | [Desktop](#) | [Desktop](#) | [Desktop](#) | [Desktop](#) | [Desktop](#) | [Desktop](#) | [Desktop](#) | [Desktop](#) | [Desktop](#) | [Desktop](#) |

### Database 

I planned out the database before beginning the project with defined relationships. The site uses a relational database due to the ability to link tables together. There are () entities in total. 

![Entity relationship diagram](static/assets/images/readme/erd.png)

#### Product
#### Order
#### OrderLineItem
#### 

### Colour Scheme

The site's colour scheme is based on the palette. This palette was selected using Coolers. 
A lot of colours for children are bright. These colours were chosen to provide a soft hue that are gentle to the eyes and help young children's minds. 
The pastels also appeal to the female users. 

I used a [contrast checker](https://webaim.org/resources/contrastchecker/) to ensure elements had a high enough contrast ratio. I ensured all elements had a high ratio. 

![Contrast results](#)

### Typography

Fonts were chosen to maintain high readability and with female parents in mind. The logo has a child element to it and this was added to a couple of places. 

### Effects 

### Design choices

- The site is as consistent as possible across all screen sizes. 
- A small, fairly neutral, colour palette was used for consistency with blue and red added for pops of colour where needed. 
- All buttons/links are animated to make it clear that they could be selectable.
- The off-white background fits in with the colour palette and helps remove the harsh white background. This is particularly useful for people with reading difficulties. All forms have a white background to stand out from the background and help the text stand out. This wasn't as harsh as the full white background. 
- Cancel buttons are red so they stand out as warning in case users clicked on something by accident. 
- The navbar contains a dropdown for the different subjects to keep it minimal and allow easy navigation. 
- The hero image was chosen as the colours were consistent with the colour scheme. It also helps make the purpose of the website clear by containing items associated with working / planning lessons as a teacher.
- I wanted my hero image fairly bright to make the site welcoming. I added a transparent overlay to make it dark enough to read text over it as well as a dark transparent background to the text overlay itself so the text stands out and is readable. 
- The subject cards are on the index page as well as the navigation bar to encourage first time users to click on them and look through the different resources. 
- The resources were displayed as cards to start with. However, these looked messy as they were large and all different sizes. I decided to change them to a table to give a more consistent and clear layout. I made the whole row selectable so users could view more information easily without having to search for something to click. 
- The downlaod option is on the resources table for large screens. The table columns overlapped on smaller screens so I removed unneccessary details from the table. Users can still click to view the detailed resource information from the table. 

## Features

### Existing Features

<details>
<summary>Home Page</summary>

</details>

<details>
<summary>Navigation Bar</summary>

</details>

<details>
<summary>Footer</summary>

</details>

<details>
<summary>Sign Up Form</summary>

</details>

<details>
<summary>Login Form</summary>

</details>

<details>
<summary>Bag</summary>

</details>

<details>
<summary>Checkout</summary>

- Stripe integration
</details>

<details>
<summary>Products View</summary>

</details>

<details>
<summary>Products Filter</summary>

</details>

<details>
<summary>How It Works</summary>

</details>

<details>
<summary>Detailed Product View</summary>

</details>

<details>
<summary>Profile</summary>

</details>

<details>
<summary>Admin Page</summary>

</details>

<details>
<summary>Add Product</summary>

</details>

<details>
<summary>Logout</summary>

</details>

<details>
<summary>404 Page</summary>

</details>

### Future Features

## Testing 

View the testing document [here](testing.md). 

## Technologies Used 

### Main Languages

HTML5, CSS3, Javascript, Python used. 

### Frameworks, Libraries and Programs

- Django to provide Python framework. 
- PostgreSQL to create relational database and store user data.
- [Bootstrap](#) front-end framework for navbar, modals, tables, cards and alignment.
- Visual Studio Code as code editor. 
- GitHub Desktop to store the local repository and allow me to code using VS code. 
- [GitHub](https://github.com/) to store the repository online.
- [Font Awesome](https://fontawesome.com/) for icons.
- Chrome Dev Tools for debugging during development.
- [Heroku](https://www.heroku.com) to deploy the live site.
- [ElephantSQL](https://www.elephantsql.com) to host my PostgreSQL database.
- [Stripe]() for payment integration to checkout.

## Deployment

### PostgreSQL Database

To set up the PostgreSQL database follow the steps: 
- Log into ElephantSQL 
- Click on 'Create New Instance'
- Type in the name of the plan (should be the project name)
- Select the plan required
- Click 'Select Region'
- Select data centre closest to you
- Click 'Review' and check through details
- Click 'Create instance' if everything is correct
- Click on the name of the instance created 

### Heroku Deployment

Follow the steps below to deploy the project on Heroku:
- Create a requirements.txt file in the root file directory using the command
` pip freeze --local > requirements.txt `. This will automatically fill with the requirements Heroku will need to install
- Create a Procfile in the root file directory and add the command 
```
web: python run.py
```
- Once these are added, log into Heroku and click 'New', 'Create new app'
- Create a name and the appropriate region and click 'Create app'
- Click on 'Settings' and 'Reveal Config Vars'
- Enter the relevant config variables
- Add a config variable named `DATABASE_URL` and copy in the database URL from ElephantSQL from the database created earlier 
- Navigate to 'Deploy' and connect to GitHub
- Select 'Enable Automatic Deploys' or manually deploy the site
- Once the site has been build, click 'More' and 'Run console'
- Type python3 and click 'Run'
- Import the database from the project onto ElephantSQL by typing into the console: 
```
from taskmanager import db
db.create_all()
```
- The site has now been successfully deployed

### Local Source Files

To access this GitHub repository locally, click on [this link](https://github.com/sarah2244-4/project-3-teacher-resource-hub) and either clone or fork it using the guidelines below. 

#### Cloning

- Open the [GitHub Repository](https://github.com/sarah2244-4/project-3-teacher-resource-hub) 
- In the repository click on the green '<> Code' dropdown
- Copy the HTTPS, SSH or GitHub CLI URL
- Open Git Shell or Terminal on the computer's IDE
- Change the current working directory to the 
- Type in `git clone` followed by the copied URL, for this project that would be 
```
git clone https://github.com/sarah2244-4/project-3-teacher-resource-hub
```
- Press enter and the clone will be successfully created

Cloning means that any edits made can be pushed and so make changes to the original repository. 

#### Forking 

- Open the [GitHub Repository](https://github.com/sarah2244-4/project-3-teacher-resource-hub) 
- In the repository click on the 'Fork' button just below the main bar
- A copy of the repository will now appear in your GitHub account

Any changes made to the forked respository will not affect the original respository in any way. 

#### Running Locally 

Once the respository has been cloned or forked, the relevant dependencies will need to be installed. 

- Open the IDE's Terminal and type 
```
pip3 install -r requirements.txt
```
- Create `env.py` within the root file directory and add this into the '.gitignore' file so it is not visible to others
- Within the `env.py` file, include the following:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "a_secret_key")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DB_URL", "postgreSQL database name")
```

## Credits

### Content

- The project is heavily based on the Boutique Ado Walkthrough. 
- [Am I Responsive?](https://ui.dev/amiresponsive) to display a mock-up of my site in different viewports.
- I used [Coolors](https://coolors.co/) to help me come up with a colour scheme.
- I used [WebAIM](https://webaim.org/resources/contrastchecker/) to check the contrast of the colours used on all the elements. 

### Images

- Hero image downloaded from [Pexels](https://www.pexels.com/photo/silver-ipad-545057/), which was free with no credit required.
- The site's favicon was generated at [favicon.io](https://favicon.io/favicon-generator/). 
- The logo was created with [LogoAI's logo maker](https://www.logoai.com/logo-maker).
- Images for products came from [](). 

### Acknowledgements

- Thank you to Code Institute for providing detailed lessons and walkthroughs.
- Thank you to the Code Institute community on Slack for providing advice and motivation.
- Thank you to my mentor Spencer for his invaluable advice and expertise.
