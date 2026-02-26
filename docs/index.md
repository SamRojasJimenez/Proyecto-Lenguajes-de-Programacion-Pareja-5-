# Bitácora de Desarrollo - Proyecto Final de Lenguajes

Este documento resume el progreso y las decisiones técnicas tomadas durante la sesión de trabajo para el proyecto de la **Pareja 5: Control de Donaciones a la Biblioteca**.

## Sesión de Trabajo: 25-02-2026

### 1. Análisis y Planificación
*   **Fuente**: Se analizó la guía oficial del proyecto (`Proyecto Lenguaje alumnos 1 (1).pdf`).
*   **Definición de Requerimientos**: Se creó el archivo `docs/req-specs.md` detallando la arquitectura de 3 capas y los requisitos específicos para la Pareja 5.
*   **Temática**: Sistema de gestión de donaciones con microservicios de Python para reportes.

### 2. Infraestructura y DevOps
*   **Orquestación**: Implementación de `docker-compose.yml` para gestionar tres servicios:
    *   `db`: MySQL 8.0 con persistencia mediante volúmenes.
    *   `web`: Apache+PHP 8.0 con extensiones PDO.
    *   `logic`: Python 3.9 para procesamiento de datos.
*   **Dockerfile Custom**: Se crearon entornos optimizados tanto para PHP (con `pdo_mysql`) como para Python (con el conector de base de datos).
*   **Control de Versiones**: Creación de `.gitignore` para proteger datos de base de datos y guías de Conventional Commits en `docs/git-convencional.md`.

### 3. Desarrollo de Aplicación
*   **Base de Datos**: Diseño del esquema en `src/db/script.sql` con inicialización automática de tablas para donaciones.
*   **Capa Web (PHP)**:
    *   Interfaz moderna con tema oscuro y diseño responsivo.
    *   Implementación de CRUD completo (Crear, Leer, Editar Estado, Eliminar).
    *   Seguridad mediante el uso de Sentencias Preparadas (PDO).
*   **Capa Lógica (Python)**:
    *   Desarrollo de `report.py` para conteo automático de registros.
    *   Integración mediante volumen compartido para que el reporte sea visible en el frontend PHP.

### 4. Depuración y Ajustes Técnicos
*   **UTF-8 y Codificación**: Se corrigieron problemas de visualización de caracteres especiales (tildes y eñes) mediante:
    *   Ajuste de `ENGINE` y `CHARSET` en el script SQL.
    *   Configuración de `PDO::MYSQL_ATTR_INIT_COMMAND` en PHP.
    *   Inyección de `header` y `mb_internal_encoding` en el servidor.
*   **Simplificación de Interfaz**: Se realizaron ajustes en el código PHP para enfocar la aplicación estrictamente en la gestión de donaciones según el feedback del usuario.

## Estado Actual
- [x] Infraestructura Docker base.
- [x] Base de Datos funcional con inicialización.
- [x] Interfaz Web CRUD operativa.
- [x] Sincronización Python/PHP mediante reportes.
- [x] Guía de Git terminada.

---
*Próximos pasos sugeridos: Realizar el video demostrativo y subir el código a las ramas correspondientes en GitHub.*
