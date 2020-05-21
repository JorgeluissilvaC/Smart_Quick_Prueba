# Instrucciones de instalación:
1. Validamos que la máquina tenga instalado Python 2. Este proyecto se desarrolló en Python 2.7.18.
2. Instalar modulo virtualenv de Python:
	`pip install virtualenv`
3. Creamos un ambiente virtual para instalar las dependencias del proyecto. 
  `virtualenv <Nombre del entorno>`
4. Activamos el entorno virtual, ingresamos dentro de la carpeta   <Nombre del entorno> y ejecutamos:
  `Scripts\activate`    
5. Descargamos el repositorio de GitHub, con el siguiente comando (Validamos que la máquinatenga Git instalado):
  `git clone https://github.com/JorgeluissilvaC/intellinext_books.git`
6. Entramos a la carpeta del repositorio e instalamos las dependencias, con el siguiente comando:
  `pip install -r requirements.txt`
7. Realizamoslas migraciones necesarias a la base de datos. 
  `python manage.py makemigrations`               
  `python manage.py migrate`
8. En la carpeta base del proyecto, corremos el servidor de desarrollo:
	  `python manage.py runserver`
9. Procedemosa utilizar la aplicación. Estará disponible en la URL:
  http://localhost:8000/

----

1. 
  https://tutorial.djangogirls.org/es/django_start_project/
  https://www.django-rest-framework.org/api-guide/authentication/
  https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

  Crear el proyecto:
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  django-admin startproject Smart_Quick_Server .
  Creo la carpeta apps para agrupar las aplicaciones propias y dentro de ella el archivo __init__.py para que sea reconocida
  python manage.py makemigrations
  python manage.py migrate
  Instalamos Django djangorestframework
  pip install djangorestframework
  pip install markdown       # Markdown support for the browsable API.
  pip install django-filter  # Filtering support
  django-admin startapp api
  pip install django-rest-auth django-allauth

----------------------------------------------------------
--------------------------------------------------------------------
Leer todos los productos
> Request
$ curl -X GET -H "Authorization: Token 9992e37dcee4368da3f720b510d1bc9ed0f64fca" 
-d '' 
localhost:8000/api/getbooks

> Response
{"books": [
      {
        "id": 1, 
        "title": "CRUD Django", 
        "description": "Walkthrough for CRUD in DJANGO", 
        "author": 1, 
        "added_by": 2, 
        "created_date": "2020-02-29T21:07:27.968463Z"
       }
    ]
 }  

---------------------------------------------------
> Request
$ curl -X POST 
-H "Authorization: Token 1565c60a136420bc733b10c4a165e07698014acb" 
-d '{
"title":"CRUD Django",
 "description":"Walkthrough for CRUD in DJANGO",
 "author": 1}' 
localhost:8000/api/addbook 

> Response
   {"book": {
       "id": 1, 
       "title": "CRUD Django", 
       "description": "Walkthrough for CRUD in DJANGO", 
       "author": 1, 
       "added_by": 2, 
       "created_date": "2020-02-29T21:07:27.968463Z"
     }
   }
----------------------------------------------------
Actualizar un producto 
> Request
$ curl -X PUT 
-H "Authorization: Token <Toquen asociado al usuario>" 
-d '{
"title":"CRUD Django Updated V2", 
"description":"Walkthrough for CRUD in DJANGO", 
"author": 1
}' 

localhost:8000/api/updatebook/1

> Response

{"book": {
    "id": 1, 
    "title": "CRUD Django Updated V2", 
    "description": "Walkthrough for CRUD in DJANGO", 
    "author": 1, 
    "added_by": 2, 
    "created_date": "2020-02-29T21:07:27.968463Z"
  }
}
----------------------------------------------------
Eliminar un producto

> Request
$ curl -X DELETE 
-H "Authorization: Token 9992e37dcee4368da3f720b510d1bc9ed0f64fca" 
-d '' localhost:8000/api/deletebook/1