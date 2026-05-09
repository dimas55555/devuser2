#!/bin/sh

set -e

echo "Waiting for database..."

until pg_isready -h db -U postgres || pg_isready -h postgres -U postgres; do
  sleep 2
done

echo "Creating schema travel if not exists..."

psql "$DATABASE_URL" -c "CREATE SCHEMA IF NOT EXISTS travel;"

echo "Running Alembic migrations..."
alembic upgrade head

echo "Migrations applied successfully"