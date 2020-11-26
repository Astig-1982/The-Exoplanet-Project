# The Exoplanet Project

The Exoplanet Project, named Other Words, is a simple app that represents a quick guide to exoplanets - planets outside our solar system.

## UX

### Project Goals

The app is designed as a simple to use guide to exoplanets. The main goal is to provide the user the possibiliy to have her/his own list where she/he can add their prefered exoplanets in order to keep track of them as they are officially confirmed by NASA, ESA, .. and many others authorized entities, and also to add any of these exoplanets to their favourites list. To kick things off, a list with 12 of the most relevant exoplanets confirmed up date will be provided. From there, the user is free to add any of the planets to her/his list. To make things a bit more interesting, the user will also have the possibility to check her/his weight on any of the exoplanets added, if ever, hypothetically (or not), will have the chance to end up on one of them.

### User Goals

- An app that serves as a guide to relevant confirmed exolanets.
- Possibility to add any new prefered exoplanet to her/his own list.
- Possibility to delete any new prefered exoplanet from her/his own list.
- Possibility to have the planets displayed in the list depending on some of their different properties (eg. type, size).
- Navbar available across and throughout all sections for a quick and easy navigation on the website.
- A way to follow the developer on social media for the latest updated.
- Responsive interaction with the website on desktop, table and mobile.

### User Stories

- As a user, I would like to be able to find out what's the app about and how to use its features.
- As a user, I would like to have a clear and clean display of the items (exoplanets).
- As a user, I would like a navbar that it's always available on all section, for me to easily navigate at any section of the app from everywhere.
- As a user, I would like clean and visible action buttons at every section.
- As a user, I would like my own section (list) where I am able to store my items (exoplanets).
- As a user, I would like the possibility to remove at any point any item I wish from my list.
- As a user, I would like an intuitive and easy way to add items to my list.
- As a user, I am expecting guidance where necessary; especially working with exoplanets and precise data about them, that might require some research on where the specific data can be found.
- As a user, I would like to be notified (via clear messages displayed on the screen) when some specific action cannot be performed and the reasons why.
- As a user, I would like to be able to sort my items depending on some of its most important properties.
- As a user, I am looking for an app that will also keep me on some level entertained while I'm using it.

### App Owners Goals

- Providing a dynamic app to act as a guide to exoplanets, where the user would be able to have its own section where she\he can add any exoplanet they wish, thus being a good tool to keep track of all the newly discovered exoplanets.
- Providing the user a default list of exoplanets to get things started and act as a guide on what type of data can be stored about the exoplanets.
- Keeping the user entertained by allowing her/him to calculate its weight on each exoplanet from her/his list. This will encourage the user to insert more items in her/his list, thus the time spent on the app will increase.

## Design Choices

I have chosen dynamic fonts for the entire app, to keep the user entertained; also they might remind the user of the colors of space dust on some of the best known nebulae.

### Main Background Image:

