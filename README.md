Monitoring - the service to monitor the given url changes. 

To initialize Postgres we should run Alembic migrations. To install Alembic and its dependencies run:
```
pip install -r requirements.txt
```

For initialization to work we have to expose Postgres ports by adding
```
ports:
  - '5432:5432'
```
to the `docker-compose.yaml` file.

After that we run the container and create the database:
```
docker compose up db
```
```
docker exec postgres_db_container createdb -U postgres snapshots
```
And apply alembic migrations:
```
alembic upgrade head
```

Now we can remove the ports part
```
ports:
  - '5432:5432'
```

and run the app via
```
docker compose up
```