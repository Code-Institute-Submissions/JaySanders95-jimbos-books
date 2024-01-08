#Jimbo’s Books – Portfolio Project 5 – Full Stack Software Development

Img for I am responsive

## Live Site:

URL

## Repository:

URL

##Contents

-	Project Goals
-	UXD – User Experience Design
-	Marketing
-	Technologies Used
-	Testing
-	Deployment
-	Credits


## Project Goals

Jimbo’s Books is my final project for the code institute full stack developer course. It is a fictional store which sells books. They only sell books but the user can also leave reviews, apply for jobs which are being listed on the company.
On the landing page, the user is introduced to their ethos.

## Working Environment

After installing Django, Django and ElephantSQL, I copied the secret keys, stored them in an env.py file, which was placed in my .gitignore.

From this I added the relevant paragraphs to my settings.py as followed in tutorial videos @ CodeInstitute.

Once my allowed hosts were configured and I had created my first app using python3 manage.py startapp , my environment was ready to start coding.

# UXD – User Experience Design

When designing and creating this project it was important to keep the user experience at the forefront of my development, ensuring they could browse the store as smoothly as possible. This was achieved by following the 5 planes of UXD, as listed below;
-	Strategy
-	Scope
-	Structure
-	Skeleton
-	Surface


# Strategy plane

During this phase, I sat down and wondered why the Fictional book store would need a website, this would be to expand their business and allow them to grow. Reaching a bigger audience. Following this I sat down and explored what features they would require to achieve this:

-	The users would need to be able log in/ create an account.
-	The users would be able to purchase items, and receive feedback for this.
-	The users would be able to navigate the site easily and fluidly.
-	The users would be able to leave feedback, which would enhance the experience for other users.
-	The admin would be able to use CRUD functionality across different pages.

## Scope Plane

For the scope plane, I further progressed the ideas from the strategy plane, I outlined the best ideas and strengthened those, and there came a number of useful features to enhance the customer experience:
-	Home page / Landing page
-	Book Shop
-	Leave a Review
-	Staff Settings (for staff) which include CRUD functionality across the board within an easy accessible page
-	Careers
-	Account settings
-	Authentication across the site

## Structure plane

STRUCTURE PLANE IS CSS / colors / fonts etc. and what you used them for

Key Models:
-	User authentication -  using Django all-auth, I then moved their template to my root directory and amended to match my colour scheme.
-	Books – This is a display for all books currently in the store, with the ability to search based on name, genre, author etc. at the top of the screen. Once a book is selected, they are taken to a unique page for the book. The admin controls the stock from the staff settings page with full interactive CRUD functionality of what is displayed on this page. This includes a synopsis for the book, price etc. for a better experience. This included the Genre & Author models.
-	Bag – I used the CodeInstitute guide to implement a contexts.py bag, this would be available across all of the pages and allow the user to view it at any time, which would then allow the user to remove items from their bag or checkout. This was displayed using a FontAwesome Bag icon.
-	Checkout – within this, the user is allowed to create an order and purchase the selected items in the bag.
-	Reviews – These can be made from users that have registered an account with the site and the option is only displayed to those users. These will be displayed in their own section on the landing page and the admin will be able to delete these in their staff section. (for any rude/unsavoury reviews).
-	Careers – The user can view and apply for live jobs listed from the career model, the admin has full CRUD functionality over this and decides what is displayed on the web page.

## Skeleton Plane

I used wireframes for both mobile and webpage design, although during the development process, some ideas where amended or changed for better practise.

Home:

Mobile + web wireframes

Bookshop:

Mobile + web wireframes

Careers:

Mobile + web wireframes

Reviews:

Mobile + web wireframes

Staff Settings:

Mobile + web wireframes

Logout/Login/CreateAccount:

Mobile + web wireframes

Anymore -- 


Surface Plane:

These were tested for both mobile and web responses.

Nav Bar:
-	Is displayed at the top of all pages, this is extended via jinja templates
-	Clean and easy to use

Footer:
-	Same design/scheme as the navbar
-	Minimal with no cluttered text or links
-	The links all work and use “_blank” so they do not take the user from the page, they open a new tab instead.

