# Django DIY Blog

----
This web application creates a very basic blog site using Django.
The site allows blog authors to create text-only blogs using the Admin site, and any logged in user to add comments via a form.
Any user can list all bloggers, all blogs, and detail for bloggers and blogs (including comments for each blog).

The models for this site are as shown below:

![Django Blog Models](./blog/static/images/diy_django_mini_blog_models.png)


## Quick Start

To get this project up and running locally on your computer:

Assuming you have Python setup, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python3` to start Python):
   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```

Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site 
Create a few test objects of each type. 
Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
