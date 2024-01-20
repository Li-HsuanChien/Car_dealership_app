<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# Budget Management System

### Built With

* [![Django][Django]][Django-url]
* [![Flask][Flask]][Flask-url]
* [![Node][Node.js]][Node-url]
* [![Express][Express.js]][Express-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [ibm-clodant](https://www.ibm.com/products/cloudant?utm_content=SRCWW&p1=Search&p4=43700074369655661&p5=e&gclid=Cj0KCQiA2KitBhCIARIsAPPMEhLEUBpVAYLRDMkTIaoYTSBzRRyAHgda97W0ryozhh0pjTN3MFVXpeIaAoxmEALw_wcB&gclsrc=aw.ds)
* [ibm Natural Language Understanding](https://cloud.ibm.com/apidocs/natural-language-understanding)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Overview

[![Product Name Screen Shot One][product-screenshot-one]](https://github.com/Li-HsuanChien/Car_dealership_app)

<hr>

[![Product Name Screen Shot Two][product-screenshot-two]](https://github.com/Li-HsuanChien/Car_dealership_app)

<hr>

[![Product Name Screen Shot Three][product-screenshot-three]](https://github.com/Li-HsuanChien/Car_dealership_app)

<hr>

The app is a comprehensive dealership and user management platform designed to streamline the process of discovering, reviewing, and interacting with independent car dealerships. Users can easily explore a list of dealerships with detailed information such as city, address, zip, and state. The app enables user registration and authentication for a personalized experience. Additionally, users can submit and read reviews for independent dealerships, with sentiments labeled for each review.

- ## Features

    **Discover Dealerships:**
    - Access a user-friendly list of independent dealerships.
    - View detailed information, including city, address, zip, and state.

    **User Registration and Authentication:**
    - Register as a user to unlock personalized features.
    - Authenticate securely for a seamless and secure experience.

    **Review Dealerships:**
    - Share your experiences by submitting reviews for independent dealerships.
    - Read reviews from other users to make informed decisions.

    **Sentiment Analysis:**
    - Each review is analyzed for sentiment.
    - Sentiments (positive, neutral, or negative) are labeled for quick understanding.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

- [Python](https://www.python.org/)
- [Node.js](https://nodejs.org/en/) installed on your machine.
- [npm (Node Package Manager)](https://www.npmjs.com/) installed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Running the App

**Manual commands**

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Li-HsuanChien/budget_manage_system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd budget_management_system
    ```

3.  Set up a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On Linux/macOS:

    ```bash 
    source venv/bin/activate
    ```

5. Navigate to the functions directory:

    ```bash
    cd functions
    ```

6. Install dependencies for end point tool 1:

    ```bash
    npm init -y
    npm install -s @cloudant/cloudant 
    npm install express 
    ```
7. Start end point tool 1:

    ```bash
    node get-dealership.js
    ```

8. Start another terminal:

    ```
    shortcut: ctrl + shift + `
    ```
    -start terminal manually

9. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On Linux/macOS:

    ```bash 
    source venv/bin/activate
    ```
10. Navigate to the functions directory:

    ```bash
    cd functions
    ```

11. Install dependencies for end point tool 2:

    ```bash
    python -m pip install --upgrade pip
    python -m pip install Cloudant
    python -m pip install Flask
    ```

12. Start end point tool 2:

    ```bash
    python reviews.py
    ```
13. Start another terminal:

    ```
    shortcut: ctrl + shift + `
    ```
    -start terminal manually

14. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On Linux/macOS:

    ```bash 
    source venv/bin/activate
    ```

15. Navigate to the server directory:

    ```bash
    cd server
    ```

16. Install dependencies for main file:

    ```bash
    python -m pip install -U -r requirements.txt
    ```

17. Migrate Django server and start

    ``` bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

    ```

18. The application will be listening to `http://localhost:8000/` by default.

19. Create super user by executing:

    ```bash
    python manage.py createsuperuser
    ```

20. Direct to `http://localhost:8000/admin` to utilize django admin tool to set up courses and users.

21. Direct to `http://localhost:8000/onlinecourse` to use the main application




<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

**Course Management:**
  
  -create super user using ```bash python manage.py createsuperuser```
  -navigate to http://localhost:8000/admin and login
  -edit django models
  -navigating to dealers, models, makers to customize dealerships, car models, and car makers

**Read reviews:**
- click on dealership names to inspect dealership reviews
- read label icons to easily understand the sentiment of the review

**Review Dealerships:**
    - login through nav bar
    - click the "add review" button to add review to relevant dealerships

**Review details:**
    - Each review is analyzed for sentiment
    - Add review, past transaction records and product model
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>
  
## Awaiting Updates

1. **Container and hosting**
   - Host websites and automate project installation
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Feel free to contribute to the development of this  system by creating issues or pull requests.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

This project is licensed under the Apache 2.0 - see the [LICENSE](LICENSE) file for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Node.js]: https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white
[Node-url]: https://nodejs.org
[Express.js]: https://img.shields.io/badge/Express.js-404D59?style=for-the-badge
[Express-url]: https://expressjs.com/
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[product-screenshot-one]: images/snapshot1.jpg
[product-screenshot-two]: images/snapshot2.jpg
[product-screenshot-three]: images/snapshot3.jpg
[contributors-shield]: https://img.shields.io/github/contributors/Li-HsuanChien/budget_manage_system.svg?style=for-the-badge
[contributors-url]: https://github.com/Li-HsuanChien/budget_manage_system/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Li-HsuanChien/budget_manage_system.svg?style=for-the-badge
[forks-url]: https://github.com/Li-HsuanChien/budget_manage_system/network/members
[stars-shield]: https://img.shields.io/github/stars/Li-HsuanChien/budget_manage_system.svg?style=for-the-badge
[stars-url]: https://github.com/Li-HsuanChien/budget_manage_system/stargazers
[issues-shield]: https://img.shields.io/github/issues/Li-HsuanChien/budget_manage_system.svg?style=for-the-badge
[issues-url]: https://github.com/Li-HsuanChien/budget_manage_system/issues
[license-shield]: https://img.shields.io/github/license/Li-HsuanChien/budget_manage_system.svg?style=for-the-badge
[license-url]: https://github.com/Li-HsuanChien/budget_manage_system/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/lihsuan-chien/