Homepage:
-	Engaging photos on a carousel at the top of the screen, with an added catch quote.
-	A friendly about us
-	Reviews from previous users

BookShop:
-	Easy to navigate page with a clean amount of items per page depending on size. With only basic information unless the user clicks the item and is taken to their personalised page.
-	Search bar at the top of the screen for filtering products.

Reviews:
-	For user, they can view all reviews on the Landing page/Home page
-	For Authenticated User they can view all reviews and make reviews
-	For Staff they can Delete unsavoury reviews and can also view them both in their staff panel and the homepage.

Careers:
-	For user they can view and apply for jobs.
-	For staff they can view all jobs, delete, create and amend.

Staff Settings:
-	Personalised admin panel for all database CRUD functionality (Staff only), this includes books, careers and reviews.
Bag:
-	This includes a table of all items that have been added to the users bag, with the option to remove the items from their bag or to proceed to payment.

Checkout:
-	This allows users to create an order and pay for their items, this is a simple form for delivery address. The payments are handled by STRIPE API

Messages:
-	These are popup messages that appear for user experience, they will confirm when actions have been made or failed to have been made. Giving the user feedback to their actions.


## Marketing 

The marketing for this project was to ensure the business got as much exposure as possible. This was by adding a pop up the start for users (signed in or not) to be asked whether they wanted to receive a newsletter.

As the company was a fictional one, it had never been marketed. Therefore I created a Facebook page and a newsletter.

Links:


## SEO

To determine how a bookshop sells itself online, I had looked at competitor sites, these were websites such as Waterstones and WHSmith, when typing bookshop / Liverpool into Google searches, these two were amongst the top of the list, due to a couple of factors that they had keywords listed for the meta tags.

For my own project, I tried to be as descriptive on meta tags to give google enough information to assume this is a site that is worth visiting, these were strong tags and meta tags that describe clearly what the business is and what our ethos is.

## Technologies 

I had installed all of these technologies, imported where needed and initiated freeze > requirements.txt

Python3 :

HTML
CSS
JS
Bootstrap
FontAwesome
 Etc. do it later jimbyyyy


## Devices and browsers
-	Samsung
-	Iphone
-	Chrome
-	Edge

All of these platforms rendered as expected.


Code Institute provided the template that was used to create the project

