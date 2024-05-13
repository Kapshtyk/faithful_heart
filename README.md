# Fork of a Telegram bot and backend project for the animal shelter "Faithful heart".

On this project I was fully responsible for the bot implementation.

## Tech stack:

- Django 5
- aiogram 3.2.0
  
## Project structure:

- Bot - Telegram bot written on the aiogram framework.
- Backend - Backend written on the Django framework.
- Nginx - Directory for storing nginx config.

## Functional goals of the project:

Provide convenient user interaction with information about the shelter - frequently asked questions in different categories, the ability to ask your own question and easy access to the main pages of the shelter's main website.

## Achieved and planned:

## Requirements:
- Provide automatic answers (templates) to frequently asked questions. For example, working hours, visiting hours, how to bring an animal to the shelter, what food is needed, etc.
- You can template questions and answers in the bot,
- Have the possibility to receive a unique question from the user (not in the templates), which will be forwarded to the manager (to Telegram or e-mail),
- send the address of the shelter at the user's request,
- Send a link to the website (landing page) for donors to make a donation,
- Collect and store email addresses, full name and phone number of users, download report in Excel format.
- Send a link to the landing page with a list of animals in the shelter,
- Send a link to the landing page to join the adoption programme
### All of the above requirements were met:
- Sending messages has been implemented BOTH to telegram AND to email.
- Mass sending of news / promotions / important information about the shelter to all bot users has been implemented.
- A convenient system of question categories and their display in the bot has been implemented. In the admin panel you can easily create a new question for any of the categories.
- Validation of questions asked by the user has been implemented. If they contain obscene words, the question will not be saved in the database and administrators will not receive notifications about this question.

## Everything you need to run/work with the project:

- Instructions for running the project locally
  - When running locally, the backend and bot are launched as separate applications.
    * Backend:
      - Go to the `/backend/faithful_heart` folder, create an `.env` file based on the `.env.example` file.
      - In the `.env` file, specify `DEBUG_MODE=True` if you want to use SQLite as database, otherwise Postgres will be used.
      - Create migrations with the command `python manage.py makemigrations`.
      - Apply migrations with the command `python manage.py migrate`.
      - Questions can be loaded into the database as fixtures using the command `python manage.py loaddata data/questions.json`. These questions have been taken from the brief and grouped into categories.
      - The server can be started with the command python manage.py runserver.
    * Bot:
      - Go to the `/bot` folder.
      - Create an `.env` file based on `.env.example`.
      - Run the bot with the command `python main.py`.

- Instructions for Deploying the Project in Containers
  - To deploy in containers, you need to create `.env` files, 2 as described above, but also in the root directory you need to create an `.env` file based on `.env.example`.
- Recommendations for developers
  - The following things need to be done for the bot to work properly:
    - After starting the project, you need to upload the questions. You can do this in one of the following ways
    * Connect to a container:
      - Get all containers - `docker container ls`.
        - Copy the backend container id
      - Connect to the container
        - `docker exec -ti { container id} bash`.
    * Perform migrations:
      - `python manage.py migrate`.
    * Populate the database with questions:
      - `python manage.py loaddata data/questions.json`.
- The project supports sending notifications to multiple administrators.
- Below are instructions on how to populate users so that notifications are sent and work correctly.
  - To send notifications to Telegram correctly
    - Create a user in the admin panel (Admin Panel Users) or select an existing one.
    - When editing the user, enter `telegram_username` in the "Telegram username" field.
    - It is important that the Telegram user with this `telegram_username` is saved in the database.
  - To send notifications by email correctly
    - Create a user in the admin panel (Admin Panel Users) or select an existing one.
    - When editing a user, enter the email address to which notifications should be sent in the 'Email address' field.
