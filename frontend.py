from fastapi import FastAPI
from nicegui import app, ui

from dotenv import load_dotenv
import os
load_dotenv()

# loading my api key from .env file  - you can replace os.getenv("API_KEY") with your API KEY
hidden_key = os.getenv("SECRET_KEY")


def init(fastapi_app: FastAPI) -> None:
    @ui.page('/show')
    def show():
        ui.label('Hello, FastAPI!')

        # NOTE dark mode will be persistent for each user across tabs and server restarts
        ui.dark_mode().bind_value(app.storage.user, 'dark_mode')
        ui.checkbox('dark mode').bind_value(app.storage.user, 'dark_mode')

    ui.run_with(
        fastapi_app,
        # NOTE setting a secret is optional but allows for persistent storage per user
        storage_secret=hidden_key,
    )
