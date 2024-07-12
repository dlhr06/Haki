# Haki
Repositorio para el Hackathon - Crea tu PL de Código Facilito 🐊


Comandos:

* Para leer documento PDF.
~~~
info = read_pdf('filename.pdf') # Leer documento pdf
~~~

* Para imprimir en consola los datos del PDF.
~~~
print(info) # Se imprime en consola los datos que contiene el pdf
Output:
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

* Para actualizar datos del PDF.
~~~
info['name'] = 'Cody' # Se actualiza la información
~~~

* Para agregar información que no contiene el PDF.
~~~
education_info = {
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

dicc['education'] = education_info # Se agrega nueva información no contenida en el PDF
~~~
