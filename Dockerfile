FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py collectstatic --noinput
CMD python manage.py migrate && gunicorn dar_market.wsgi:application --bind 0.0.0.0:$PORT
