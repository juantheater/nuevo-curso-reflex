"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(
            position="bottom-right"
        ),
        rx.vstack(
            rx.heading(
                "Bienvenido a Reflex!",
                 size="9"
            ),
            rx.text(
                "Listos para comenzar",
                size="7"    
            ),
            rx.link(
                rx.button("Docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
