
---
Demo Staff User Login Credentials for Deployed API:

    1.  username - demo_staff_1  , password - staffishere 
    2.  username - demo_staff_2  , password - staffishere 
    3.  username - demo_staff_3  , password - staffishere 

Demo Non Staff  User Login Credentials:

    1.  username - demo_user_1  , password - demoishere 

---
# Django REST Framework Project Setup Guide

This guide will help you set up a Django REST Framework project with the required dependencies and create a superuser.

## Requirements

* Python 3.6 or later
* pip

## Step 1: Clone the project

Clone the project from the repository using the following command:

```
git clone <repository url>
```


## Step 2: Create a Virtual Environment

Create a virtual environment using the following command:

```
python3 -m venv venv
```
Activate the virtual environment using the following command:

```
source venv/bin/activate
```

## Step 3: Install Dependencies

Change to the project directory and install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Step 4: Make Migrations and Migrate

Run the following commands to create database migrations and migrate the database:

```

python manage.py makemigrations
python manage.py migrate

```

## Step 5: Create a Superuser

Run the following command to create a superuser:

```
python manage.py createsuperuser
```

You will be prompted to enter a username, email, and password for the superuser.

## Step 6: Run the Server

To start the server, run the following command:

```
python manage.py runserver
```

You should now be able to access the project at http://localhost:8000/. 

## Step 7: Testing the API endpoints

You can test the API endpoints using tools like Postman or cURL. 