# Django Todo Application

A feature-rich Todo application built with Django that includes user authentication, task management, and theme switching.

## Features

- User Authentication (Register, Login, Logout)
- Create, Read, Update, and Delete tasks
- Task filtering (All, Pending, Completed)
- Dark/Light theme switching
- Responsive design
- Due date support for tasks

## Installation

1. Clone the repository in bash

git clone https://github.com/yourusername/Django-Todo-Project.git
cd Django-Todo-Project

2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Run migrations

python manage.py migrate

5. Start the development server

python manage.py runserver

## Usage

1. Register a new account or login with existing credentials
2. Add new tasks with optional description and due date
3. Mark tasks as complete
4. Edit or delete existing tasks
5. Filter tasks by status
6. Toggle between light and dark themes

## Technologies Used

- Django
- HTML/CSS
- JavaScript
- SQLite

## License

This project is licensed under the MIT License - see the LICENSE file for details.