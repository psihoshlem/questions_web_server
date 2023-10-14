import os

DB_HOST: str = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT: str = os.environ.get("DB_PORT", "5432")
DB_USER: str = os.environ.get("DB_USER", "postgres")
DB_PASSWORD: str = os.environ.get("DB_PASSWORD", "1234")
DB_NAME: str = os.environ.get("DB_NAME", "questions")