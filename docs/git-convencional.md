# Guía de Conventional Commits

Conventional Commits es una especificación ligera sobre los mensajes de commit. Proporciona un conjunto fácil de reglas para crear un historial de commits explícito, lo que facilita la creación de herramientas automatizadas encima.

Esta convención encaja perfectamente con el requerimiento de tu proyecto de mantener un control de versiones organizado en GitHub.

## Estructura del Mensaje

El mensaje de commit debe estar estructurado de la siguiente manera:

```text
<tipo>[contexto opcional]: <descripción>

[cuerpo opcional]

[nota(s) al pie opcional(es)]
```

## Tipos de Commit Principales

*   **`feat`**: Una nueva característica para el usuario (se correlaciona con `MINOR` en semantic versioning).
    *   *Ejemplo:* `feat: agregar formulario de registro de donaciones`
*   **`fix`**: Una solución a un error (se correlaciona con `PATCH` en semantic versioning).
    *   *Ejemplo:* `fix: corregir codificación UTF-8 en nombres con tildes`
*   **`docs`**: Cambios en la documentación.
    *   *Ejemplo:* `docs: crear guía de conventional commits`
*   **`style`**: Cambios que no afectan el significado del código (espacios en blanco, formato, puntos y comas faltantes, etc.).
*   **`refactor`**: Un cambio en el código que ni corrige un error ni añade una característica.
*   **`test`**: Añadir pruebas faltantes o corregir pruebas existentes.
*   **`chore`**: Cambios en el proceso de construcción o herramientas auxiliares y librerías.
    *   *Ejemplo:* `chore: actualizar docker-compose para incluir volúmenes`

## Beneficios para tu Proyecto

1.  **Claridad**: Cualquier persona (o el profesor) que vea tu repositorio entenderá qué hiciste en cada paso sin leer el código.
2.  **Organización por Ramas**: Puedes usar estos tipos para tus ramas:
    *   `feature/web` -> commits tipo `feat` o `fix`.
    *   `feature/database` -> commits tipo `feat` o `chore`.
3.  **Historial Profesional**: Demuestra un alto nivel de madurez técnica en el taller de lenguajes de programación.

## Ejemplo de un historial de commits para la Pareja 5:

1. `feat: configurar infraestructura inicial con docker-compose`
2. `feat(db): definir esquema SQL para tabla de donaciones`
3. `feat(web): implementar interfaz CRUD con PHP y estilos premium`
4. `fix(web): corregir visualización de caracteres especiales`
5. `feat(logic): añadir script de python para generación de reportes`
