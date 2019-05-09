FROM tiangolo/uwsgi-nginx-flask:python3.7
COPY ./lipwig /app/lipwig
COPY ./uwsgi.ini /app
