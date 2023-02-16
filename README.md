# RemindPay Backend
Bienvenidos al reposiotorio backend para la app de recordatorios de suscripciones de pago, encontrarás la guía de como implementar en tu entorno local y hacer pruebas. 
## Clonar repositorio
git clone https://github.com/diego-vecch/remindpay_back.git

## Configuración del proyecto en windows
python -m venv env
source env\Scripts\activate


### Instalar el entorno  virtualenv
pip install virtualenv

### Crear el entorno virtual
python -m virtualenv venv

### Activar virtualenv
.\venv\Scripts\activate

## Configuración del proyecto en Mac
## Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  

## Install Django and Django REST framework into the virtual environment
pip install django
pip install djangorestframework

### Install Corsheaders
pip install django-cors-headers