from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool, text
from alembic import context

from src.config import get_settings
from src.db.entities import Base

# Alembic config object
config = context.config

# -----------------------------
# Load DB URL from Settings
# -----------------------------
config.set_main_option(
    "sqlalchemy.url",
    get_settings().DATABASE_URL
)

# -----------------------------
# Metadata for autogenerate
# -----------------------------
target_metadata = Base.metadata

# -----------------------------
# Schema name (methodology requirement)
# -----------------------------
SCHEMA_NAME = "travel"


# -----------------------------
# Filter objects for schema
# -----------------------------
def include_object(object, name, type_, reflected, compare_to):
    if type_ == "table":
        return object.schema == SCHEMA_NAME
    return True


# -----------------------------
# OFFLINE MIGRATIONS
# -----------------------------
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
    )

    with context.begin_transaction():
        context.run_migrations()


# -----------------------------
# ONLINE MIGRATIONS
# -----------------------------
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:

        # 🔥 CREATE SCHEMA IF NOT EXISTS (FIX FOR YOUR ERROR)
        connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME}"))

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()