# Instrucciones de instalación:
1. Validamos que la máquina tenga instalado Python 3.8.2.
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

# EndPoints

## Registro de usuario

Para registar un usuario se debe envíar por POST a la dirreción
> Request $ curl -X POST -d '{
    "username": "dgarciam",
    "email": "dgarcia@uninorte.edu.co",
    "password1": "jorge123.",
    "password2": "jorge123."
} ' http://localhost:8000/rest-auth/registration/

> Response { key: <Token generado para autenticación> }
  
Este token se usará para iniciar sesión en la API. 

------------------------------------------------------------------------
## Iniciar sesión 

> Request $ curl -X POST -d '{
    "username": "dgarciam",
    "password": "jorge123.",
} ' http://localhost:8000/rest-auth/login/

La respuesta nos entrega el Token asignado al usuario. 
Con este podemos interactiar con la API, el token debe enviarse en la cabecera

> Response {
    "key": "<Token generado>"
}
	
------------------------------------------------------------------------
## Cerrar sesión

Para Cerrar sesión se debe enviar por medio de POST el Token , por medio del parámetro 'Authorization=Token <Token generado>'
EnfPoint : http://localhost:8000/rest-auth/logout/ 

> Request $ curl -X POST -H "Authorization: Token <Token generado para el usuario>" 
-d '{   "name" : "Saviloe",
    	"description" : "muy bueno",
    	"attribute1" : "100Hg",
    	"attribute2" : "ds",
     	"attribute3" : "ds",
    	"attribute4" : "sd"
}' localhost:8000/api/v1/addproduct/ 

> Response {
    "detail": "Sesión cerrada con éxito."
}
------------------------------------------------------------------------
## Leer todos los productos
> Request
$ curl -X GET -H "Authorization: Token <Token generado para el usuario>" 
-d '' http://localhost:8000/api/v1/getproducts/

> Response
{
    "products": [
        {
            "id": 1,
            "name": "Vive100",
            "description": "muy bueno",
            "attribute1": "100Hg",
            "attribute2": "ds",
            "attribute3": "ds",
            "attribute4": "sd"
        },
        {
            "id": 2,
            "name": "Saviloe",
            "description": "muy bueno",
            "attribute1": "100Hg",
            "attribute2": "ds",
            "attribute3": "ds",
            "attribute4": "sd"
        },
        {
            "id": 3,
            "name": "Saviloeddd",
            "description": "muy bueno",
            "attribute1": "100Hg",
            "attribute2": "ds",
            "attribute3": "ds",
            "attribute4": "sd"
        }
    ]
}
------------------------------------------------------------------------
## Agregar un nuevo producto

> Request
$ curl -X POST 
-H "Authorization: Token <Token generado para el usuario>" 
-d '{
	"name" : "Saviloe",
    	"description" : "muy bueno",
    	"attribute1" : "100Hg",
    	"attribute2" : "ds",
     	"attribute3" : "ds",
    	"attribute4" : "sd"
}' 
localhost:8000/api/v1/addproduct/ 

> Response
   {"book": {
       "id": 1, 
	"name" : "Saviloe",
    	"description" : "muy bueno",
    	"attribute1" : "100Hg",
    	"attribute2" : "ds",
     	"attribute3" : "ds",
    	"attribute4" : "sd"
     }
   }

## Actualizar un producto 

> Request
$ curl -X PUT 
-H "Authorization: Token <Toquen asociado al usuario>" 
-d '{
       "id": 1, 
	"name" : "Saviloe",
    	"description" : "muy bueno",
    	"attribute1" : "100Hg",
    	"attribute2" : "ds",
     	"attribute3" : "ds",
    	"attribute4" : "sd"
}' 

http://localhost:8000/api/v1/updateproduct/<id>

> Response

{"book": {
       "id": 1, 
	"name" : "Saviloe",
    	"description" : "muy bueno",
    	"attribute1" : "100Hg",
    	"attribute2" : "ds",
     	"attribute3" : "ds",
    	"attribute4" : "sd"
  }
}

