<h1 align="center">MS3 Project - HeatSink</h1>

[View the live project here.](https://heatsink-flask-project.herokuapp.com/)

Based on an actual requirement, a company has a series of electric heaters installed in various offices and their canteen. During the colder months, the electric heaters would be left on constantly (in some cases, overnight.), even when they were not needed or the room was too hot. When turning them on in the morning to warm up the area, employees would tend to turn the thermostats to the highest setting and leave them there for the duration. On top of that, when a room would get too hot, rather than turn the thermostat down, employees would tend to open a window and let the cool air in, leaving the heater running at full tilt the entire time. As you may have guessed, this used caused the company to consume unnecessary amounts of electricity.

Being part of the Origin Green initiative coupled with a strong desire to reduce their carbon footprint to zero, the company tasked me to install a system to both control and lessen the usage of the electric heaters. As a cost-saving exercise (translation: being given a minute budget to work with), I elected to install a series of [Raspberry PI Zeros](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) coupled with [Pimoroni Automation Hats](https://shop.pimoroni.com/products/automation-hat) to achieve this goal. As the electric heaters were strategically grouped with multiple heaters wired to the same electrical panels, this allowed me to group multiple heaters on one controller and save 60% on costs compared to commercial HVAC solutions.

At the start, with a bit of education on turning the thermostats down and logically programmed scheduled tasks, all was working well and the heaters were being controlled. However, manipulating the controllers had to be carried out via a series of commands executed via batch files, using command lines. This left the usage of the system awkward, cumbersome, leaving the employees less likely to use the system and reverting to their old ways. A more user-friendly front-end was required to engage the end-user to get the full benefit of the design. This project is the answer to that need. Utilising Python, the Flask Framework, MongoDB, Materialize CSS, HTML5, CSS3 and JQuery, this application gives the end-user an easy to use, easy to access application to control the heaters when desired, as well as administration functionality for the manipulation of devices.

In our modern world, we tend to use our mobile phones for everything. I have designed this application targeting mobile phones. However, with the use of Materialize CSS, the application scales to larger devices (i.e. Tablets, Desktops, etc…) if a mobile phone is not available.

When testing this application, you are controlling actual mock devices (the live test can be found [here](https://github.com/rdylanward/HeatSink/blob/master/static/docs/video/live_test.mp4)...). I have set up a controller (using DDNS) that is being accessed remotely by the application. I have set up three mock devices, the first two of which I would like to keep intact. When testing the admin functionality, I kindly request you only make changes to the third device named “demo”. The remaining two were set up solely to test the user functionality.



-   ### Responsive Screenshots

    -   #### iPhone 6-7-8 (375 x 677)

    <h2 align="center"><img src="#"></h2>

    -   #### iPhone X (375 x 812)

    <h2 align="center"><img src="#"></h2>

    -   #### iPad (768 x 1024)

    <h2 align="center"><img src="#"></h2>

    -   #### MacBook Air (1440 x 990)

    <h2 align="center"><img src="#"></h2>

    -   #### 24" Monitor (1920 x 1080)

    <h2 align="center"><img src="#"></h2>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. - Introduce the site and welcome new users -
        2. - Describe to new users who the owners are and there ethos -
        3. - Provide a basic description of the features -
        4. - Provide new users with clear and concise navigation throughout the site -
        5. - Get new users to try the map feature and explore new destinations and plan activities -
        6. - Provide the opportunity for new users to book a holiday destination -

    -   #### Returning Visitor Goals

        1. - Steer returning clients to the destinations page to explore new destinations -
        2. - Ensure that returning clients can book further holidays -
        3. - Enable users to sign-up for the company newsletter to receive holiday reviews, current deals, and company news -

    -   #### Frequent User Goals
        1. - Enable clients to explore further holiday destinations -
        2. - Enable clients to book further holidays -

-   ### Design
    -   #### Colour Scheme
        -   I chose  a light colour scheme based on a light blue (Peter River) to give a holiday kind of feel to the site with a bright colour scheme.
    -   #### Typography
        -   Two fonts were chosen as for the project, Amatic SC and Architects Daughter. Both fonts are handwriting style fonts chosen to give a postcard feel to the site. Sans Serif was chosen as the back-up in the event the main font does not load. Future changes to typography possible.
    -   #### Imagery
        -   Multiple images based on travel were chosen with a combination of images based on maps and actual destinations. One of the images is of a traveller overlooking a valley chosen to represent one of the owners of the fictional company.

*   ### Wireframes

    -   Wireframes PDF File - [View](https://github.com/rdylanward/HeatSink/blob/master/static/docs/wireframes/MS3_Wireframes.pdf)

## Features

-   ### Responsive on all device sizes
    -   #### Major and common devices were chosen for the responsive design, ranging from:
        -   Samsung
        -   Apple
        -   Google
        -   Standard Laptop and Desktop screen sizes

-   ### Interactive elements include:
    -   #### An interactive map that allows you to search for destinations
    -   #### An autocomplete function for the search text box
    -   #### Zooming into the destination brings up detailed information of local businesses, eateries and sites along with links to Street View if available.
    -   #### A sticky menu that hides until you start to scroll the page
    -   #### Modals that provide confirmation of the actions taken (i.e. Signing up for the newsletter, booking a holiday and contacting the company)

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JQuery](https://jquery.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Python v3.8:](https://www.python.org/)
    - Python v3.8 was used to code both the application and the physical controller.
1. [Paramiko:](https://www.python.org/)
    - Paramiko implementation of the SSHv2 protocol, providing both client and server functionality.
1. [pgpio:](http://abyz.me.uk/rpi/pigpio/)
    - Pigpio is a library for the Raspberry PI which allows the control of the General Purpose Input Outputs (GPIO).
1. [Raspbian:](https://www.raspberrypi.org/software/)
    - The Raspberry PI OS based on Debian Linux. The light or headless version was used for the controller.
1. [Flask:](https://flask.palletsprojects.com/en/2.0.x/)
    - A framework that allows the utilisation of Python in your web-based projects.
1. [Jinja:](https://jinja.palletsprojects.com/en/3.0.x/)
    - Included with the Flask Framework, Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax.
1. [Werkzeug:](https://www.palletsprojects.com/p/werkzeug/)
    - Included with the Flask Framework, Werkzeug is a comprehensive WSGI web application library.
1. [MongoDB:](https://www.mongodb.com/)
    - MongoDB is a general purpose, document-based (or NoSQL), distributed database.
1. [Materialize CSS:](https://https://materializecss.com/)
    - Materialize CSS was chosen for its ability to provide more precise control over responsive design.
1. [CSS3:](https://en.wikipedia.org/wiki/CSS)
    - CSS3 was used to aid in the aesthetic presentation of the project.
1. [jQuery:](https://jquery.com/)
    - jQuery was essential for enabling the interactive elements like the sticky menu and hiding/unhiding the modals.
1. [Heroku:](https://heroku.com/)
    - Heroku is utilised to host the project.
1. [Gitpod:](http://gitpod.io/)
    - GitPod was chosen for the coding of the site. Gitpod has a great set of features for programming multiple languages and connects directly to GitHub.
1. [Git](https://git-scm.com/)
    - Git was used in conjunction with Gitpod for version control to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub utilised as a repository for the code.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Montserrat' and 'IM Fell English' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used for the brand. the bullet points on the membership page and for the quotes used throughout.
1. [GIMP:](https://www.gimp.org/)
    - Gimp (Graphic Image Manipulation Program) was used for resizing cropping and editing images for the website.
1. [Autoprefixer:](http://autoprefixer.github.io/)
    - Autoprefixer was used to ensure the code has all relevant vendor prefixes.
1. [Tiny PNG:](https://tinypng.com/)
    - Tiny PNG was used to reduce the file size of the images to aid in faster loading times.
1. [Burst:](https://burst.shopify.com/)
    - Burst was used to obtain royalty free images for the site.
1. [Devoth‘s HEX 2 RGBA Color Calculator:](http://hex2rgba.devoth.com/)
    - Devoth‘s HEX 2 RGBA Color Calculator was used to aid in converting hex colurs to rgb and rgba.
1. [Responsively:](https://responsively.app/)
    - Responsively provides an array of virtual devices to test a website's responsive design.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) - [Results](https://github.com/rdylanward/HeatSink/tree/master/static/docs/validation/html5)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/rdylanward/HeatSink/tree/master/static/docs/validation/css3)
-   [BeautifyTools JavaScript Validator](https://beautifytools.com/javascript-validator.php) - [Results](https://github.com/rdylanward/HeatSink/tree/master/static/docs/validation/jscript)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. Introduce the site and welcome new users.

        1. - New users are greeted with a welcoming header hero and motivational quote. -
        2. - The very next section is a desription of the company and its owners. -

    2. Describe to new users who the owners are and there ethos.

        1. - Scroll down to the next section on the home page and the user will find a desription of the company and its owners. -

    3. Provide a basic description of the features.
        1. - On the home page the user will find a link to the bookings page in the about us section. -
        2. - The user will find a brief description and a link to the destinations page. -

    4. Provide new users with clear and concise navigation throughout the site.
        1. - The user is provided with a well defined and easy to use menu. -
        2. - Multiple links and buttons are provided to all pages. -

    5. Get new users to try the map feature and explore new destinations and plan activities.
        1. - The user is is enticed to follow the link to the destinations page in the section provided on the home page. -
        2. - Once on the destinations page, the user can navigate the map to find destinations they are interested in. -

    6. Provide the opportunity for new users to book a holiday destination.
        1. - Multiple links are provided to take the user to the bookings page. Once there, the user can complete the form to organise a booking. -

-   #### Returning Visitor Goals

    1. Steer returning clients to the destinations page to explore new destinations.

        1. - Upon returning to the site, the user is provided with multiple links to the destinations page. Once there the user can explore any and all desired destinations. -

    2. Enable clients to book further holidays.

        1. - Once the user has explored the desired destinations, links are provided to the bookings page where they can complete the form and make a booking. -

    3. Enable users to sign-up for the company newsletter to receive holiday reviews, current deals, and company news.

        1. - In the footer section on all pages, an input is provided where the user can enter there email and get signed up to the newsletter. -

-   #### Frequent User Goals

    1. Enable clients to explore further holiday destinations.

        1. - The map is always available on the destinations page to explore further destinations. -

    2. Enable clients to book further holidays.

        1. - Multiple links are available for returning users to get to the bookings page. If the user already has a destination in mind, they can go straight to the bookings page and complete the form. -

### Further Testing

-   The Website was tested on Google Chrome, Firefox, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone6, iPad & Samsung Note 10+.
-   All menu links were tested across all pages to ensure that they all go to the correct page.
-   All of the buttons were tested, across all pages, to ensure that they go to the links specified or carried out the desired action.

### Known Bugs

-   The map markers initially worked but stopped working after fixing a fault flagged by the validator. The code was restored to its original version, but the markers still do not work.

### Future Development

-   Create a members login to save bookings details.
-   Link the member login to Google Maps to save marker information of destinations searched.
-   Create a database to store all relevant details.
-   Fix the markers feature for the map.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/rdylanward/HeatSink)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://guides.github.com/features/pages/) for a tutorial on the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com/rdylanward/HeatSink/heatsink.py) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/rdylanward/HeatSink)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/rdylanward/HeatSink)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   The Javascript for the modals was originally written by [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) and repurposed to aid in the function of the modal.

-   The Javascript for the Map was originally written for and provided by the Google Maps Platform Maps JavaScript API Guide [Google Maps Platform](https://developers.google.com/maps) and repurposed to aid in the function and design of the map.

-   The Javascript for the Sticky Menu was originally written by [W3Schools](https://www.w3schools.com/howto/howto_js_navbar_sticky.asp) and repurposed to aid in the function of the sticky menu.

-   The Javascript for the Mobile Menu was originally written by [W3Schools](https://www.w3schools.com/howto/howto_js_mobile_navbar.asp) and repurposed to aid in the function of the mobile menu.

-   GitHub instructions provided in the Development section of this ReadMe was provided by [GitHub](https://github.com/) and [Code Institute](https://codeinstitute.net/) with links updated to this project.

### Content

-   All content was written and edited by Dylan Ward using the [Brackets](http://brackets.io/) editor.

-   Colour pallettes were chosen with the aid of [Paletton](https://paletton.com/), [Flat UI Colors 2](https://flatuicolors.com/) and [0to255.com](https://www.0to255.com/).

### Media

-   All images were provided, royalty free, by [Burst](https://burst.shopify.com/).

-   The screenshots for the virtual device views of the website at the beginning of this document were captured with the aid of Google Chrome developer tools.

-   Image manipulation was completed with the aid of [GIMP](https://www.gimp.org/) and [Tiny PNG](https://tinypng.com/).

### Acknowledgements

-   My Mentor, Gerard McBride, for continuous support and timeless advice keeping me on the right track.

-   The Tutor support at Code Institute for their support in times of need and aiding in answering all queries.