# ToDoChallenge Invera

Desafio planteado por **Invera**. Desarrollo de una AppWebAPI ToDoList con backend (Django) y frontend (HTML y Bootstrap), con manejo de logs y dockerización del proyecto.

## Requerimientos

Es necesario instalar Docker y es recomendable utilizar una terminal Linux (WSL2.0 servira en el caso de SO Windows)

## Instalación

Como primer paso debe clonarse el repositorio y moverse a la carpeta donde se halla el mismo

```
git clone https://github.com/IgnacioBarroso/todo-challenge.git
```

El segundo paso es hacer Build de la imagen del contenedor con el siguiente comando. (Podria darse cualquier nombre)

```
docker build -t todochallenge .
```

Una vez construida la imagen, se debe correr la misma exponiendo sus puertos y dandole nombre al contenedor

```
docker run -p 8000:8000 --name todolist todochallenge
```

Finalizado el proceso de instalación, ya puede ser utilizada la App e interactuar con sus funciones accediendo a la misma desde la direccion **(0.0.0.0:8000)** en su navegador.

## Resumen del proyecto

Alli se encontrara con un login donde puede acceder si ya posee un usuario creado, de lo contrario debera registrarse, podra ingresar desde el endpoint /register o desde SignUp debajo en el login. Una vez registrado podra ingresar a la aplicacion como administrador e interactuar con las Task que quiera crear. Tambien tendra la posibilidad de buscar determinados Task filtrandolos por contenido y/o fecha, cambiar su estado de pending a check y borrar si lo necesita. Una vez finalizados los cambios e interaccion con la App, puede hacer logout de la misma y cerrar asi su sesion. La aplicación en cuanto a frontend esta diseñada para ser lo mas intuitiva posible, con un diseño minimalista, centrado y responsive, por lo que, aseguro, no tendra problemas en su uso.

## Herramientas utilizadas

Python - Django - Bootstrap - SQLite3 

### ¡Muchas gracias por chequear el proyecto!

Invito a los revisores a ver mis otros repositorios y consultar conmigo via redes sociales, todo estara en mi README personal. ¡Saludos!
