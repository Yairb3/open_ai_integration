FROM python:3.11.9
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary
COPY . .
EXPOSE 5000
CMD ["sh", "-c", "alembic upgrade head && python3 app.py"]