The main background image of the app is a representation of the recently confirmed exoplanet **Trappist 1 e** and it has been designed by [NASA](https://www.nasa.gov/) within their [SPACE TOURISM](https://solarsystem.nasa.gov/resources/682/space-tourism-posters/) program. Please see at the [Credits](#credits) section the source where the image in the app was taken from. I have chosen this image because it represents the travelers' excitement upon arrival on a foreign planet, with them browsing through the window of their space ship. In my opinion, this can as well represent the users' excitement when browsing through exoplanets in the app, a brief virtual trip through outer space.

### Exoplanets' Images:

I have used images representing each exoplanet from the main list in order for the user to have a better representation of the specific exoplanet. It also adds dynamicity to the app by zooming in the image upon hovering. Please see at [Credits](#credits) section the sources where the images have been taken from.

### Default Images Within The App:

A default image will be added automatically when manually adding an exoplanet to your list. There are 2 images, each representing a common rocky planet and resepctively a common gas giant. Please see at [Credits](#credits) section the sources where these images have been taken from.

### Fonts:

I chose to use [ABRIL FATFACE](https://fonts.google.com/specimen/Abril+Fatface?query=abril) as the font for all the main titles as I believe it's thickness and clean shape provide good readability and would be a good match for all of the app's sections.

I chose to use [LATO](https://fonts.google.com/specimen/Lato?query=lato) as main font as I believe it provides a good readability and looks proffessional.

I chose to use [ROBOTO SLAB](https://fonts.google.com/specimen/Roboto+Slab?query=roboto) for all action buttons as I believe it provides one of the best readability, which is always important for action buttons.

### Icons:

No icons have been used for the app.

### Colors:

* Primary: **See Through Red** rgba(112, 16, 3, 0.8). I chose this color as background for all sections that contain text (including flash messages), as I believe it offers a not so strong contrast with the main image (in this case the main image will still be visible), but in the same time a good enough contrast for the text to be readable.

* Secondary **Indigo** rgb(60, 10, 125). I chose this color for the action buttons and navbar as it matches some of the colors found in the main background image, and also I believe it provides a very good contrast between them and the rest of the app making them more visible, which is very important in order to provide a good user experience.

* Tertiary Color: **Light Grey** #e5e5dc. I chose this color for the text as overall it gives a good contrast with all backgrounds used in the app. I chose this in the detriment of plain white as I believe it is also a bit warmer color, being a better fit for the overall design choices used throughout the app.

* Register Button: **Candy Apple Red** rgb(196, 23, 0). I chose this color for the Register button as it stands out on the navbar, urging the user to register if she/he hasn't done it so far. Also it is similar to the overall colors in the main background image. This color is not used anywhere else in the app.

## Wireframes:

I've built the wireframes for this project using [BALSAMIQ](https://balsamiq.com/). I've started creating the basic structure, basically the display of the items (exoplanets) and building on that afterwords. I have built wireframes for all multiple devices, which speeded up the process altogether. Please note that very few features and design elements may vary slightly or a lot from the original wireframes, as while I was developing I had to either adapt or, due to esthetic reasons, I changed my mind completey in regards to some elements of design.

Please view my wireframes for this project [here](https://github.com/Astig-1982/The-Exoplanet-Project/tree/master/wireframes). You can also see my wireframes on gitpod in the **wireframes** directory.

## Database Structure:

I have used MondoDB to set up the database. The project contains the following collections:

#### **Users:**

Key      | Value
---------|-----------
_id      | ObjectId
username | String
password | String

#### **Exoplanets**

Key                 | Value
--------------------|-----------
_id                 | ObjectId
exoplanet_image     | String
planet_name         | String
discovery_date      | Date
distance_from_earth | Decimal
type                | String
star_system         | String
mass                | Decimal

#### Individual users' collection

Key                 | Value
--------------------|-----------
_id                 | ObjectId
exoplanet_image     | String
planet_name         | String
discovery_date      | Date
distance_from_earth | Decimal
type                | String
star_system         | String
mass                | Decimal

## Features:

* Register an account form, Log-in & Log-out functionality.
* Adding manually any preferred exoplanet into the user's favourites list.
* Guidance on inserting an exoplanet to favourites list.
* Adding a default image of a rocky or gas giant planet, depending on the type of planet inserted by the user.
* Adding to favourites list any exoplanet from the main list provided in the app.
* Advanced item information, providing users with some of the exoplanet's most important properties.
* Possibility to filter the exoplanets by type: rocky planets or gas giants.
* Possibility to sort the exoplanets depending on their mass, from smallest to largest and other way around.
* Possiblity to calculate the user's weight on each exoplanet added to her/his favourites list.
* Profile section that will display the number of exoplanets the user has in her/his favourites list; also displays the number of rocky planets and number of gas giants in the favourites list.

### Register an account form, Log-in & Log-out functionality:

I chose to use this feature because it is one of the main features that defines the purpose of the app - each user to have her/his own favourites list where to add any preferred exoplanet.

#### Implementation:

I've created a Register/Log In section that it's connected to a login function in the app.py file. The login function will look for the user's username and passwords in the users collection in the database and if the password enteres mathces with the one in the database, the user's username will be put in a session variable. If the username is not found in the database, the user will be advised to go to the register form, where her/his username and passwords (once inputed in the relevant fields) will be saved into the users collection in the database and the user's username will be put in a session variable. Upon adding the first exoplanet to the favourites list, a collection with the name of the user's username will be created in the database.

### Adding manually any preferred exoplanet:

I chose to use this feature because, similar to the first feature, it is one of the main features that defines the porpuse of the app - to add any exoplanet as their discovery is cofirmed to the favourites list, in this case the user will be up to date to the lates discoveries in terms of exoplanets.

#### Implementation:

I've created a form with the fields representing the exoplanet's properties. The function created in app.py file will take the user's input and added into a variable 'new_planet' that will be inserted into the user's collection in the data base.

### Guidance on inserting an exoplanet to favourites list:

I have created this feature to provide the user a quick guidance on how the fields should be completed. It is crucial for the user to understand where she/he can find the mass of an exoplanet on internet (or what's the easiest way to find it). In order to further guide the user regarding the mass, I have provided a screenshot where the user can find the location of the mass on the wikipedia page. The mass property is very important to be inserted correctly, as based on this the app will calculate the user's weight on the exoplanet.

#### Implementation:

I have simply created a section in the html file where the form for inserting the exoplanet is located, in which I have explained how some of the properties would need to be inserted. I have also provided a link to another newly created html page that contains the screenshot with the location of the mass.

### Adding a default image of a rocky or gas giant planet:

I chose to use this feature as I believe it is good and useful for the user to have some sort of representation of the exoplanet inserted. In the nearest future I will develop this feature in order to give the possibility to the user to upload her/his own image of the exoplanet.

#### Implementation:

In the function created in app.py file to insert an exoplanet, I simply used an if statement with the outcome of defining a variable 'default_image', depending whether the type of exoplanet inserted by the user is rocky or gas. The 'default_image' variable will be inserted as a value for 'exoplanet_image' key in the user's collection.

### Adding to favourites list:

As mentioned above, this feature is on of the core features that defines the purpose of the app.

#### Implementation:

I've created a function in app.py file, that based on its id, will find the respective exoplanet in the 'exoplanets' collection in the data base and insert the same exoplanet in the user's collection (favourites list).

### Advanced exoplanet information:

I chose to feature in order to display in details some of the exoplanet's most relevant properties. For any exoplanet enthusiast, the info displayed in regards to the exoplanet in this section is essential when thinking of almost any celestial body (distance from earth, start system, etc.).

#### Implementation:

I've simply created a function in app.py file that, based on its id will find the exoplanet in either the 'exoplanets' collection or user's collection in the database and diplay all of its key-values in a separate section (page).

### Possibility to filter the exoplanets by their type:

I chose to use this feature as I believe any exoplanet enthusiast will be interested in filtering the exoplanets based on one their most important characteristics - their type of composition.

#### Implementation:

I've created functions in app.py file that will find in the respective collection ('exoplanets' or user's collection) only items (exoplanets) with the value of either 'rocky' or 'gas' for the key 'type'.

### Possibility to sort the exoplanets depending on their mass:

I've created this function as the mass is one of the most important properties in a celestial body. The user will be most likey interested to check which exoplanet is more massive than the other. This feature, together with the one above (filtering by type), in my opinion will keep the user more enternained when using the app, resulting in more time spent on the app.

#### Implementation:

By simply creating a function in app.py file that will find all exoplanets in a respective collection ('exoplanets' or user's collection) and applies sort() method to them before rendering them onto either the main list section or favourites list.

### Possiblity to calculate the user's weight on each exoplanet:

This feature was created in the spirit of keeping the user excited and also making the user adding more exoplanets to her/his favourites list - as only on the surface of the exoplanets added to favourites list can the weight be calculated. It also, in my opinion, contributes to app's dynamicity.

#### Implementation:

I've created a function in app.py file that will take the user's input (her/his weight) from a form created html, and parse it into a float number. It also finds, based on its id, the respective exoplanet in the user's collection, take its 'mass' and parse it also into a float number. Afterwords it multiplies the mass and the user's input and the result (representing her/his weight on the respective exoplanet) will be rendered onto a new page.

### Profile section that will display the number of exoplanets in the favourites list:

I chose to use this feature as I believe it's good for the user to have a quick reminder of the items in her/his favourites list everytime when she/he logs in.

#### Implementation:

In the function created in app.py file for displaying the profile, I've used count() method on the items from the the user's collection.

## Technologies used:

### Languages:

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
- [JavaScript](https://www.javascript.com/)
- [Python](https://www.python.org/)

### Tools & Libraries:

- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [MongoDB](https://www.mongodb.com/)
- [TinyPng](https://tinypng.com/)
- [PyMongo](https://pypi.org/project/pymongo/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB)

## Testing:

Planning for this project took a significant amount of a time as this was my first time working with databases.

### Testing Stories:

#### W3C Validation Service:

- I have tested my **HTML** code using [The W3C Markup Validation Service](https://validator.w3.org/). As expected, it has found errors related to the use of jinja (DOCTYPE not declared, head element missing the required instance of child element title). I have ingnored this errors as they were due to the use of jinja. I have used the W3 Markup Validation more to find any errors like unclosed divs or other basic html errors. It has actually found a couple of unclosed divs and a double use of an id. I have corrected the respective errors. It has also found one more error not related to the use of jinja - 'The element button must not appear as a descendant of the anchor element'. As I was advanced on my project with little time left until my deadline, I have decided to treat this error as a bug (see my [Bugs](#bugs) section) as all the styling for almost each individual button has been already set in the style.css. In the very nearest future I will remove all buttons from the anchor tags and style the achors.
- I have tested my **CSS** code using [CSS Validation Service](https://jigsaw.w3.org/css-validator/). It has found NO errors.

#### Register with an account:

- I have tested this feature multiple times as it was my first time ever working both with session variables and databases. The code checks if the user exists in the users collection and if it does a flash message will appear displaying the username already exists. If it doesn't, the username and hashed passwords will be inserted into the users collection in the database. Then the code initiates the ‘session’ for the user signing them in. To test this feature I've created a few temporary accounts in order to test that the registration worked as intended, checking what values were passed and stored into the database.

#### Deleting and account:

- The code will first delete the entire user's collection from the database. Then it removes the user object from the 'users' collection and logs the user out. To test this feature I've created a few temporary accounts, created the user's collection by adding to favourites list and deleted the profile. Afterwords I was checking the database to check if both the user object and the collection have been removed. It works as intended. I did this several times with succesful outcomes everytime.

#### Sign out of an account:

- I've simply created a function using session.pop and redirecting the user to the login page once she/he's logged out. Testing this feature was very straight forward, all I had to do was log into a previously created account and click the log out button in the navigation. I have used google dev-tools to check if the session was cleared and the user was no longer logged in. The test has passed succesfuly based on the above criteria.

#### Inserting an exoplanet:

- I have tested multiple times this feature by inserting items (exoplanets) and checking the favourites list in the app and the users collection in the database to see if all details entered in the respective fields were correctly inserted. I've added pattern attributes to the html form in order to catch all the unwanted inputs - Ex: the 'distance from earth' and 'mass' fields need to be only digits. I have also checked multiple times to see if the default image was inserted in the database, coresponding with the value of the input inserted by the user at the 'type' field (either 'rocky' or 'gas'). All the tests have passed succesfuly and the function works as intended.

#### Calculating the user's weight on each exoplanet:

- I have tested multiple times this function by entering different values and manually checking the outcome with a calculator. I have also tested this function when calculating the user's weight on the exoplanets inserted manually by her/him. All the tests have passed succesfuly and the function works as intended.

#### Try/Except:

- I've added try/except statement everywhere a function will activate only if the user is logged in. The try block is looking in the users collection for the object with the key 'username' matching the session variable defined at the login function, and sets it as value for a variable named 'username'. If this is not possible (because the session variable hasn't been defined as yet), the except block will be executed. This redirects the user to the login page and displays a flash message - "Please login in order to use this feauture" (or similar message depending on the action the user is trying to perform). I have tested the code numerous times, being logged in and logged out. I was encountering one error at 'calculate_weight' function. Within this function I also had an if statement that will check if the respective exopalanet was first added to the favourites list, and if not, the notAdded.html page would be rendered. Unfortunately, even though I was logged in, the function was redirecting me to the login page everytime the I was trying to calculate the weight on an exoplanet that was not yet added to my favourites list. Luckily I have found the error: I have enclosed in the try block almost the entire 'calculate_weight' function - basically the try block was trying first to find the session variable and also was executing the whole function. Because of this, the except block was handling the else block from the if statement (that checks if the respective exoplanet was first added to the favourites list) as an error. I have modified the function and now the try block ckecks only if the session variable exists and if it does, it executes the rest of the function. If the respective exoplanet is not added to the favourites list, the user will now be taken to notAdded.html page, as expected, and NOT redirected to the login page. I have again tested numerous times and everytime it now works as expected.

## Overall:

### Responsivness:

I knew that the project needed to be fully responsive on all types of screen, especially mobile friendly. In order to accomplish this requirement I used Bootstrap as HTML framework. I've carried the testing using dev-tools throughout and a final test after the completion.

### Result:

The app is fully responsive as expected, all elements and content fit within their boundaries and are easy to see on any device.

## Bugs

During the development I was lucky enough to encounter little to no significant bugs. Below are a few that unfotunately I couldn't get rid of:

* **Bug**:

  'The element button must not appear as a descendant of the anchor element' - this is not an actualy bug, but rather an error found by W3C Markup Validator. I have decided to treat it as one, as being very close to my deadline removing all buttons from anchors and styling again the anchors was not time permitted. 100% in the very nearest future this error will be corrected.

* **Bug**:

  The home page for mobile screens has a very small lateral margin/padding that I struggled to find out where it is coming from. I have encountered similar issues to at least half of the pages on all screens and succesfuly I got rid of them mainly with the help of [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB). However I cannot seem to be as succesful in regards to the home section (only for mobile screens). Hopefully by the end of this project I will figure it out. If not, I am very confident this small, but annoying bug will be crushed in the very nearest future.

* **Bug**:

  When running all simulations on dev-tools for iPad Pro screens, the app works exactly as expected. However, when actually running the app on my personal iPad Pro, the main background image is NOT fixed, as if the background-attachment property set for the 'body' element is not working. I am still trying to wrap my head around this issue and I am confident it will be fixed very soon. As mentioned, when testing with dev-tools it works as expected.

## Deployment:

The Exoplanet Project was developed on GitPod using git and GitHub to host the repository.

### Deploying The Exoplanet Project to Heroku:

* 1: **Create** a requirements.txt file using the following command.
```bash
pip3 freeze > requirements.txt
```
* 2: **Create<** a Procfile with the following command.
```bash
echo web: python3 app.py > Procfile
```
* 3: **Push** these newly created files to your repository.
* 4: **Create** a new app for this project on the Heroku Dashboard.
* 5: **Select** your deployment method by clicking on the **deployment** method button and select **GitHub**.
* 6: On the dashboard, **set** the following config variables:

**Key**|**Value**
:-----:|:-----:
IP|0.0.0.0
PORT|8080
MONGO\_URI|mongodb+srv://<username>:<password>@<cluster\_name>-qtxun.mongodb.net/<database\_name>?retryWrites=true&w=majority
SECRET\_KEY|"your\_secret\_key"
* 7: Click the deploy button on the Heroku dashboard.
* 8: The app has been deployed the Heroku.

## Credits:

* [NASA](https://exoplanets.nasa.gov/resources/2159/planet-hop-from-trappist-1e/)
* [Wikipedia](https://en.wikipedia.org/wiki/Lists_of_exoplanets)

### Content:

The first paragraph from **About** page, starting: "Exoplanets are planets that orbit a star other than our sun. The prefix exo comes from the Greek...  " has been taken from the webiste [Earthsky.org](https://earthsky.org/astronomy-essentials/what-are-exoplanets#:~:text=Exoplanets%20are%20planets%20that%20orbit,1%2C000%20more%20more%20awaiting%20confirmation.). 

### Media:

* The **main background image** was sourced from [wallup.net](https://wallup.net/trappist-1e-nasa-space-space-travel/)
* The image representing exoplanet **51 Pegasi b** was sourced from [commons.wikimedia.org](https://commons.wikimedia.org/wiki/File:Artist%E2%80%99s_Impression_of_a_Jupiter_twin_orbiting_HIP_11915_Image.jpg)
* The image representing exoplanet **Kepler-186f** was sourced from [sci-news.com](http://www.sci-news.com/astronomy/science-kepler186f-potentially-habitable-earth-like-exoplanet-01864.html)
* The image representing exoplanet **Proxima Centauri b** was sourced from [theusbport.com](https://theusbport.com/proxima-centauri-b-may-be-a-candidate-for-human-colonization/18550)
* The image representing exoplanet **HD 209458 b** was sourced from [NASA](https://www.nasa.gov/press/2014/july/hubble-finds-three-surprisingly-dry-exoplanets/)
* The image representing exoplanet **Kepler-4b** was sourced from [wired.com](https://www.wired.com/story/neptune-is-a-windy-chilly-and-baffling-planet-lets-go/)
* The image representing exoplanet **K2-18b** was sourced from [khabarhub.com](https://english.khabarhub.com/2019/23/45787/)
* The image representing exoplanet **PH1b** was sourced from [theverge.com](https://www.theverge.com/2015/8/13/9149549/young-jupiter-like-exoplanet-directly-imaged-by-earth-based-telescope)
* The image representing exoplanet **TRAPPIST-1d** was sourced from [reddit.com](https://www.reddit.com/r/KerbalSpaceProgram/comments/ca7i2w/trappist1d_in_ksp/)
* The image representing exoplanet **Gliese 581c** was sourced from [spiegel.de](https://www.spiegel.de/international/zeitgeist/the-twin-earths-of-gliese-581-two-exoplanets-may-support-life-a-721840.html)
* The image representing exoplanet **WASP-12b** was sourced from [princeton.edu](https://www.princeton.edu/news/2020/01/07/planet-wasp-12b-death-spiral-say-scientists)
* The image representing exoplanet **KELT-9b** was sourced from [irishnews.com](https://www.irishnews.com/magazine/science/2017/06/06/news/everything-you-need-to-know-about-kelt-9b---the-newly-discovered-planet-that-is-hotter-than-most-stars-1047146/)
* The image representing exoplanet **Kepler-10b** was sourced from [NASA](https://www.nasa.gov/mission_pages/kepler/multimedia/images/kepler10b_images.html)
* The **photo representing the location of exoplanet's mass** on wikipedia was sourced from [wikipedia.org](https://en.wikipedia.org/wiki/Kepler-186f)

