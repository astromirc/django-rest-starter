# Django REST Starter

Plantilla base para proyectos Django REST Framework con PostgreSQL, Redis, Docker y AWS S3.

## Características

- **Acceso denegado por defecto**: Todos los endpoints están bloqueados. Esto obliga a definir explícitamente los `permission_classes` en la vista, evitando exponer endpoints por error.
- **Modelo User custom**: Email como username e ID con UUID7, que mantienen un orden secuencial, evitando la fragmentación en la base de datos con grandes volúmenes de información.
- **Admin seguro**: Eliminación de usuarios deshabilitada, grupos y permisos ocultos. Puedes habilitarlos según lo que necesite el proyecto.
- **Throttling**: Límites de peticiones por IP (50/min) y por usuario (200/min). Totalmente ajustable desde la configuración.
- **Cache con Redis**: Caché y sesiones preconfiguradas para usarse con Redis.
- **Lista para producción**: Gunicorn, WhiteNoise, AWS S3 y HSTS preconfigurados. Solo necesitas definir las variables de entorno.

## Requisitos

- Docker

## Instalación (Build de contenedores)

```bash
# Desarrollo
$ docker compose build

# Producción
$ docker compose -f compose.yml build
```

> **Nota:** Si usas Dev Containers al desarrollar, el build y arranque son automáticos. Evita usar `docker compose down` ya que destruye los contenedores y obliga a reconstruir el entorno al reconectar; en su lugar, usa `docker compose stop` para pausar y `docker compose start` para reanudar.

## Configuración

1. Copia el archivo `env.example` y guárdalo con el nombre `.env`.
2. Ajusta las variables de entorno del archivo `.env` según sea necesario.
3. Aplica las migraciones pendientes.

> **Nota:** En modo de desarrollo, el valor de `POSTGRES_HOST` debe ser `postgres`, que es el nombre del contenedor donde está corriendo el servidor de PostgreSQL. El resto de variables definen la base de datos y credenciales que se crearán automáticamente al levantar el servicio.

## Comandos

Comandos para gestionar el entorno desde la terminal:

```bash
# Iniciar / Levantar contenedores en segundo plano
$ docker compose up -d

# Pausar contenedores (mantiene datos e instancias)
$ docker compose stop

# Reanudar contenedores pausados
$ docker compose start

# Destruir contenedores y redes
$ docker compose down

# Entrar al contenedor del backend
$ docker compose exec backend bash
```

> **Nota:** En producción, especifica el archivo base pasando `-f compose.yml` (ej. `docker compose -f compose.yml up -d`).

## Comandos de la aplicación

Comandos disponibles dentro del contenedor:

```bash
# Crear migraciones
$ python manage.py makemigrations

# Aplicar migraciones
$ python manage.py migrate

# Crear superusuario
$ python manage.py createsuperuser

# Ejecutar tests
$ python manage.py test

# Ejecutar linter
$ linter
```

## Conexión a PostgreSQL desde la máquina anfitriona

Puedes conectarte a PostgreSQL desde la máquina anfitriona utilizando `localhost` como host y el puerto `5432`. Esto permite acceder a la base de datos mediante herramientas como gestores de bases de datos o clientes SQL.

## Stack Tecnológico

- **Framework**: Django y Django REST Framework
- **Base de datos**: PostgreSQL
- **Cache**: Redis
- **Servidor**: Gunicorn
