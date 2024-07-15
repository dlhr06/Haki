# Haki
Repositorio para el Hackathon - Crea tu PL de Código Facilito 🐊


Comandos:

* Para leer documento PDF.
~~~
haki read_pdf "filename.pdf"
~~~

Al leer el documento PDF, se crea un archivo json (**YAML en lugar de json**) con el nombre del PDF más "_haki". Ejemplo: cv_zoro_roronoa.pdf -> cv_zoro_roronoa_haki.json. El archivo json contiene la información del pdf, como se muestra a continuación:
~~~
{
    "name": "Zoro",
    "lastname": "Roronoa",
     "Age": 21,
    "Address": "Calle Espada Samurai No. 3",
    "City": "Onigashima",
    "State": "Wano",
    "Country": "Mexico",
    "phonenumber": "1234567890"
}
~~~

Si desea crear, actualizar o borrar un dato puede hacerlo directamente en el archivo json. A continuación, se actualiza el nombre y se agrega información de la educación:
~~~
{
    "name": "Cody",
    "lastname": "Roronoa",
     "Age": 21,
    "Address": "Calle Espada Samurai No. 3",
    "City": "Onigashima",
    "State": "Wano",
    "Country": "Mexico",
    "phonenumber": "1234567890",
    education: {
        "title_obtained": "Espadachín Maestro",
        "description": "Entrenamiento intensivo en técnicas de espada y combate cuerpo a cuerpo.",
        "institution": "Shimotsuki Dojo Sword School",
        "location": "Shimotsuki Island",
        "start_date": {
            "day": 1,
            "month": 1,
            "year": 2000
        },
        "end_date": {
            "day": 31,
            "month": 12,
            "year": 2005
        }
    }
}
~~~


**Proximamente**
* Realizar postulación en una página

~~~
haki apply_for "filename_haki.json" "www.url.com"
~~~

En caso de que la página requiera postularse mediante una cuenta, esta deberá crearse previamente y agregar los datos de inicio en un nuevo archivo json. Por ejemplo, en el siguiente archivo json, llamado ``login_credentials.json``, se muestra el correo y la contraseña utilizados para iniciar sesión en la página de postulación:
~~~
{
"mail": "roronoa_zoro@mugiwara-no-ichimi.com
"password": "miCapitanSeraElReyDeLosPiratas!"
}
~~~

Cuando se realiza postulación con una cuenta, se agrega el json de las credenciales:
~~~
haki apply_for "filename_haki.json" "www.url.com" "login_credentials.json"
~~~

**Este lenguaje no almacena ni comparte tu información**
