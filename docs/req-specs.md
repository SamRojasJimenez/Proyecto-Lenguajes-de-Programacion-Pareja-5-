# Documento de Requerimientos y Especificaciones: Control de Donaciones a la Biblioteca (Pareja 5)

## 1. Perfil del Proyecto
Este documento define los requerimientos para la aplicación web de gestión de donaciones, diseñada siguiendo una arquitectura de microservicios simplificada basada en 3 capas orquestadas por contenedores.

**Temática:** Control de Donaciones a la Biblioteca
**Asignatura:** Teoría y Taller Lenguaje de Programación 2025 (Universidad de Oriente)

## 2. Pila Tecnológica
*   **Frontend:** PHP (Landing Page y Sistema CRUD).
*   **Backend Lógico:** Scripting en Python (Generador de reportes).
*   **Persistencia:** Base de Datos (MySQL).
*   **Infraestructura:** Docker & Docker Compose.

## 3. Especificaciones de la Base de Datos
La base de datos debe inicializarse automáticamente mediante un script `script.sql` ubicado en la carpeta `/docker-entrypoint-initdb.d/` del contenedor de base de datos.

### 3.1. Modelo de Datos
*   **Tabla `donaciones`**:
    *   `id`: PK, Autoincremental.
    *   `donante`: Texto.
    *   `titulo_libro`: Texto.
    *   `fecha_donacion`: Date/Time.
    *   `procesado_inventario`: Boolean (Procesado/Por procesar).

## 4. Capa Web (PHP) - Requerimientos de Interfaz
### 4.1. Landing Page (`index.php`)
*   Sección de Portafolio Profesional: Carga dinámica de la Bio, Foto y Habilidades del alumno desde la tabla `portafolio`.

### 4.2. Sistema de Gestión de Donaciones
*   **Formulario de Registro**: Captura de datos de donación con validación de campos obligatorios.
*   **Tabla de Registros**: Visualización de todas las donaciones.
*   **Acciones por Fila (CRUD)**:
    *   **Cambiar Estado**: Alternar valor booleano (`UPDATE`) de `procesado_inventario`.
    *   **Leer**: Visualización de detalles en la misma página.
    *   **Editar**: Modificación de `donante` o `titulo_libro` (`UPDATE`).
    *   **Eliminar**: Borrado físico del registro (`DELETE`).

### 4.3. Seguridad y UX
*   **Seguridad**: Uso obligatorio de **Sentencias Preparadas (PDO)** para interactuar con la DB.
*   **Optimización**: Implementación de **AJAX** para ejecutar las acciones (cambiar estado, eliminar, editar) sin recargar la página.

## 5. Backend Lógico (Python)
*   Script independiente que se conecta a la DB para realizar consultas de agregación.
*   **Función**: Generar un archivo `reporte.txt` con el total histórico de libros donados.
*   **Integración**: Este archivo debe ser guardado en un volumen compartido con el servidor PHP para su visualización desde la interfaz web.

## 6. Infraestructura (Docker)
*   **Orquestación**: Un archivo `docker-compose.yml` que gestione los 3 servicios (Web, Python, DB).
*   **Persistencia**: Uso de volúmenes de Docker vinculados a la base de datos para asegurar que los datos no se pierdan al reiniciar contenedores.
*   **Comunicación**: Red interna de contenedores y volúmenes compartidos para intercambio de reportes.

## 7. Criterios de Entrega
*   Código fuente en repositorio GitHub organizado con `.gitignore`.
*   Uso de ramas: `feature/database`, `feature/web`, `main`.
*   **Video Demostrativo**: Deberá mostrar la ejecución de `docker-compose up`, inserción de datos, edición, borrado y prueba de persistencia.