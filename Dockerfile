FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 5000

CMD alembic upgrade head && flask run --host=0.0.0.0 --port=5000