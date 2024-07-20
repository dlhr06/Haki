# Haki
Repositorio para el Hackathon - Crea tu PL de Código Facilito 🐊


Comandos:

* Para leer documento PDF.
~~~
haki read_pdf filename.pdf
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

Si desea crear, actualizar o borrar un dato puede hacerlo directamente en el archivo yaml. A continuación, se actualiza el nombre y se agrega información de la educación:
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


**Proximamente**
* Generar resumen profesional para proporcionar una visión general de tus habilidades y logros. El resumen se genera con base al archivo yaml generado previamente.
  ~~~
  haki get_professional_resume filename_haki.yaml
  ~~~
  
* Generar carta de motivaciones. El resumen se genera con base al archivo yaml generado previamente y la información del puesto de trabajo al que se desea aplicar (ulr).
  ~~~
  haki get_professional_resume filename_haki.yaml www.url.com
  ~~~

* Ingresar página donde se encuentra la información de la postulación. Mediante LLM (publico o privado) realizar sugerencias a la información del CV (crea un nuevo yaml con las sugerencias) y proporcionar porcentaje de ajuste con el puesto
~~~
haki check_position filename_haki.yaml www.url.com

output:
Tu CV se ajusta 100% a la posición!.
~~~

* Realizar postulación en una página

~~~
haki apply_for filename_haki.yaml www.url.com
~~~

En caso de que la página requiera postularse mediante una cuenta, esta deberá crearse previamente y agregar los datos de inicio en un nuevo archivo yaml. Por ejemplo, en el siguiente archivo yaml, llamado ``login_credentials.yaml``, se muestra el correo y la contraseña utilizados para iniciar sesión en la página de postulación:
~~~
credentials:
  mail: roronoa_zoro@mugiwara-no-ichimi.com
  password: miCapitanSeraElReyDeLosPiratas!
~~~

Cuando se realiza postulación con una cuenta, se agrega el yaml de las credenciales:
~~~
haki apply_for filename_haki.yaml www.url.com login_credentials.yaml
~~~

**Este lenguaje no almacena ni comparte tu información**
