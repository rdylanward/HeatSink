<h1 align="center">MS3 Project - HeatSink</h1>

[View the live project here.](https://heatsink-flask-project.herokuapp.com/)

Based on an actual requirement, a company has a series of electric heaters installed in various offices and their canteen. During the colder months, the electric heaters would be left on constantly (in some cases, overnight.), even when they were not needed or the room was too hot. When turning them on in the morning to warm up the area, employees would tend to turn the thermostats to the highest setting and leave them there for the duration. On top of that, when a room would get too hot, rather than turn the thermostat down, employees would tend to open a window and let the cool air in, leaving the heater running at full tilt the entire time. As you may have guessed, this used caused the company to consume unnecessary amounts of electricity.

Being part of the Origin Green initiative coupled with a strong desire to reduce their carbon footprint to zero, the company tasked me to install a system to both control and lessen the usage of the electric heaters. As a cost-saving exercise (translation: being given a minute budget to work with), I elected to install a series of [Raspberry PI Zeros](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) coupled with [Pimoroni Automation Hats](https://shop.pimoroni.com/products/automation-hat) to achieve this goal. As the electric heaters were strategically grouped with multiple heaters wired to the same electrical panels, this allowed me to group multiple heaters on one controller and save 60% on costs compared to commercial HVAC solutions.

At the start, with a bit of education on turning the thermostats down and logically programmed scheduled tasks, all was working well and the heaters were being controlled. However, manipulating the controllers had to be carried out via a series of commands executed via batch files, using command lines. This left the usage of the system awkward, cumbersome, leaving the employees less likely to use the system and reverting to their old ways. A more user-friendly front-end was required to engage the end-user to get the full benefit of the design. This project is the answer to that need. Utilising Python, the Flask Framework, MongoDB, Materialize CSS, HTML5, CSS3 and JQuery, this application gives the end-user an easy to use, easy to access application to control the heaters when desired, as well as administration functionality for the manipulation of devices.

In our modern world, we tend to use our mobile phones for everything. I have designed this application targeting mobile phones. However, with the use of Materialize CSS, the application scales to larger devices (i.e. Tablets, Desktops, etc…) if a mobile phone is not available.



-   ### Responsive Screenshots

    -   #### iPhone 6-7-8 (375 x 677)

    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/iPhone_6-7-8_index.html.png"></h2>
    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/iPhone_6-7-8_heaters.html.png"></h2>
    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/iPhone_6-7-8_sidenav.png"></h2>

    -   #### iPhone X (375 x 812)

    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/iPhone_X_heaters.html.png"></h2>
    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/iPhone_X_settings.html.png"></h2>

    -   #### iPad (768 x 1024)

    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/iPad_heaters.html.png"></h2>
    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/iPad_settings.html.png"></h2>

    -   #### MacBook Air (1440 x 990)

    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/MacBook_Air_heaters.html.png"></h2>
    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/MacBook_Air_settings.html.png"></h2>

    -   #### 24" Monitor (1920 x 1080)

    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/Desktop_index.html.png"></h2>
    <h2 align="center"><img src="https://github.com/rdylanward/HeatSink/blob/master/static/img/screenshots/Desktop_heaters.html.png"></h2>

## User Experience (UX)

-   ### User stories

    -   #### Administration Goals

        1. - Login with the admin login details -
        2. - Add a new member to the database -
        3. - Add a new controller to the system -
        4. - Add heaters to the controllers -
        5. - Add members to the heater groups to allow access -

    -   #### Returning Administrator Goals

        1. - Update details for members, controllers, heaters and member groups -
        2. - Remove members, controllers, heaters and member groups from database -

    -   #### Member Goals
        1. - Login to the application -
        2. - Switch heaters on and off -

-   ### Design
    -   #### Colour Scheme
        -   I chose red, green and grey accents for the heaters to indicate off, on and disabled states. Off-white was chosen for the background of the heater cards and the sidenav menu.
    -   #### Typography
        -   Montserrat was chosen for its clean design and easy to read style. Sans Serif was chosen as the back-up in the event the main font does not load. Future changes to typography possible.
    -   #### Imagery
        -   Implemented a fixed image related to the type of application this is. A dark filter is layered over the image to allow for the elements to stand out.

*   ### Wireframes

    -   Wireframes PDF File - [View](https://github.com/rdylanward/HeatSink/blob/master/static/docs/MS3_Wireframes.pdf)

## Features

-   ### Responsive on all device sizes
    -   #### Major and common devices were chosen for the responsive design, ranging from:
        -   Samsung
        -   Apple
        -   Google
        -   Standard Laptop and Desktop screen sizes

-   ### Interactive elements include:
    -   #### A fully operational login page
    -   #### Menu elements visible depending upon user status (whether an admin or not).
    -   #### Heaters presented according to access permissions of the logged in user.
    -   #### Settings page gives admins the ability to add and remove users (members), controllers the heaters are associated with, the heaters, heater member groups and deletion of any asset configured on the system.
    -   #### A sidenav menu the slides out from the left on mobiles and tablets.
    -   #### A responsive design that responds to all devices.

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

### Testing User Stories from User Experience (UX) Section

-   #### Administration Goals

    1. Login with the admin login details.

        1. - Logged in with the admin details and was taken straight to the heaters page. -
        2. - All relavent heaters were displayed when the heaters page was rendered. -

    2. Add a new member to the database.

        1. - Added two standard members, hsdemo and hsdemo2. -

    3. Add a new controller to the system.
        1. - Added the HS2 controller to the database. -

    4. Add heaters to the controllers.
        1. - Added multiple heaters across both controllers configured. -
        2. - Heaters displayed upon logging in (perrmissions permitting). -

    5. Add members to the heater groups to allow access.
        1. - Added the created members to the member groups, spread across them to demonstrate permissions. -
        2. - The heaters displayed correctly based on the groups the users were added to. -

-   #### Returning Administrator Goals

    1. Update details for members, controllers, heaters and member groups.

        1. - Changed passwords on members and tested the logins. The members logged in with the new passwords. -
        2. - Changed the address of the controllers. -
        3. - Switched the heaters between enabled and disabled. Switched the heaters between controllers. Changed the location and name details of the controllers.-
        3. - Switched the members between the various member groups.-

    2. Remove members, controllers, heaters and member groups from database.

        1. - Created a new test member and removed it from the database. -
        2. - Created a new test controller and removed it from the database. -
        3. - Created a new test heater and removed it from the database. -
        4. - Created a new test member, added it to a member group, removed it from the group and removed the test member from the database. -

-   #### Member Goals

    1. Login to the application.

        1. - Both users logged on, displayed the proper menu and displayed the relevant heaters. -

    2. Switch heaters on and off.

        1. - Switched the heateers on and off multiple times. -

### Further Testing

-   The Website was tested on Google Chrome, Firefox, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone6, iPad & Samsung Note 10+.
-   All menu links were tested across all pages to ensure that they all go to the correct page.
-   All of the buttons were tested, across all pages, to ensure that they go to the links specified or carried out the desired action.

### Known Bugs

-   The initial devices (setup for the company), previously configured, have been deployed and are working. The test device configured identically is not switching the relays. To complete the project, I have configured the heater button to simulate the action of the relay using the database. I have attached the code for the relays [here](https://github.com/rdylanward/HeatSink/blob/master/static/docs/relay.py). The installation instructions can be found [here](https://github.com/rdylanward/HeatSink/blob/master/static/docs/Configure_HeatSink_Automation_Hat.txt)

### Future Development

-   Resolve the issue with the switching the relays on the device and re-implement the remote access.
-   Add a mechanism to create and update schedules on the controllers.
-   Add a documentation page.

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

-   Method POST button code provided by Andrew Clark(https://stackoverflow.com/questions/66618070/flask-differentiating-between-different-post-requests) and adjusted for my requirements.

-   GitHub instructions provided in the Development section of this ReadMe was provided by [GitHub](https://github.com/) and [Code Institute](https://codeinstitute.net/) with links updated to this project.

### Content

-   All content was written and edited by Dylan Ward using the [GitPod](https://www.gitpod.io/) editor.

-   Colour pallettes were chosen with the aid of [Paletton](https://paletton.com/), [Flat UI Colors 2](https://flatuicolors.com/) and [0to255.com](https://www.0to255.com/).

### Media

-   All images were provided, royalty free, by [Burst](https://burst.shopify.com/).

-   The screenshots for the virtual device views of the website at the beginning of this document were captured with the aid of the Microsoft Snip-it tool.

-   Image manipulation was completed with the aid of [GIMP](https://www.gimp.org/) and [Tiny PNG](https://tinypng.com/).

### Acknowledgements

-   My Mentor, Gerard McBride, for continuous support and timeless advice keeping me on the right track.

-   The Tutor support at Code Institute for their support in times of need and aiding in answering all queries.