## Eliminar un producto

> Request
$ curl -X DELETE 
-H "Authorization: Token <Toquen asociado al usuario>" 
-d '' http://localhost:8000/api/v1/deleteproduct/<id>

## Leer todos  los clientes

> Request
$ curl -X GET -H "Authorization: Token <Token generado para el usuario>" 
-d '' 
http://localhost:8000/api/v1/getclients/

> Response
{
    "clients": [
        {
            	"id": 1,
   		"document" : "1143144920",
    		"first_name" : "Jorge2",
    		"last_name" : "Silva2",
    		"email" : "j@u2.com"
        },
    ]
}
## Agregar un nuevo cliente

> Request
$ curl -X POST 
-H "Authorization: Token <Token generado para el usuario>" 
-d '{
   "document" : "1143144920",
    "first_name" : "Jorge2",
    "last_name" : "Silva2",
    "email" : "j@u2.com"
}' 
localhost:8000/api/v1/addclient/ 

> Response
   {"client": {
       "id": 1, 
   "document" : "1143144920",
    "first_name" : "Jorge2",
    "last_name" : "Silva2",
    "email" : "j@u2.com"
     }
   }

## Actualizar un cliente

> Request
$ curl -X PUT 
-H "Authorization: Token <Toquen asociado al usuario>" 
-d '{
     "id": 1, 
   "document" : "1143144920",
    "first_name" : "Jorge2",
    "last_name" : "Silva2",
    "email" : "j@u2.com"
}' http://localhost:8000/api/v1/updateclient/<id>

> Response {"client": {
    "id": 1, 
   "document" : "1143144920",
    "first_name" : "Jorge2",
    "last_name" : "Silva2",
    "email" : "j@u2.com"
  }
}

## Eliminar un cliente

> Request
$ curl -X DELETE 
-H "Authorization: Token <Toquen asociado al usuario>" 
-d '' http://localhost:8000/api/v1/deletecliente/<id>


## Leer todos  los facturas
> Request
$ curl -X GET -H "Authorization: Token <Token generado para el usuario>" 
-d '' http://localhost:8000/api/v1/getbills/

> Response {
    "bills": [
        {
	"name" : "Smart",
    	"client_id" : "1",
   	 "company_name" : "La mejor",
    	"nit" : "31321654654",
     	"code" : "13213213213",
    	"product" : 1
        },
    ]
}

## Agregar una nueva factura

> Request
$ curl -X POST 
-H "Authorization: Token <Token generado para el usuario>" 
-d '{
	"name" : "Smart",
    	"client_id" : 4,
   	 "company_name" : "La mejor",
    	"nit" : "31321654654",
     	"code" : "13213213213",
    	"product" : 2
}'  localhost:8000/api/v1/addbill/ 

> Response
{
    "bill": {
        "id": 25,
        "name": "Smart",
        "client_id": 4,
        "company_name": "La mejor",
        "nit": "31321654654",
        "code": "13213213213",
        "product": [
            2
        ]
    }
}

## Actualizar una factura
> Request
$ curl -X PUT 
-H "Authorization: Token <Toquen asociado al usuario>" 
-d '{
        "id": 25,
        "name": "Smart",
        "client_id": 4,
        "company_name": "La mejor",
        "nit": "31321654654",
        "code": "13213213213",
        "product": [
            2
        ]
}' http://localhost:8000/api/v1/updatebill/<id>

> Response

{"client": {
        "id": 25,
        "name": "Smart",
        "client_id": 4,
        "company_name": "La mejor",
        "nit": "31321654654",
        "code": "13213213213",
        "product": [
            2
        ]
  }
}

## Eliminar una factura

> Request
$ curl -X DELETE 
-H "Authorization: Token <Toquen asociado al usuario>" 
-d '' http://localhost:8000/api/v1/deletebill/<id>


## Endpoint descargar CSV .

> Request
$ curl -X POST 
-H "Authorization: Token <Toquen asociado al usuario>" 
-d '' http://localhost:8000/api/v1/getdatacsv/
