-- samuel
Hola gemini, este es un documento que describe un trabajo de lenguajes de programacion que debo realizar, a mi me toca la de la pareja 5 (control de donaciones de biblioteca), podrias crear crear un prompt para crear todo el proyecto en antigravity (utilizando un solo promt)

-- gemini
¡Hola! Entiendo perfectamente la situación. Estás buscando un "mega-prompt" para generar la estructura completa de tu proyecto final para la Universidad de Oriente. Usar una herramienta generativa (como Antigravity, Bolt, Cursor o Claude) es una excelente estrategia para arrancar con buen pie y orquestar toda la infraestructura rápidamente.

Sin embargo, como inteligencia artificial, te recomiendo que estudies detenidamente el código que la herramienta te genere. Recuerda que uno de los entregables es un video demostrativo donde debes mostrar la ejecución de los comandos, el funcionamiento del CRUD y demostrar la persistencia de datos apagando y encendiendo los contenedores. Si no entiendes cómo se conectan las piezas, podría ser difícil defender el trabajo.

He redactado un prompt estructurado y optimizado que abarca todos los requisitos generales y los específicos de la **Pareja 5 (Control de Donaciones a la Biblioteca)**.

Copia el texto que está en el bloque a continuación y pégalo en la herramienta que vayas a utilizar:

> **Rol y Objetivo:**
> Actúa como un desarrollador Full-Stack y experto en DevOps. Tu objetivo es crear el código completo y los archivos de configuración para una aplicación web de 3 capas (Frontend, Backend Lógico, Persistencia) orquestada con Docker. El sistema simulará una arquitectura de microservicios simplificada.
> 
> 
> **Pila Tecnológica:**
> * **Frontend:** PHP.
> * **Backend Lógico:** Scripting en Python.
> * **Base de Datos:** PostgreSQL o MySQL usando la imagen oficial.
> * **Infraestructura:** `docker-compose.yml` para orquestar los 3 contenedores.
> 
> 
> **Requerimientos de la Base de Datos (Inicialización y Esquema):**
> * Utiliza un script automático `script.sql` ubicado en `/docker-entrypoint-initdb.d/` para inicializar la base de datos y las tablas al levantar el contenedor.
> * **Tabla 1 (Portafolio):** Crea una tabla para almacenar los datos del alumno (Foto, Biografía, Habilidades).
> * **Tabla 2 (Donaciones):** Crea la tabla `donaciones` con las siguientes columnas: `id` (PK, Autoincremental), `donante` (Texto), `titulo_libro` (Texto), `fecha_donacion` (Date/Time), y `procesado_inventario` (Boolean).
> 
> 
> **Requerimientos del Frontend (PHP) - Capa Web:**
> * Crea un archivo `index.php` que funcione como una Landing Page mostrando la información del alumno obtenida desde la base de datos.
> * Incluye un formulario para insertar nuevas donaciones validando que los campos no estén vacíos.
> * Muestra una tabla con los registros de la base de datos.
> 
> 
> * Cada fila de la tabla debe incluir botones de acción para:
> * **Cambiar Estado:** Alternar el valor booleano entre "Procesado" o "Por procesar" mediante un UPDATE.
> * **Leer:** Mostrar una lista de los datos recibidos en la misma página.
> * **Editar:** Modificar el título del libro o el donante mediante un UPDATE.
> * **Eliminar:** Borrar el registro completamente mediante un DELETE.
> * **Seguridad Obligatoria:** Todas las interacciones con la base de datos desde PHP deben usar sentencias preparadas (ej. PDO) para prevenir inyecciones SQL.
> * **Desafío Opcional:** Implementa las acciones de los botones (cambiar estado, eliminar, editar) utilizando JavaScript y AJAX para evitar recargar la página.
> 
> 
> 
> 
> **Requerimientos del Backend Lógico (Python):**
> * Crea un script en Python que se conecte a la base de datos y genere un reporte calculando el total histórico de libros donados.
> * El resultado de este conteo debe guardarse en un archivo llamado `reporte.txt`.
> 
> 
> **Requerimientos de Docker y Volúmenes:**
> * Implementa Volúmenes de Docker para la base de datos para garantizar la persistencia de la información si el contenedor se apaga.
> * Implementa un **Volumen Compartido** entre el contenedor de Python y el contenedor de PHP para que el archivo `reporte.txt` generado por Python sea visible y se pueda leer desde el Frontend en PHP.
> 
> 
> Por favor, entrégame el contenido exacto de los archivos necesarios (`docker-compose.yml`, `Dockerfile` si es necesario, `script.sql`, `index.php`, script de Python, y archivos JS/CSS) estructurados claramente.

---

### Recomendaciones adicionales para tu entrega:

* 
**Git y GitHub:** No olvides crear tu archivo `.gitignore` para no subir contraseñas ni carpetas innecesarias.


* 
**Ramas:** Trabaja usando las ramas `feature/database`, `feature/web` y `main` tal como exige la guía.



¿Te gustaría que repasemos juntos cómo funciona el archivo `docker-compose.yml` que va a conectar estas tres capas, o prefieres que te ayude a estructurar el guion para tu video demostrativo?

