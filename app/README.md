# Backend Boilerplate Python Django

## Project Code

The project code is located under `app-backend/`.

## Getting started

1. Make sure [`python3`](https://www.python.org/downloads/) and [`pip3`](https://pip.pypa.io/en/stable/installing/) are installed on your local env.

2. Build your app.

```bash
pip3 install -r requirements.txt && python3 manage.py migrate
```

3. Start your app.

```bash
python3 manage.py runserver
```

Locally:

- App should be started at `http://127.0.0.1:8000` and swagger documentation you can find at `/swagger`

Codespaces:

- You should see a popup telling you app started at `http://127.0.0.1:8000` prompting you to `Open in Browser`, which will forward that to a public url that you can access. Swagger documentation can be found at `/swagger`
