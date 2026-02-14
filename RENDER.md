# Deploy on Render.com (Docker)

This backend is ready to deploy as a **Web Service** using the included Dockerfile.

## Steps

1. **Push this folder as its own Git repo** (only `server_django` contents at repo root).
2. In [Render Dashboard](https://dashboard.render.com) → **New** → **Web Service**.
3. Connect your GitHub repo (the one that contains this Dockerfile at root).
4. **Environment**: Docker.
5. **Build**: Render will use the `Dockerfile` automatically.
6. **Environment variables** (required):

   | Key | Description |
   |-----|-------------|
   | `DB_HOST` | PostgreSQL host (e.g. from Render PostgreSQL). |
   | `DB_PORT` | `5432` |
   | `DB_NAME` | Database name |
   | `DB_USER` | Database user |
   | `DB_PASSWORD` | Database password |
   | `PORT` | Set by Render automatically (no need to add). |
   | `SECRET_KEY` | Random secret, e.g. `openssl rand -hex 32` |
   | `DEBUG` | `False` in production |
   | `CORS_ORIGIN` | Frontend URL, e.g. `https://your-frontend.onrender.com` |

7. If you use **Render PostgreSQL**: create a database, then set `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` from its connection info (or use a single `DATABASE_URL` if you add `dj-database-url` and change settings to read it).
8. Deploy. Migrations run on each deploy via `python manage.py migrate` in the Docker `CMD`.

## Local Docker run

```bash
docker build -t todo-django .
docker run -p 4001:4001 -e DB_HOST=host.docker.internal -e DB_PORT=5432 -e DB_NAME=todoapp -e DB_USER=todoapp -e DB_PASSWORD=xxx -e SECRET_KEY=xxx -e CORS_ORIGIN=http://localhost:5173 -e PORT=4001 todo-django
```
