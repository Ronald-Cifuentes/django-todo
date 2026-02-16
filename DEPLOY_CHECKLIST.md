# Checklist para deploy en Render

Asegúrate de que el **repo que conectas a Render** tenga exactamente estos archivos/cambios (si despliegas solo esta carpeta como repo):

## Archivos que deben estar en el repo

- `todoapp/urls.py` – con `path('api', views.api_root)` y `path('api/', include('todos.urls'))`
- `todoapp/exceptions.py` – con logging del traceback (logger.exception + traceback.print_exc)
- `todos/views.py` – con `root`, `api_root`, `health_check`, `todo_list`, `todo_detail`
- `todos/urls.py` – con `path('', views.api_root)` además de `todos` y `todos/<str:id>`
- `todos/migrations/0001_initial.py` – **imprescindible** para que exista la tabla `todos` en la DB

## Después de push

1. En Render → tu Web Service → **Manual Deploy** (o espera el auto-deploy).
2. En el deploy, debe ejecutarse `python manage.py migrate --noinput` (en el CMD del Dockerfile).
3. Revisa **Logs**: si `/api/todos` sigue dando 500, debería aparecer el traceback completo (por el cambio en `exceptions.py`).

## Comprobar que todo está pusheado

```bash
git status
git log -1 --name-only   # últimos archivos en el último commit
```

Si `todos/migrations/0001_initial.py` no está en el repo, `/api/todos` seguirá dando 500 (tabla no existe).
