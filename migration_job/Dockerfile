FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x migration_job/entrypoint.sh

CMD ["sh", "migration_job/entrypoint.sh"]