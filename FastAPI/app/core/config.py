import os


class Settings:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "0.0.0.0")
    POSTGRES_PORT: str = os.getenv(
        "POSTGRES_PORT", 5432
    )  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "postgres")
    DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{POSTGRES_DB}"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
    ALGORITHM = "HS256"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "aboba")  # should be kept secret
    JWT_REFRESH_SECRET_KEY = os.getenv(
        "JWT_REFRESH_SECRET_KEY", "aboba"
    )  # should be kept secret


settings = Settings()
