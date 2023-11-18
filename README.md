# omardo
Main page for https://omar.do


## Dev

#### 1. clona el repositorio

#### 2. crea un ambiente virtual 

`python -m venv .venv`

#### 3. actívalo 

Corre el script que está en:
`.venv\Scripts\activate`

#### 4. instala las dependencias de python.

``` bat
pip install -r requirements.txt
python -m pip install django-tailwind[reload]
python omardo\manage.py tailwind install
```

#### 5. Inicia el observador de tailwind
``` bat
python omardo\manage.py tailwind start
```
Este servicio obsrevará tus *django-templates* para crear el style.css correspondiente. También actualizará cualquier página abierta para aplicar los cambios automáticamente.


#### 5. Inicia el servidor de desarrollo
``` bat
python omardo\manage.py runserver
```
