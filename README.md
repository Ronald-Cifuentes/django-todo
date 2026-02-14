# Django Backend

## Setup

1. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy environment file:
```bash
cp .env.example .env
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start server:
```bash
python manage.py runserver 4001
```

## Health Check

```bash
curl http://localhost:4001/health
```
