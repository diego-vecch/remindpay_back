# RemindPay Backend
Welcome to the repository backend for paid subscription reminders app, you will find the guide on how to deploy in your local environment and do testing.
---
## 1) Clone repository
$ git clone https://github.com/diego-vecch/remindpay_back.git

# Project Settings on Windows 

## 2) Create a virtual environment and activate it - for this step there are two options::

### Option 1 - Use venv
$ python -m venv env
$ env\Scripts\activate

### Option 2 - Use virtual env 

#### Install virtual env
#### $ pip install virtualenv

#### Create a virtual environment
#### $ python -m virtualenv venv

#### Active virtualenv
$ .\venv\Scripts\activate

## 3) Install Django and Django REST framework into the virtual environment
#### $ pip install django

## 4) Install dependencies

#### $ pip install django-cors-headers
#### $ pip install python-dotenv
#### $ pip install python-decouple

# Project Settings on Mac

## 2) Create a virtual environment to isolate our package dependencies locally
$ python3 -m venv env
$ source env/bin/activate

## 3) Install Django and Django REST framework into the virtual environment
$ pip install django
$ pip install djangorestframework

## 4) Install dependencias
#### $ pip install django-cors-headers
#### $ pip install python-dotenv
#### $ pip install python-decouple
---
