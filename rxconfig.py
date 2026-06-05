import reflex as rx
import os

database_url = os.environ.get("DATABASE_URL", "sqlite:///reflex.db")

config = rx.Config(
    app_name="nuevo_curso_reflex",
    db_url=database_url,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)