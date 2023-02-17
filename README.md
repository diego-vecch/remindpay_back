# RemindPay Backend
Bienvenidos al reposiotorio backend para la app de recordatorios de suscripciones de pago, encontrarás la guía de como implementar en tu entorno local y hacer pruebas. 
## Clonar repositorio
git clone https://github.com/diego-vecch/remindpay_back.git

# Configuración del proyecto en windows 

## Usando venv (entorno virtual) - opción 1
python -m venv env
env\Scripts\activate

## Usando virtual env(entorno virtual) - opción 2

### Instalar el entorno  virtualenv
pip install virtualenv

### Crear el entorno virtual
python -m virtualenv venv

### Activar virtualenv
.\venv\Scripts\activate

### Install Corsheaders
pip install django-cors-headers
pip install python-dotenv
pip install python-decouple
pip install django
# Configuración del proyecto en Mac
## Create a virtual environment to isolate our package dependencies locally
python3 -m venv env

## Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

### Install Corsheaders
pip3 install django-cors-headers
pip3 install python-dotenv
pip3 install python-decouple
