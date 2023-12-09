# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 [Book_Matcher] <a name="about-project"></a>

> Book Matcher is an innovative web application designed to provide personalized book recommendations based on individual personalities. Using advanced algorithms, it analyzes user responses to carefully crafted questions and suggests literature genres and specific books tailored to each user's unique preferences.

Link to (FRONT END CODE)["https://github.com/Rishi-Mishra0704/book-match-frontend"]

**[Book_Matcher]**

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
<summary>Client</summary>
<ul>
<li>Next.js</li>
<li>Tailwind CSS</li>
<li>TypeScript</li>
</ul>
</details>
<details>
<summary>Server</summary>
<ul>
<li>Django</li>
<li>Django Rest Framework</li>
</ul>
</details>
<details>
<summary>Database</summary>
<ul>
<li>PostgreSQL</li>
</ul>
</details>
### Key Features <a name="key-features"></a>

<ul>
<li>Login page</li>
<li>Add Students</li>
<li>Find Books</li>


</ul>
<h1>Before continuiing with the project please watch the video</h1>

<h3>Video presentation</h3>
<a href="https://drive.google.com/file/d/1bs84yFmiVkm-vmsStWG0C9HwRdqGXVRi/view?usp=sharing">Click here</a>
<h3>🚀 Live Demo</h3>
<a href="https://book-match-frontend.vercel.app/">Live Demo</a>
## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Django Rest Framework</li>
    <li>PostgreSQL</li>
    <li>Psycopg2</li>
</ul>

### Setup

Clone this repository to your desired folder:

Example commands:
```bash
cd my-folder
git clone https://github.com/Rishi-Mishra0704/book-match-backend.git
```
### Database Setup

1. **Create a PostgreSQL Database:**
   - Set up a PostgreSQL database and make a note of the database name, username, and password.

2. **Update `settings.py`:**
   - Open the `settings.py` file in your Django project.

3. **Add Database Configuration:**
   - Locate the `DATABASES` section in `settings.py` and update it with the following code:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your-db-name',
             'USER': 'your-username',
             'PASSWORD': 'your-password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

   - Replace `'your-db-name'`, `'your-username'`, and `'your-password'` with your actual database credentials.

Now your Django project is configured to use the PostgreSQL database you've set up.


### Install

1. Create a virtual environment and activate it:
   - For Windows:
     ```powershell
     python -m venv env
     & desired_folder/env/Scripts/Activate.ps1
     ```

   - For Linux and Mac:
     ```bash
     python -m venv env
     source env/bin/activate
     ```

   Ensure that you have the necessary execution permissions on the activation script.

2. Install the dependencies:
```bash
   pip install -r requirement.txt
 ```
 
3. Run the following commands to create the Models in database :
```bash
python manage.py makemigrations
python manage.py migrate
```
### Usage

To run the project, execute the following command:

```bash
cd desired-folder/vendor-management/vendorManagement
 python manage.py runserver
 ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

👤 **Rishi_Mishra**

- GitHub: [@githubhandle](https://github.com/Rishi-Mishra0704)
- Twitter: [@twitterhandle](https://twitter.com/RishiMi31357764)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/rrmishra/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

> Show your support by giving a ⭐️ if you like this project!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank Reach Best for giving me the opportunity to work on this project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
