# Curso Básico de Flask
## Introducción

En este curso aprenderemos a utilizar Flask, el cual es un marco de desarrollo web basado en Python.

Flask es un framework minimalista con el cual es muy fácil hacer aplicaciones web. Incluso siendo minimalista, Flask puede escalar junto con tus proyectos tanto como lo necesites, claro que necesitaras un poco más de conocimiento pero la posibilidad existe. Afortunadamente es un framework que cuenta con bastantes funcionalidades para cumplir las tareas mas comunes y en que caso de que necesites algo más puedes hacer uso de las librerías que otros usuarios han creado para hacer que tu aplicación pueda hacer justo lo que necesitas, eso vuelve todo el proceso más sencillo, así que no hay nada de que preocuparse.

### Hola Mundo con Flask (Ejemplo; App)
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"
	
if __name__ == "__main__":
	app.run()
```

**Sencillo, ¿no es así? Pues vamos a comenzar entonces, ¡suerte!**

## Resumen general

Bienvenido al resumen general de curso, aquí puedes darte una idea del contenido de cada vídeo y si estás buscando algo en específico pues a por ello. Aún así te recomendamos que mires cada vídeo para que te puedas beneficiar de toda la información.

#### Aplicación base, servidor y servir aplicación localmente.
##### Tutoriales: 1, y 2.
Crear una aplicación de Flask es algo muy sencillo, y comenzar a utilizarla también, para hacerlo solamente necesitamos servirla mediante un servidor local que nosotros establecemos. En esto último nosotros podemos elegir en que puerto y host se ejecutará nuestra aplicación, entre otras cosas.

#### Rutas, Url's, estáticas y dinamicas
##### Tutorial: 3
Una de las actividades mas comúnes consiste en crear rutas mediante las cuales realizamos diferentes acciones. Ya sean rutas dinamicas o estáticas nosotros aprendimos a crearlas, y analizamos diferentes características de estas, e incluso mencionamos algunos consejos para crearlas de manera correcta.

#### Archivos estáticos
##### Tutorial: 4
Un tema que no es complejo del todo y del que además no hablamos mucho son los archivos estáticos (CSS, JS, Favicon) pues no corresponden como tal de manera literal al curso, sin embargo, aún así explicamos qué son y como utilizarlos en conjunto con nuestra aplicación.

#### Vistas (Plantillas HTML)
##### Tutorial: 5
Podemos crear aplicaciones web mediante Flask utilizando diferentes bases referentes a desarrollo web, sin embargo, muchas de las aplicaciones creadas hoy en día son para que las utilicé cualquier usuario común directamente y para hacer que esto se cumpla nosotros les fácilitamos el uso del sitio web mostrando la información necesaria mediante plantillas HTML en las cuales nosotros podemos presentar diferentes elementos visuales al usuario para que pueda hacer uso de cada una de las funciones que nuestro sitio web ofrezca. Lograr todo esto es bastante sencillo, preparamos un directorio y allí guardamos nuestras plantillas, después a cada ruta le asignamos una plantilla que distribuir, y listo!

#### Jinja (Motor de vistas)
##### Tutorial: 6
La mayoría de plantillas HTML muestran datos estáticos, es decir, no cambian, sin embargo nosotros estamos creando un sitio web dinamico donde mucha de la información cambia en base a los datos que se esten manejando en el área del servidor (backend) y que de hecho es la parte que estamos administrando mediante Flask, es por ello que contamos con un motor de vistas por defecto y ese es Jinja el cual se encarga de crear un vinculo entre nuestras plantillas HTML y nuestra aplicación para darle vida a esa información, y no solo eso sino que con Jinja también podemos "programar" en dichas plantillas. Un motor de vistas bastante potente y del cuál hay muchas cosas de que hablar, aquí te damos los básicos para que aprendas el uso que le puedas dar (más adelante hay mas tutoriales referentes a Jinja).

#### Bases de Datos (Conexión, esquemas y operaciones)
##### Tutorial: 7
En este tipo de aplicaciones requerimos hacer eso de un montón de datos y muchos de ellos se necesitan almacenar, para después recuperarlos y realizar diferentes operaciones con ellos para en la mayoría de ocasiones mostrarlos como información a un usuario. En pocas palabras, necesitamos persistencia de datos y para ello existen las bases de datos, esta ocasión te mostramos como ligar a tu aplicación una base de datos MySQL pero utilizando lenguaje No-SQL para administrarla, así que ni siquiera necesitas saber SQL. (En tutoriales posteriores se muestra más información acerca de bases de datos).

#### Formularios (GET, POST, DB, Cifrar Datos)
##### Tutorial: 8
A través de los formularios HTML podemos recuperar datos, y hacer algo con esos datos en el área del servidor, por ejemplo, almacenarlos en una base de datos. Algo muy común en un sitio web es pedir a los usuarios registrarse para poder ofrecerles una mejor experiencia durante su visita, es precisamente este ejercicio el que tomamos: Sistema de gestión de usuarios, para explicar todos los elementos y aprender a cómo utilizar formularios por diferentes métodos, rutas; incluso cifrar sus datos, realizar validaciones, etc. Un vídeo bastante importante pues a partir de aquí en adelante se hacen muchas referencias a este ejercicio.

#### Cookies (Crear, leer, e información general)
##### Tutorial: 9
Hacer o no uso de cookies en un sitio web es algo sobre lo que se discute muy amenudo por diferentes cuestiones como seguridad, rendimiento y la privacidad del usuario. En esta ocasión no estaremos tocando el tema por ese lado sino solamente aprenderas a crearlas, leerlas, en fin, a utilizarlas de manera general, y sino sabes qué son te damos algunas ideas para que formes la tuya propia y les des un uso. _(Te recomedamos ver el último vídeo del curso pues hay información importante relacionada a este tema)_.

#### Sesiones (Crear, editar y eliminar; Cookies)
##### Tutorial: 10
Las sesiones están relacionadas a las cookies pues la sesión en sí misma es una cookie, pero que estas son más fáciles de utilizar pues tienen algunos valores por defecto. En ellas podemos almacenar diferente información, por ejemplo, guardar los datos de un usuario ya registrado que ha accedido con sus datos a nuestro sitio web y entonces por ejemplo, comprobar si el usuario esta navegando por nuestro sitio web a través de su cuenta o no, entre otras cosas.

#### Redirect & Url_for (Rutas; URL's)
##### Tutorial: 11
Como ya habíamos mencionado, trabajar con rutas es algo de lo más común en aplicaciones web, y dos de las acciones más requeridas son: redireccionar y aputar a diferentes rutas. Podemos lograr esto de manera sencilla utilizando las funciones redirect y url_for, incluso podemos utilizarlas en conjunto, y lograr sacar provecho de otras caracteristicas interesantes que poseen.

#### Message Flashing (Mensajes Flash [info, error, éxito, etc])
##### Tutorial: 12
Cuando un usuario utilice nuestro sitio web lo más probable es que se necesiten llevar a cabo diferentes acciones en el área del servidor que posteriormente arrojen un resultado, y una manera de informar estos resultados de manera amigable al usuario es hacer uso de los mensajes flash. De hecho me atrevería a decir que es la manera más "amigable" de hacerlo, pues estos mensajes normalmente son llamativos y no le resultan molestos al usuario pues se muestran de manera espontanea en la ruta donde se encuentra.

#### Macros (Jinja; Don't repeat yourself)
##### Tutorial: 13
Cuando estamos programando y notamos que hacemos acciones de manera bastante repetitiva creamos funciones, y así evitamos repetir código, lo que se traduce en un código mejor estructurado a la par de que desarrollamos más rápido nustro proyecto pues perdemos menos tiempo escribiendo código innecesario. Esta situación se puede aplicar a la macros que si bien no son lo mismo que una función, pues las ventajas que nos ofrecen son parecidas, en este caso en particular nosotros creamos macros a través de nuestro motor de vistas Jinja para crear plantillas HTML mejor organizadas, más eficientes, fáciles de actualizar y todo ello en menos tiempo.

#### WhiteSpacing (Jinja; remover espacios blancos)
##### Tutorial: 14
Un tutorial bastante corto donde aprendemos a evitar los espacios blancos que deja nuestro motor de vistas Jinja a la hora de ver/analizar las plantillas HTML en un navegador web. Un tema de no tanta relevancia pero que puede ser útil para tareas como depurar plantillas, y mejorar la semantica de las mismas.

#### Decoradores de petición (Before, after y teardown requests)
##### Tutorial: 15
En muchas ocasiones necesitamos realizar diferentes acciones antes, o después de una petición bajo diferentes circunstancias. Es en esta parte que hacemos uso de estos decoradores, existen varios de ellos pero aquí te mostramos tres de los que más se utilizan comúnmente.

#### Objecto Global (flask.g)
##### Tutorial: 16
A veces es necesario mover información a través de diferentes contextos en nuestra aplicación, una manera sencilla de hacerlo es hacer uso del objeto global que nos proporciona Flask al cual podemos agregarle diferentes métodos y almacenar allí información, por ejemplo: guardar conexiones/operaciones de una base de datos, la información de un usuario, etc. Algo interesante acerca de este objeto es que incluso podemos hacer uso de el a través de nuestro motor de vistas Jinja y ejecutar diferentes acciones en nuestras plantillas HTML, sin siquiera tener que importarlo pues esto se hace por defecto.

#### JSON (Jsonify)
##### Tutorial: 17
Hasta el momento hemos hablado de sitios web creados para ser utilizados por usuarios comunes, pero existen otras bases de desarrollo web que son utilizadas para crear aplicaciones, una de la bases más populares se le conoce como "RESTful API" y en muchas ocasiones estas aplicaciones utilizan las estructuras JSON para intercambiar datos y llevar a cabo diferentes tareas. Pues aquí te damos una breve introducción a ello, explicando que son las estructuras JSON y como puedes administrarlas a través de tu aplicación de Flask. _Habrá un curso exclusivo para crear este tipo de aplicaciones_.

#### Requests (GET, API to API)
##### Tutorial: 18
Haciendo uso de la librebría requests en conjunto con tu aplicación de Flask puedes comunicarte con otras aplicaciones, a través del protocolo HTTP y bajo el contexto de RESTful API. _Recordemos que habrá un curso exclusivo para este tipo de aplicaciones_ pero aún así te dejamos un sencillo ejemplo para solicitar recursos servidos por otra API.

#### Subir Archivos (y validaciones)
##### Tutorial: 19
Aprender a subir archivos mediante tu aplicación de Flask utilizando formularios HTML, algo importante en este tema es cuidar el tipo de archivos que se suben y para ello podemos realizar diferentes validaciones de seguridad, pues aquí cubrimos todo eso e incluso te mostramos como recuperar esos archivos una vez que hayan sido subidos y mostrarlos a través de una ruta de tu aplicación.

#### Manejar errores (Rutas; URL's, Códigos de estado [peticiones])
##### Tutorial: 20
Nuevamente, una de las cosas más comunes en aplicaciones web es hacer uso de diferentes rutas, y es aquí donde nos topamos con algunos errores más comúnes, como acceder a una ruta que no existe o entrar a una ruta no autorizada. Aunque se devuelven respuestas por defecto, nosotros podemos tomar tales errores y devolver respuestas personalizadas, como una plantilla personalizada para cubrir el famoso error 404 (recurso no encontrado), o incluso un JSON con un objecto que contenga el error, eso ya dependerá del concepto de nuestra aplicación.

#### Organización y configuración (básica-intermedia)
##### Tutorial: 21
Nuestra aplicación comienza a crecer después de un tiempo y es por ello que debemos tomarnos el tiempo de organizar el árbol de nuestra aplicación de alguna manera en que podamos mantener todo bajo control de una manera más sencilla. Existen varias maneras de organizar una aplicación de Flask, en esta ocasión te mostramos como hacerlo mediante el concepto paquete-modúlo-importación. Otra cosa muy importante son los párametros de configuración que necesita nuestra aplicación para funcionar, de igual manera hay diferentes prácticas para lograrlo, aquí se muestra como asignar diferentes configuraciones en base a clases (desarrollo-producción) y como recuperar los valores de configuración de diferentes maneras (variables, archivos, objetos, variables de entorno).

#### Aplicación final (Resumen de curso)
##### Tutorial: 22
Durante el curso se mostro bastante información y se abordo en muchas ocasiones de diferente manera, aunque esto no me parece que haya sido un problema pues siempre estuvo disponible el repositorio del curso en GitHub de donde podías tomar cada uno de los proyectos que se fuesen generando a lo largo del curso. De cualquiera manera en esta ocasión se dará un breve resumen del curso de manera interactiva mostrando una aplicación de Flask que ha sido creada utilizando la mayoría de información que se mosotró durante todo el curso. De hecho, es en este tutorial donde se te invitará a leer este mismo resumen que estás leyendo para que no te olvides de incluir nada que se haya enseñado en el curso en tu propio proyecto.

#### Aplicación en producción (App Deployment; App in Cloud)
##### Tutorial: 23
Llegó la hora de subir una aplicación de Flask a la nube para que los usuarios puedan hacer uso de ella desde sus respectivos dispositivos conectados a Internet, después de todo es una aplicación web. Para hacer disponible nuestra aplicación de Flask al público existen diferentes maneras de hacerlo, una de ellas es hacer uso de algún servicio de terceros. En esta ocasión lo haremos a través de PythonAnyWhere, un host gratuito y fácil de usar.

#### Base de datos remota; MySQL (App Deploymente; parte 2)
##### Tutorial: 24
Si bien cuando desarrollamos, SQLite3 es una buena herramienta para manejar nuestras bases de datos, lo cierto es que a la hora colocar nuestra aplicación en producción SQLite3 se nos comienza a quedar corto, por ello se hacen uso de otros servicios como MySQL, PostreSQL, MongoDB, entre otros. En el tutorial pasado hicimos uso de PythonAnyWhere para distribuir nuestra aplicación, pues en este mismo Host podemos configurar nuestro servicio de MySQL de manera gratuita, y entonces integrar ese servicio con nuestra aplicación de Flask sin ningún problema.

#### Final; Información importante
##### Tutorial: 25
Llegamos a nuestro final de curso, y aún quedan bastantes cosas que aprender sobre Flask, pero lo básico ya está y nos será bastante útil para seguir los siguientes tutoriales y cursos sobre el mismo, así que esten pendientes a ellos. Claro que antes de dar por finalizado el curso debemos analizar algunas cuestiones importantes sobre las aplicaciones que podemos generar con todo el conocimiento que adquirimos durante el curso.

**Dudas importantes**:
* ¿Qué más se puede hacer con Flask?
* ¿Ya está lista mi aplicación de Flask para ser puesta en producción?
	* ¿Cómo hacer uso de HTTPS?
	* ¿Qué hay del uso de Cookies y Sesiones?
	* ¿Cómo protegerse contra los ataques maliciosos más comúnes?
	* ¿Cómo mantener la configuración de mi app más segura?
	* ¿Cómo crear aplicaciones de Flask grandes de manera correcta?
* ¿Cómo puedo crear mejores aplicaciones?
* En general, ¿y ahora qué? o.o!