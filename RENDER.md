# Deploy on Render.com (Docker)

This backend is ready to deploy as a **Web Service** using the included Dockerfile.

## Database connection (important)

The app connects to PostgreSQL using **either**:

- **`DATABASE_URL`** (recommended on Render) – single URL; Render sets this automatically when you add a PostgreSQL database and link it to the service.
- **Or** `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` – if you prefer to set them manually.

If none are set, it falls back to `localhost`, which **fails on Render** (no PostgreSQL on the container). So you must either link a Render PostgreSQL database (so `DATABASE_URL` is set) or set the `DB_*` variables yourself.

## Steps

1. **Push this folder as its own Git repo** (only `server_django` contents at repo root).
2. In [Render Dashboard](https://dashboard.render.com):
   - **New → PostgreSQL** – create a database if you don’t have one.
   - **New → Web Service** – connect your GitHub repo (Dockerfile at root).
3. **Environment**: Docker.
4. **Link PostgreSQL** (so Render sets `DATABASE_URL` automatically):
   - In the Web Service → **Environment** → **Add Environment Variable**.
   - Or in the database’s page, use **Connect** and choose your Web Service; Render will add `DATABASE_URL` (use the **Internal Database URL** for services in the same account).
5. **Other environment variables**:

   | Key | Description |
   |-----|-------------|
   | `DATABASE_URL` | Set automatically if you linked the PostgreSQL DB. Otherwise paste the **Internal Connection String** from the database’s **Info** tab. |
   | `SECRET_KEY` | Random secret, e.g. `openssl rand -hex 32` |
   | `DEBUG` | `False` in production |
   | `CORS_ORIGIN` | Frontend URL, e.g. `https://your-frontend.onrender.com` |
   | `PORT` | Set by Render (do not add). |

6. Deploy. Migrations run on each deploy via `python manage.py migrate` in the Docker CMD.

## If you don’t link the database

Set these manually instead of `DATABASE_URL` (from your Render PostgreSQL **Info** tab):

- `DB_HOST` – hostname (e.g. `dpg-xxxxx-a.oregon-postgres.render.com`)
- `DB_PORT` – `5432`
- `DB_NAME` – database name
- `DB_USER` – user
- `DB_PASSWORD` – password

**Do not** use `localhost` as `DB_HOST` on Render; the database runs on a different host.

## Local Docker run

```bash
docker build -t todo-django .
docker run -p 4001:4001 -e DATABASE_URL="postgresql://user:pass@host.docker.internal:5432/todoapp" -e SECRET_KEY=xxx -e CORS_ORIGIN=http://localhost:5173 -e PORT=4001 todo-django
```

Or with `DB_*`:

```bash
docker run -p 4001:4001 -e DB_HOST=host.docker.internal -e DB_PORT=5432 -e DB_NAME=todoapp -e DB_USER=todoapp -e DB_PASSWORD=xxx -e SECRET_KEY=xxx -e CORS_ORIGIN=http://localhost:5173 -e PORT=4001 todo-django
```
