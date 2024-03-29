# Django Personal Blog

Django Personal Blog is a basic blog application built using the Django web framework. It includes features such as displaying blog posts, creating and managing tags, creating and managing comments, pagination, searching, and more. It also uses the TinyMCE rich text editor for creating and editing blog posts. Recently I have added Django Rest Framwork To this Project. You can see the site [Here](https://jethliyabalaji-blogs.up.railway.app/)
& API [Here](https://jethliyabalaji-blogs.up.railway.app/api/)

## Features
- CRUD functionality for blog posts
- Ability to view blogs related to a specific tag
- Rich text editor for creating and editing blog posts
- Search functionality for blog posts
- Pagination for blog post
- RESTful APIs for accessing and managing blog posts, tags, and comments through Django Rest Framework.

## Requirements
- Python 3.x
- Django 3.x
- DRF 3.x
- & [More](https://github.com/jethliya-balaji/Django-Personal-Blog/blob/main/requirements.txt)

## Installation



- Clone the repository

    `https://github.com/jethliya-balaji/Django-Personal-Blog.git`
- Create a virtual environment & Activate the virtual environment (optional)

    `python -m venv env`

    `source env/bin/activate` or `source env/Scripts/activate` or Based on your terminal/operating system. 
- Install the requirements

    `pip install -r requirements.txt`

- Note :
    1. `.env.example` file is provided in the project root directory as an example of environment variables you need to set before running server.

        ```
        SECRET_KEY=Django secret key
        DEBUG=Debug mode, set to TRUE or FALSE
        ALLOWED_HOSTS=127.0.0.1 localhost

        #### Only required if you are using postgresql ####
        PGDATABASE=
        PGUSER=
        PGPASSWORD=
        PGHOST=
        PGPORT=
        ```

        To generate a new key, we can use the `get_random_secret_key()` function present in `django.core.management.utils`. This function returns a 50 character string that consists of random characters. This string can be used as a SECRET_KEY.
        ```
        # importing the function from utils
        from django.core.management.utils import get_random_secret_key

        # generating and printing the SECRET_KEY
        print(get_random_secret_key())
        ```
        Run above code in terminal (same folder as manage.py file with virtual environment active)

    2. Make sure to set up the correct database settings in the settings.py file. Use sqlite3 for local local machine & postgresql while deploying.
        ```

        # Database
        # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

        # DATABASES = {
        #     'default': {
        #         'ENGINE': 'django.db.backends.postgresql',
        #         'NAME': os.environ.get('PGDATABASE'),
        #         'USER': os.environ.get('PGUSER'),
        #         'PASSWORD': os.environ.get('PGPASSWORD'),
        #         'HOST': os.environ.get('PGHOST'),
        #         'PORT': os.environ.get('PGPORT'),
        #     }
        # }
        ```

- Run migrations & collectstatic

    `python manage.py makemigrations`

    `python manage.py migrate`
- Run the development server

    `python manage.py runserver`
- Visit http://localhost:8000 in your web browser to view the application


## File Structure
```
📦Django-Personal-Blog
 ┣ 📂blog
 ┃ ┣ 📂api
 ┃ ┃ ┣ 📜serializers.py
 ┃ ┃ ┣ 📜urls.py
 ┃ ┃ ┣ 📜views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📂migrations
 ┃ ┃ ┣ 📜0001_initial.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜utils.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂core
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┣ 📂css
 ┃ ┃ ┣ 📜bootstrap.css
 ┃ ┃ ┗ 📜prism.css
 ┃ ┣ 📂js
 ┃ ┃ ┣ 📜bootstrap.bundle.min.js
 ┃ ┃ ┣ 📜prism.js
 ┃ ┃ ┗ 📜tinymce.js
 ┃ ┗ 📂resource
 ┃ ┃ ┣ 📜dummy.png
 ┃ ┃ ┣ 📜favicon.svg
 ┃ ┃ ┗ 📜profile.jpg
 ┣ 📂templates
 ┃ ┣ 📂blog
 ┃ ┃ ┣ 📜about.html
 ┃ ┃ ┣ 📜base.html
 ┃ ┃ ┣ 📜blogs.html
 ┃ ┃ ┣ 📜blogs_related_to_tag.html
 ┃ ┃ ┣ 📜blog_detail.html
 ┃ ┃ ┣ 📜home.html
 ┃ ┃ ┗ 📜tags.html
 ┃ ┗ 📜404.html
 ┣ 📜.env.example
 ┣ 📜.gitignore
 ┣ 📜manage.py
 ┣ 📜Procfile
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜runtime.txt
```
The project is structured with the following main directories:
- blog: contains all the application's logic for blog posts & all RESTapi in api folder
- core: contains the project's settings and URL configurations
- static: contains static files such as CSS, JavaScript, and images
- templates: contains all the HTML templates used in the project

## Built With
[Django](https://docs.djangoproject.com/en/3.2/) - The web framework used

[TinyMCE](https://www.tiny.cloud/) - Rich text editor used in the project

[Bootstrap](https://getbootstrap.com/) & [Bootswatch](https://bootswatch.com)- Front-end framework used for styling

[PrismJS](https://prismjs.com/) - Syntax Highlighter

[Django Rest Framwork](https://www.django-rest-framework.org/) - The RESTAPI framework used to build APIs 

## Contribution
Please read [CONTRIBUTING](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details code of conduct, and the process for submitting pull requests to us.

## Support
If you need any help or have any questions, please feel free to contact me.

## Conclusion
The app is a great starting point for anyone looking to build a personal blog website using Django. It demonstrates the use of Django's built-in pagination, forms and the rich text editor for handling user input. The app is easy to customize and extend to suit your needs.

## Fun Section
The demo web site is up and running at [here](https://jethliyabalaji-blogs.up.railway.app/) but it may be temporarily down because the developer needs a coffee break. If you find the app helpful, feel free to buy the developer a coffee! [here]()

## Authors
Balaji Jethliya - Initial work - [GitHub](https://github.com/jethliya-balaji), [Twitter](https://twitter.com/jethliyabalaji)
