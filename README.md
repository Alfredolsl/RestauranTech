[![language](https://img.shields.io/badge/Python-03.11%20%20-blue)](https://learn.microsoft.com/ru-ru/dotnet/csharp/tour-of-csharp/overview)
![RestauranTech](https://i.imgur.com/WuPNVfx.png)

# RestauranTech

## Introduction
RestauranTech is a web application designed to optimize restaurant operations through advanced inventory management, cost control, and supplier price analysis. The app allows restaurants to manage the stock of ingredients, beverages, and other supplies in real-time, as well as monitor and control expenses related to purchases.
## Why was it made?
RestauranTech was made to help!
We are looking to aid:
* Restaurant owners and managers
* Restaurant administration staff
* Chefs and kitchen staff
* Suppliers and distributors


This project is our Portfolio projects to demonstrate what we've been taught regarding Holberton School's Foundations. 
## The Team
This project came into existence with well-thought-out work from passionate developers!
* **[José Daniel Puc Poot](https://github.com/jose121k0074)**
* **[Efrén Jimenez Mukul](https://www.linkedin.com/in/efren-jimenez/)**
* **[Alfredo Lehman](https://www.linkedin.com/in/alfredolsl/)**

## Deployed Project
**[Restaurantech](https://restaurantech.onrender.com/)**
![RestauranTech](https://github.com/Alfredolsl/RestauranTech/blob/main/app/static/images/restaurantech_feature_inventory.png)
## Learn more about the project
**[Blog Post](https://www.linkedin.com/pulse/restaurantech-my-first-web-application-alfredo-lopez-fb7oc/?trackingId=5icztELj1UXYLg2WC6ZfkA%3D%3D)**


# Tutorial
## Installation
Install the required python packages inside `requirements.txt` with the following command:
```
pip install -r requirements.txt
```

For the web app to work correctly, make sure to have a MySQL database with the tables inside **[app/tables](https://github.com/Alfredolsl/RestauranTech/tree/main/app/tables)**

For the web app to work as expected, add a `.env` file at the root of the repository with the following variables:
```
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DATABASE=
```
It is necessary to have a working MySQL database.


# Usage
When the installation steps are successful, run in the root folder:
```
python run.py
```
It returns the following message in the console:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on (localhost)
 * Running on (local network IP)
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: (pin)
```
Now one of the two links provided by the app should send you to your browser of choice.

For using the core functions:
* Log In with your account or create a new one.
* After logging in, you're redirected to the admin panel.
* Add new items on the 'Add New Item' button.
* In the form, select the available branch in the Branch field, then click 'Search Sections' button.
* After that, choose the section of your choice, then click 'Search Products in Section'.
* You should get a list of items (currently in spanish), choose the one you want to add, then click 'Fill Information'
* Make sure that everything is filled out to your liking
* Then, add the Shelf life in the Shelf life form.
* Click 'Add Item to Inventory'
* Click 'Back', you will see the new item added to the Inventory table.

# Contributing
We've come a long way to make this project what it is. However, the development doesn't stop here, and your contributions are crucial for our improvement.

Please feel free to contribute by forking this repo or message **[Alfredo via Linkedin](https://www.linkedin.com/in/alfredolsl/)**.

We appreciate your support and feedback to making our project better!

# Known bugs
The 'Fill Information' button doesn't fill out the Shelf Life form, so expect to manually input a number in that field.

# About this project
My team members are really passionate for developing applications, and even more passionate if said application can improve or aid the life or work of the users. When we were reviewing what topic or problem we could develop on and possibly solve, we first chose to turn music lyrics into images in real-time using Artificial Intelligence, we took a step back and turned our perspective into our surroundings, then, to our community.

Whenever we started a meeting, we always started to talk about how was our day, what we ate, etc. Our frequent topic was about food, and one of our members, with experience on working with restaurants, pointed out that restaurants may have trouble managing their inventory. With this problem at hand, we delved into the problem, and we all agreed to change the scope of the project and focus on what we were comfortable on developing and, of course, passionate about.

Oddly enough, I didn't have any idea about how our project topic was going to be about restaurants, but having listened to my other team members talk with sheer curiosity about what roles they want in the development and the results were expecting, I knew I couldn't deny their happiness from this newfound topic, so I decided to fill on the parts to work on, fortunately, with the development of the app, it was entertaining progressing on the functionality of the app. A funny thing about developing this app was when the sessions felt like meditating for me! My mind went quiet whenever there was a problem to solve and how to implement a solution on it.

# About the Devs 
## What Alfredo learned from this
What I've learned
I'm really proud the amount of work I delivered in this project, and these are the numerous key skills I gained experience in:

* Backend development
* Database management - Learnt how to structure relational databases.
* AJAX and front-back interactivity - With discovering the benefits of using JavaScript, I won't fear using it for future projects.
* Data handling - This is an important skill for building interactive applications, such as this project.
* Problem-solving

## What's next for Alfredo?
Developing this type of work is almost therapeutic for me; I calm down, my mind goes quiet, and I can achieve progress (or even exponential progress if I wear noise-cancelling headphones!). With insight gained from this project and the fundamentals learned of building projects, my next step in life is seeing what type of technical and creative work I could go into in the future, and what to setup for my portfolio. From what I've interacted with, augmented and virtual reality are new and exciting topics for me, and Unity sounds fun.

Thanks for reading! I'm Alfredo, a passionate developer and creative that would love to do multiple types of work in life! From technical work, such as programming software, to creative work like 3D art!

# Licensing
MIT License

Copyright (c) [2024-present] [Alfredo Lehman, José Puc Poot, Efrén Jiménez]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
