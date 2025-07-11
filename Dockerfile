ARG PYTHON_VERSION=3.11.9
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV TZ=Europe/Warsaw
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]