FROM php:8.0-apache

# Instalar extensiones necesarias para MySQL
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Habilitar mod_rewrite para Apache (opcional pero recomendado)
RUN a2enmod rewrite

# Establecer el directorio de trabajo
WORKDIR /var/www/html

# Asegurar permisos para la carpeta de reportes compartida
RUN mkdir -p /var/www/html/reports && chown -R www-data:www-data /var/www/html/reports
