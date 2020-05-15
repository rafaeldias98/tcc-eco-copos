# Eco Copos - TCC
*Information Systems course conclusion work (a.k.a TCC, in portuguese)*

---

## Members of TCC
- Norbert Csasznik
- Leonardo Biscuola Scarpa
- Rafael Dias da Silva
- Richard Oliveira da Silva

---

## Development
- Rafael Dias da Silva

---

## Pre-requisites

`docker version 17+` See how to download and install in [Docker site.][3]

`docker-compose version 1.20+` See how to download and install in [Docker site.][4]

Basically the project uses [`pypy3`][1] to run and the dependencies are set using [`pip`][2].

---

## Development

### Generating environment variables

Copy env vars:
```bash
cp .env.example .env
```

Start docker-compose services:
```bash
docker-compose up
```

## URLs

### Product list page

| environment | url                                       |
|-------------|-------------------------------------------|
| development | http://localhost/products/                |

### Product detail page

| environment | url                                       |
|-------------|-------------------------------------------|
| development | http://localhost/{id-of-product}/         |

### About us page

| environment | url                                       |
|-------------|-------------------------------------------|
| development | http://localhost/about-us/                |

### Admin page

| environment | url                                       |
|-------------|-------------------------------------------|
| development | http://localhost/admin/                |

## Todo List
- Security:
https://django-simple-captcha.readthedocs.io/en/latest/usage.html#installation
