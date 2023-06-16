# Django

## Install:

We need to install [docker and docker-compose](https://docs.docker.com/compose/install/).

## Run:

Clone this repository and run:

```sh
docker-compose -f docker-compose.dev.yml up --build 
```

## Useful docker commands:

### Start server:
```sh
docker-compose -f docker-compose.dev.yml run web python3 manage.py runserver 0.0.0.0:80
```

### Log into web container:
```sh
docker exec -itu 'user:group' 'container name (docker-compose ps)' bash
```

### Start django project:
```
docker-compose -f docker-compose.dev.yml run web -u $(id -u):$(id -g) django-admin startproject mysite
```

## Access webpage:

- IP ADDRESS: 10.10.0.5
# planet-catalog
