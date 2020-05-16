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

`docker version 17+` See how to download and install in [Docker site.][1]

`docker-compose version 1.20+` See how to download and install in [Docker Compose site.][2]

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
- [x] README
- [x] Security

[1]: https://docs.docker.com/install/linux/docker-ce/ubuntu/
[2]: https://docs.docker.com/compose/install/#install-compose
