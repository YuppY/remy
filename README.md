# Order API

## Running

1. Install Docker Compose

2. Initialize containers and the database:
```bash
docker-compose run app wait-for-it db:5432 -- ./manage.py migrate
```
3. Start the application:
```bash
docker-compose up
```

## Admin interface access

1. Create a superuser:
```bash
docker-compose run app ./manage.py createsuperuser
```

2. Login into the admin interface of the running app via http://localhost:8000/admin/
