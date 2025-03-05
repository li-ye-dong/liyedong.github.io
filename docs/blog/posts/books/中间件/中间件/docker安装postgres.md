```bash
docker pull postgres:12
docker run -d \
  --name db \
  --restart always \
  -p 5432:5432 \
  -v app-db-data:/var/lib/postgresql/data/pgdata \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -e POSTGRES_PASSWORD=root \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=app \
  postgres:12

```

