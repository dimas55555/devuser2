#!/bin/sh

set -e

echo "Waiting for database..."

until pg_isready -h db -U postgres; do
  sleep 2
done

echo "Running Alembic migrations..."
alembic upgrade head

echo "Migrations applied successfully"