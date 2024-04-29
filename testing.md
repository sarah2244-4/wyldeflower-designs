# Testing

## Contents

- [Manual Testing](#manual-testing)
    - [Responsivity](#responsivity)
    - [Browser Compatibility](#browser-compatibility)
    - [Functionality and Usability](#functionality-and-usability)
- [Testing User Stories](#testing-user-stories)
    - [New Users](#new-users)
    - [Existing Users](#existing-users)
- [Bugs](#bugs)
    - [Resolved Bugs](#resolved-bugs)
    - [Unresolved Bugs](#unresolved-bugs)
- [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Javascript Validation](#javascript-validation)
    - [Python Validation](#python-validation)
    - [Lighthouse Testing](#lighthouse-testing)

## Manual Testing 

### Responsivity

| All pages | iPhone SE | Pixel 5 | Samsung Galazy S8+ | iPad Air | Surface Pro 7 | Nest Hub | Desktop |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| Responsive | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| All buttons change when hovered over | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

### Browser Compatibility

| All pages | Chrome | Firefox | Edge | Opera |
| --- | :---: | :---: | :---: | :---: |
| Loads as expected | Yes | Yes | Yes | Yes |
| Responsive | Yes | Yes | Yes | Yes |

### Functionality and Usability

| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Type in website url | Loads home page | Yes | 
| Visit page that doesn't exist | Loads custom 404 error page | Yes |
| Click logo | Loads home page | Yes | 
| Click Home button in navbar | Loads home page | Yes |
| Hover over Resources button in nav bar | Dropdown menu appears | Yes |
| Click Biology button in navbar dropdown | Biology resources appear | Yes |
| Click Chemistry button in navbar dropdown | Chemistry resources appear | Yes |
| Click Physics button in navbar dropdown | Physics resources appear | Yes |
| Click Sign Up button in navbar dropdown | Sign up form appears | Yes |
| Click Sign Out button in navbar | User is logged out and redirected to home page | Yes |
| Use website without being logged in | Navbar displays home, resources, sign up and login buttons | Yes |
| Use website logged in as a user | Navbar displays home, profile, resources, and logout buttons | Yes |
| Click Login button in navbar dropdown | Login form appears | Yes |

#### Login and Sign Up Form Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Submit sign up form with a field missing | Form does not submit and user is promtped to fill in required field | Yes |
| Submit sign up form with existing username or email | Form does not submit and message is flashed to say they already exist | Yes |
| Submit sign up form with passwords that don't match | Form does not submit and message is flashed to say passwords should match | Yes |
| Submit valid sign up form | New user is created and profile page is loaded | Yes |
| Submit login form with incorrect email | Form does not submit and message flashed that email does not exist | Yes |
| Submit login form with incorrect password | Form does not submit and message flashed that password is incorrect | Yes |
| Submit valid login form | Profile page loads and message flashed to say login is successful | Yes |

#### Profile Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click Edit Profile button on profile | Edit profile form appears | Yes |


#### Product Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click add on profile to add resource | Add resource form appears | Yes |


#### Bag Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click add button to add comment with blank field | Form not submitted and user directed to fill in field | Yes |


#### View Products Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click all button on biology resources | All biology resources are shown in the table | Yes | 


#### Admin Actions
| User Action | Expected response | Correct Response |
| --- | --- | :---: |
| Click all button on biology resources | All biology resources are shown in the table | Yes | 

## Testing User Stories

### New Users

| Goal | Result | Image |
| --- | --- | :---: |
| Find information about the website to see what it is used for. | The hero text on the index page displays a line explaining the aim of the website straight away. There is a promotion table beneath this explaining why users should use the webiste. | [Hero image](resourcehub/static/assets/images/readme/hero.JPG) [Promo table](resourcehub/static/assets/images/readme/promo-table.JPG) |


### Existing Users

| Goal | Result | Image |
| --- | --- | :---: |



## Bugs

### Resolved Bugs

- The rows of the table overlapped on smaller screens. Without adding horizontal scroll bars or making text too small to read, I created tables with fewer columns to display on smaller screens. Most vital information was shown as the rest can still be accessed when the row is clicked. 
- Comments were added to the same row of the comment table on the profile if more than one comment was added to the same resource. To fix this, I had to move for loop outside the table row. 
- Alerts wouldn't close when the close button was clicked. The fix was to add javascript to add an event listener to close the alert when the button is clicked. 

### Unresolved Bugs




## Validation

### HTML Validation

I used the [W3 Validator](https://validator.w3.org/) to validate my HTML files. I did this by pasting in the URI for each page of my depolyed site. 

Initial issues were: 



After fixing these each page passes the validator with no issues: 

<details>
<summary>Index</summary>

![W3C Validator for index page](resourcehub/static/assets/images/testing/w3-index.JPG)
</details>

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

### CSS Validation

I used the [W3 Validator](https://validator.w3.org/) to validate my styles.css file. 

![W3C Validator for CSS](#)

### Javascript Validation

I used [JSHint](https://jshint.com/) to validate my script.js file. 

The only message is one undefined variable but this was needed to initialize the Materialize elements so I was able to ignore it. 

![JSHint message](/static/assets/images/testing/jshint.JPG)

### Python Validation

I used the [Code Institute Python Linter](https://pep8ci.herokuapp.com/) to validate my python files. 

The initial results that came up were whitespaces at the ends of lines and some lines were too long. 

![initial Python Linter](resourcehub/static/assets/images/testing/pep8-checker-initial.JPG)

After fixing these, there were no errors. 

![Final Python Linter](resourcehub/static/assets/images/testing/pep8-checker-final.JPG)

### Lighthouse Testing

I used lighthouse in Chrome Dev Tools to test for performance, accessibility, best practises and SEO for each page. 

Initial lighthouse testing showed:


Final results can be seen here: 

<details>
<summary>Index Page</summary>

![Index Page Lighthouse Test](resourcehub/static/assets/images/testing/lighthouse-index.JPG)
</details>


### Return to [README](README.md).  