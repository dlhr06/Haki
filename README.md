# Haki 

### Tu Curriculum Vitae de manera eficaz en la web 📑🌐

_Repositorio final para el primer Hackathon virtual "Crea tu propio lenguaje de programación" de Código Facilito_ 💻🐊

_Desarrollo por: Equipo no. 20_ 

## Descripción 

Haki es un innovador lenguaje de programación diseñado específicamente para leer y administrar la información contenida en tu curriculum vitae, con el objetivo de simplificar el proceso de postulación al automatizar la extracción y el llenado de formularios en diversas plataformas de empleo. 📨🔎

## Indice 

[Descripción](#descripción) | [Instalación](#instalación) | [Comandos](#comandos) | [Video Demostración](#video-demostración) | [Próximamente](#próximamente) | [Herramientas](#herramientas) | [Autores](#autores) | [Política de Privacidad](#política-de-privacidad) | [Licencia](#licencia)



## Instalación 

[Instala nuestro ejecutable y comienza a gestionar la información de tu CV de manera eficaz_](https://drive.google.com/file/d/1kTEz6pPqFvE9S9lor_GgXzbIcnmdQJFT/view?usp=drive_link)


## Comandos 

### Lee CV en formato PDF. 
~~~
haki read_pdf CV.pdf
~~~

Al leer el documento PDF, se crea un archivo *yaml* con el nombre del PDF más "_haki". Ejemplo: cv_zoro_roronoa.pdf -> cv_zoro_roronoa_haki.yaml. El archivo yaml contiene la información del pdf, como se muestra a continuación:
~~~
personal_information:
  name: Zoro
  lastname: Roronoa
  Age: 21
  Address: Calle Espada Samurai No. 3
  City: Onigashima
  State: Wano
  Country: Mexico
  phonenumber: "1234567890"
~~~

Si desea crear, actualizar o borrar un dato puede hacerlo directamente en el archivo yaml. 
~~~
personal_information:
  name: Cody
  lastname: Roronoa
  Age: 21
  Address: Calle Espada Samurai No. 3
  City: Onigashima
  State: Wano
  Country: Mexico
  phonenumber: "1234567890"

education:
  title_obtained: Espadachín Maestro
  description: Entrenamiento intensivo en técnicas de espada y combate cuerpo a cuerpo.
  institution: Shimotsuki Dojo Sword School
  location: Shimotsuki Island
  start_date:
    day: 1
    month: 1
    year: 2000
  end_date:
    day: 31
    month: 12
    year: 2005
~~~


### Genera un resumen profesional 
* El resumen se genera con base al archivo yaml generado previamente.
  ~~~
  haki get_professional_summary CV_haki.yaml
  ~~~
  


## Video demostración 

Consulta el [video demostración de Haki](https://drive.google.com/file/d/1HlGD03fOTVwO5_i9uf6cb_krdqvpB-fy/view?usp=drive_link) para descubrir como ejecutar todas las funciones para administrar la información de tu CV

## Próximamente 

## Genera una carta de motivaciones de manera automática

~~~
haki get_motivation_letter CV_haki.yaml
~~~

### Compara tu perfil con el puesto de trabajo solicitado
* Mediante un modelo LLM (chat-gp3) se pueden realizar sugerencias respecto al CV, y otorgarnos un archivo yaml con sugerencias y el porcentaje de ajuste de nuestro perfil con el puesto de trabajo.

~~~
haki check_position filename_haki.yaml www.url.com

output:
Tu CV se ajusta 100% a la posición!.
~~~

### Postula de manera automática desde la web

* Mediante el modelo LLM selecciona, llena el formulario de postulación a un empleo de manera automática desde una plataforma determinada.

~~~
haki apply_for_job CV_haki.yaml CV_haki.pdf www.url.com
~~~

* En caso de que la página requiera postularse mediante una cuenta, esta deberá crearse previamente y agregar los datos de inicio en un nuevo archivo yaml.

~~~
archivo_login = login_credentials.yaml

credentials(archivo_login):
  mail: roronoa_zoro@mugiwara-no-ichimi.com
  password: miCapitanSeraElReyDeLosPiratas!
~~~

* Cuando se realiza postulación con una cuenta, se agrega el yaml de las credenciales:
~~~
haki apply_for filename_haki.yaml www.url.com login_credentials.yaml
~~~


## Herramientas

* [Python](https://www.python.org/) - El lenguaje de programación base
* [g4f](https://pypi.org/project/g4f/) - Herramienta para manejar modelos de lenguaje como GPT-4.


## Autores 

* **Juan Arias Castillo** - *Desarrollador* - [jariasca9](https://github.com/jariasca9)

* **Diana Hernández Romero** - *Desarrollador* - [dlhr06](https://github.com/dlhr06)


## Politica de Privacidad 

1. Haki no recopila, almacena ni gestiona ninguna información personal identificable. Toda la información y los datos que maneja la aplicación se procesan localmente en su dispositivo.
2. Haki no recopila ni almacena información sobre el uso de la aplicación. No tenemos acceso a los archivos PDF que lee ni a ninguna otra actividad que realice dentro de la aplicación.
3. Toda la información y los datos procesados por Haki se almacenan localmente en su dispositivo. No se transmite ninguna información a servidores externos ni a terceros.
4. Aunque Haki no maneja datos personales, recomendamos a los usuarios que protejan sus dispositivos con medidas de seguridad adecuadas, como contraseñas fuertes y software antivirus, para asegurar la integridad de sus datos locales.

## Licencia 

Este proyecto está bajo la Licencia (Haki Corps S.A) - mira el archivo [LICENSE.md](LICENSE.md) para detalles



