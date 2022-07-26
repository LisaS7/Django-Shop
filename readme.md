A Django ecommerce site based on [Tutorial](https://www.youtube.com/watch?v=UqSJCVePEWU&t=1500s)

I've played around with Django in the past but I felt like a structured tutorial would be useful as a refresher and to fill in some areas of knowledge that I hadn't covered yet. I decided to stick with the Star Wars theme used in a previous small project. Following this tutorial has helped me to understand how to better organise a Django app.

### What I learned:

General
* Using a context processor to access data across all templates.

Testing & Formatting
* Using the coverage library to help identify where tests are needed.
* Setting up test data.
* Testing views using the Client object.
* Fixing import statements using isort.

Basket
* Working with sessions: saving and retrieving data.
* Using Ajax to dynamically update the number of items in the basket and the totals on the basket summary page.

Users & Admin
* Creating a custom user model.
* Configuring the admin view display fields and filters.
* Sending an email to validate new users.
* Generating a password reset token.
