A Django ecommerce site for a Star Wars fictional weapons trader.

[Heroku app](https://rodian-arms-shop.herokuapp.com)
(Some functionality missing on mobile at the moment)

I had minimal experience with Django so a structured tutorial felt like it would be useful as a refresher and to fill in some areas of knowledge that I hadn't covered yet. I decided to stick with the Star Wars theme used in a previous small project. Following this tutorial has helped me to understand how to better organise a Django app and the deployment process.


### What I learned:

Django
* Using a context processor to access data across all templates.

Testing & Formatting
* Using the coverage library to help identify where tests are needed.
* Setting up test data and using the Client object.
* Fixing import statements using isort.

Basket
* Working with sessions: saving and retrieving data.
* Using Ajax to dynamically update the number of items in the basket and the totals on the basket summary page.

Users & Admin
* Overriding Django's built in user functionality to create a custom user model, forms, and views.
* Sending an email with a unique token to validate new users or reset passwords.
* Configuring the admin view display fields and filters.

Deployment
* Moving secret keys and other private data to environment variables using the Ubuntu .profile file.
* Set up AWS account with S3 storage for static files and new IAM user.
* Setting environment variables in Heroku.
* Using the Heroku Procfile to handle database migration and load data.

### Resources
* [Ecommerce site tutorial](https://www.youtube.com/watch?v=UqSJCVePEWU&t=1500s)
* [Setup and configure postgresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
* [AWS S3 storage setup](https://youtu.be/kt3ZtW9MXhw)
* [Deploy to Heroku](https://youtu.be/6DI_7Zja8Zc)