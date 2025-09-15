from app.factory import create_app


app = create_app()

# run using: gunicorn -w 4 -b 0.0.0.0:7000 wsgi:app