[Code Institute Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Click the 'Use This Template' button
- Give your new repository a name
- Click 'Create Repository from Template'. This creates your new repository
- Click the green 'Gitpod' button. This will open a new gitpod workspace
- If using gitpod, ensure the workspace is pinned and you only open this once the workspace
- To commit to any work you do, simply follow these steps:
        - `git add .` 
        - `git commit -m "Add a short messaged explaining your commit"`
        - `git push`

#### Requirements

- Python 3
- Pip
- Git
- AWS S3

#### Creating a Clone

- On the repository, click Code
- In the Clone >> HTTPS section, copy the clone URL for the repository
- In your local IDE open Git Bash
- You will have to change the working directory based on where you want the clone directory to be made
- In the terminal type: `git clone, then paste in the URL from step 2
- In the env.py file, make sure you have these values:
        
        import os

        os.environ.setdefault("SECRET_KEY", "<app secret key of your choice>")
        os.environ.setdefault("DEVELOPMENT", "True")
        os.environ.setdefault('STRIPE_PUBLIC_KEY', '<key generated by Stripe>')
        os.environ.setdefault('STRIPE_SECRET_KEY', '<key generated by Stripe>')
        os.environ.setdefault('STRIPE_WH_SECRET', '<key generated by Stripe>')

- Stripe Keys are generated by Stripe with each user account having their unique key

- Install project requirements - `pip3 install requirements.txt`
- Migrate the database - `python3 manage.py migrate`
- Create a superuser - `python3 manage.py createsuperuser`
- To see the cloned project, in the terminal type: `python3 manage.py run server


#### Heroku Deployment

- Create a Heroku account, or, Sign in if you already have one
- Click New App Button
- In the Resources tab, search for Heroku Postgre and add it to your project
- dj_database_url and pyscopg2 need to be installed:

                pip3 install dj_database_url
                pip3 install psycopg2

- Log into Heroku CLI - `heroku login -1`
- Run migrations - ` Heroku run python3 manage.py migrate`
- Create a Superuser - `python3 manage.py createsuperuser`
- Install gunicorn - `pip3 install gunicorn`
- Create a file called requirements.txt - ` pip3 freeze > requirements.txt`
- Create a Procfile with this code inside it (notice the capital P!!)
        
        web: gunicorn (your_apps_name).wsgi:application

- Disable Heroku from collecting static files - ` heroku config:set DISABLE_COLLECTSTATIC=1 -- <app-name>`
- Add the host name to the project settings.py file

        ALLOWED_HOSTS = ['<app-name>.herokuapp.com', 'localhost']

- Connect Heroku to your Github, by selecting Github as the deployment method and searching for the GitHub repository, and pressing connect
- In Heroku, within settings, under config vars select Reveal config vars
- Add the following,

        AWS_ACCESS_KEY_ID =     <your variable here>
        AWS_SECRET_ACCESS_KEY = <your variable here>
        DATABASE_URL =  <added by Heroku when Postgres installed>
        DISABLE_COLLECTSTATIC = 1 
        EMAIL_HOST_PASS = <your variable here>
        EMAIL_HOST_USER = <your variable here>
        SECRET_KEY = <your variable here>
        STRIPE_PUBLIC_KEY = <your variable here>
        STRIPE_SECRET_KEY = <your variable here>
        STRIPE_WH_SECRET = <different from env.py>
        USE_AWS = True
- Go back to the Deploy tab and under Automatic Deploys choose Enable Automatic Deploys
- Back in your CLI add, commit, and push your changes and Heroku will automatically deploy your app
        
        git add.
        git commit -m "Initial commit"
        git push

- Your deployed site can be launched by clicking Open App from its page within Heroku.


AWS S3 Bucket setup

- Create an Amazon AWS account
- Search for S3 and create a new bucket
        - Allow public access
- Under Properties > Static website hosting
        - Enable
        - index.html as index.html
        - save
- Under Permissions > CORS use the following:

        [
         {
                "AllowedHeaders": [
                        "Authorization"
                ],
                "AllowedMethods": [
                        "GET"
                ],
                "AllowedOrigins": [
                        "*"
                ],
                "ExposeHeaders": []
         }
        ]

- Under Permissions > Bucket Policy:
        - Generate Bucket Policy and take note of Bucket ARN
        - Chose S3 Bucket Policy as Type of Policy
        - For Principal, enter *
        - Enter ARN noted above
        - Add Statement
        - Generate Policy
        - Copy Policy JSON Document
        - Paste policy into Edit Bucket policy on the previous tab
        - Save changes
- Under Access Control List (ACL):
        - For Everyone (public access), tick List
        - Accept that everyone in the world may access the Bucket
        - Save changes

AWS IAM (Identity and Access Management) setup:

- From the IAM dashboard within AWS, select User Groups:
        - Create a new group
        - Click through and Create Group
- Select Policies:
        - Create policy
        - Under the JSON tab, click Import managed policy
Choose AmazongS3FullAccess
        - Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
        - Click next step and go to Review policy
        - Give the policy a name and description of your choice
        - Create policy
- Go back to User Groups and choose the group created earlier
        - Under Permissions > Add permissions, choose Attach Policies and select the one just created
        - Add permissions
-       - Under Users:
        - Choose a username
        - Select Programmatic access as the Access type
        - Click Next
        - Add the user to the Group just created
        - Click Next and Create User
- Download the .csv containing the access key and secret access key.
        - THE .csv FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.

Connecting Heroku to AWS S3

- Install boto3 and django-storages

        pip3 install boto3
        pip3 install django-storages
        pip3 freeze > requirements.txt
        
- Add the values from the .csv you downloaded to your Heroku Config Vars under Settings:
- Delete the DISABLE_COLLECTSTATIC variable from your Cvars and deploy your Heroku app
- With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any required media files to it.
        - PLEASE MAKE SURE media AND static FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS

---

## Credits
